Análise de Currículos com IA Utilizando as seguintes tecnologias:
- Python
- LangChain
- TinyDB
- ChatGroq API
- Google Drive API


Passo a passo para rodar o programa:

1 - Criar um projeto no Google Cloud e habilitar a API do Google Drive:
 https://developers.google.com/drive/api/guides/about-sdk?hl=pt-br

2 - Autenticar-se ao projeto no Google Cloud. Baixe suas credenciais OAuth2 da API do Google Drive e renomeie o arquivo baixado para 'credentials.json'. Após isto rode o script authenticate.py (é necessário estar incluído no projeto com OAuth2 da google)

3 - Baixar os currículos: Por padrão, como temos uma conta de teste, criamos uma pasta no drive para armazenar os currículos desejados.
    Copie o ID da pasta desejada no Google Drive e cole na variável folder_id no arquivo download-cv.py.

    Rode o script download-cv.py para que ele possa realizar o download dos arquivos dentro da pasta 'curriculos' usando a API do Google Drive.

3 - Caso o banco de dados esteja vazio e não populado, execute os scripts create_job.py para criar as vegas desejadas.
    No arquivo create_job, você define os requisitos da vaga, como pré requisitos, diferenciais, etc...

4 - Criar uma conta no site da groq (https://console.groq.com/playground) e criar uma API key

5 - Criar um arquivo .env na raiz do projeto com uma variável chamada GROQ_API_KEY e inserir sua API key gerada no arquivo.
        Exemplo da estrutura do arquivo: GROQ_API_KEY='sua api key'

6 - Executar o script analise.py para gerar as análises de cada currículo por vaga. Este script costuma demorar para rodar.

7 - Após realizar as etapas acima, executar 'streamlit run app.py' para carregar o frontend e ter a análise dos dados.

OBS: As dependências usadas no projeto estão no arquivo pyproject.toml
