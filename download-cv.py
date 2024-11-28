from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"] # Define o escopo para pegar apenas os arquivos com permissão de leitura

creds = Credentials.from_authorized_user_file('token.json', SCOPES) # Colhendo nossas credenciais do arquivo token.json. É necessário rodar o script de autenticação para gerar este arquivo. 

service = build('drive', 'v3', credentials=creds)

folder_id = '1i1pWBFOcOFugQ3JNmuxQiBiTk-piyfG_'

results = service.files().list(
    q=f"'{folder_id}' in parents", fields='files(id, name)'
).execute()

# print(results) PRinta os resultados para verificarmos se os arquivos estão corretos na nossa pasta no drive

files = results.get('files', []) # Colocamos uma lista vazia para, caso a pasta não tenha nenhum documento, ele retorna uma lista vazia.

if not files:
    # Reconhece que não há arquivos na pasta do drive
    raise FileNotFoundError('not files in results')
else:
    for file in files:
        requests = service.files().get_media(fileId=file['id']) # Pegamos os arquivos pelo sei id, para garantirmos que será o arquivo certo.
        file_path = f"./curriculos/{file['name']}" # Definimos o caminho para onde os arquivos baixados.
        # VAmos implementar uma lógica para o python baixar o conteúdo dos arquivos do drive e escrever em um arquivo local.
        with open(file_path, 'wb') as file:
            downloader = MediaIoBaseDownload(file, requests)
            done = False
            while not done:
                status, done = downloader.next_chunk() # Juntamos os 'chunks' do arquivo baixados e compilamos no arquivo até acabar.