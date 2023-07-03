import os
from distutils.dir_util import copy_tree
import shutil
from local_settings import PATH, SERVER_PATH, COLLECTED_TXT_PATH
from local_settings import  QTD_SERVERS


for i in range(0, QTD_SERVERS):
    server_path = SERVER_PATH + str(i) + '\\' + COLLECTED_TXT_PATH
    try:
        dir_list = os.listdir(server_path)
        dir_list_local = os.listdir(PATH)
        if dir_list_local == dir_list:
            continue
    except:
        continue

    try:
        copy_tree(server_path, PATH)
        print('Copied', dir_list, f'from {SERVER_PATH}' + str(i))
        shutil.rmtree(server_path)
        print('Deleted', dir_list, f'from {SERVER_PATH}' + str(i))
    except:
        continue

os.system(r'PAUSE')