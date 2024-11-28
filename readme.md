Análise de Currículos com IA Utilizando as seguintes tecnologias:
- Python
- LangChain
- TinyDB
- ChatGroq API
- Google Drive API


Passo a passo para rodar o programa:

1 - Autenticar-se ao projeto no google cloud. Rode o script authenticate.py (é necessário estar incluído no projeto com OAuth2 da google)

2 - Baixar os currículos: Por padrão, como temos uma conta de teste, criamos uma pasta no drive para armazenar os currículos desejados.
    Rode o script download-cv.py para que ele possa realizar o download dos arquivos dentro da pasta 'curriculos' usando a API do google drive.

3 - Caso o banco de dados esteja vazio e não populado, execute os scripts create_job.py para criar as vegas desejadas.

4 - Executar o script analise.py para gerar as análises de cada currículo por vaga. Este script costuma demorar para rodar.

5 - Após realizar as etapas acima, executar 'streamlit run app.py' para carregar o frontend e ter a análise dos dados.