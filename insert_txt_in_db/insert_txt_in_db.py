import os
import re
from local_settings import COLUMNS, COLLECTED_TXT_PATH, DB_INFO
import mysql.connector

cnx = mysql.connector.connect(
  host=DB_INFO['host'],
  user=DB_INFO['user'],
  password=DB_INFO['password'],
  database=DB_INFO['database']
)

PATH = 'temp\\'

exclude_info = False

def decode_txt(txt) -> str:
    decode_dict = {
        'False': 'F',
        'True': 'T',
        'null': 'N',
        '': 'N',
    }

    decoded = txt

    try:
        decoded = decode_dict[txt]
    except:
        ...

    return decoded

def get_info(lines) -> list:
    list_values = []

    for l in lines:
        if 'powershell' in l:
            continue

        c_name = l.replace('\n','').split(':')

        if 'Hora de in' in c_name[0]:
            c_name[0] = COLUMNS[1]
            regex = re.compile(r'(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})')
            split_date = regex.findall(c_name[1])[0]
            datetime = ''
            for i, date in enumerate(split_date):
                datetime += str(date)
                if i < len(split_date)-1:
                    datetime += '-'
        
        if 'dateInstall' in c_name[0] or 'date_install' in c_name[0]:
            c_name[0] = 'os_installed_at'

        if 'ignore' in c_name[0] and c_name[1] == 'True':
            global exclude_info
            exclude_info = True

        if c_name[0] in COLUMNS:
            value = c_name[1].strip()

            value = decode_txt(value)

            list_values.append(value)

    return list_values

def get_qs() -> str:
    global exclude_info
    _columns = COLUMNS
    qs = "REPLACE INTO computers ("
    
    if exclude_info:
        qs = "DELETE FROM COMPUTERS WHERE SERIALNUMBER = %s"
        return qs

    qs_values = 'VALUES('
    for c in _columns:
        if c == _columns[-1]:
            qs += c + ')'
            qs_values += '%s)'
            continue
        qs += c + ', '
        qs_values += '%s, '
    
    return qs + qs_values

def save_info(file_name: str) -> None:
    with open(PATH + file_name) as file:
        lines = file.readlines()

        username = file_name.split('_')[0]

        info = get_info(lines)
        if info == '':
            return

        list_values = [username]
        list_values += info

        cursor = cnx.cursor()

        try:
            global exclude_info
            if exclude_info:
                cursor.execute((get_qs()), (list_values[6],))
                print('Delete from database', username, 'computer\'s')
                return

            cursor.execute((get_qs()), list_values)
            print('Saved in database', username, 'computer\'s')
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)

if __name__ == '__main__':
    list_dir = ''
    try:
        list_dir = os.listdir(PATH)
    except:
        print('Directory ' + PATH + ' not found')

    for file_name in list_dir:
        if '.txt' not in file_name:
            continue

        try:
            save_info(file_name)
        except Exception as e:
            print(e, 'on file', file_name)
            continue

        os.remove(PATH + file_name)
        print('Deleted file', file_name)
    

    cnx.commit()
    cnx.close()

    os.system(r'PAUSE')