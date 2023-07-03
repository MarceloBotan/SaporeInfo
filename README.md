# SaporeInfo

SaporeInfo é uma aplicação para inventariar as máquinas que conectam no RDP da Sapore

As informações coletadas são:
- Informações do Sistema Operacional
- Especificações do Hardware
- Softwares Padrões Instalados

## Configuração
Altere os caminhos para a coleta e download dos arquivos nos .bat e .vbs

## CollectTxt

Essa ferramenta faz a coleta dos arquivos .txt dos servidores do RDP

### Configuração
Adicione as configurações locais
```bash
PATH = 'C:\\path_to_collected_txt_in_RDP'
SERVER_PATH = '\\\\server_name'
COLLECTED_TXT_PATH = 'C$\\path_to_collected_txt_in_RDP'

QTD_SERVERS = 0
```

## InsertTxtInDb

Essa ferramenta faz a leitura dos arquivos .txt e insere os dados em um banco de dados

### Configuração
Adicione as configurações locais
```bash
DB_INFO = {
  'host': 'host',
  'user': 'user',
  'password': 'password',
  'database': 'database'
}

COLUMNS = [
    'username', 'collected_at', 'column_name3', 'column_name4', 'column_name5'
]

COLLECTED_TXT_PATH = 'temp\\'
```

## Compilar as Ferramentas em .exe

Para compilar essas ferramentas .py em um arquivo .exe, instale os módulos descritos no arquivo requirements.txt em um ambiente virtual

### Criar um ambiente virtual
```bash
python -m venv venv
```

### Instalar o requirements.txt
```bash
pip install -r requirements.txt
```

### Compilar em um arquivo .exe
O arquivo será compilado em um arquivo .exe no diretório "collect_txt/dist"
```bash
pyinstaller update_files.py --onefile
```