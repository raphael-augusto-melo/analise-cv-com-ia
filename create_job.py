import uuid
from models.job import Job
from database import AnalyseDatabase

database = AnalyseDatabase() # Inicializa o banco de dados, criando o arquivo db.json.


name = 'Vaga de Cientista de Dados'

activities = '''
Atualizar e monitorar dashboards de custos internos diariamente
Limpeza, estruturação e análise de dados para apoiar a tomada de decisões
Trabalhar em colaboração com áreas de negócio para implementar soluções de Ciência de Dados que apoiem a tomada de decisão baseada em dados
Desenvolver painéis de acompanhamento de demandas
Colaborar com soluções inovadoras, especialmente utilizando Inteligência Artificial
Identificar, criar, automatizar e manter modelos de Machine Learning
Extrair insights através de diversas metodologias (clusterização, previsão de demanda, etc)
Realizar análises para identificação de oportunidades e/ou problemas
'''

prerequisites = '''
Experiência com construção de dashboards (Power BI, Looker Studio)
Graduação em Análise e Desenvolvimento de Sistemas, Tecnologia da Informação, Publicidade, Ciência da Computação ou áreas correlatas
Conhecimento em IA generativa
Habilidade em programação em Python e suas bibliotecas para análise de dados e aprendizado de máquina
Pensamento crítico, Curiosidade e entendimentos de regras de negócio
Excel e/ou Google Sheets em nível intermediário (tabelas dinâmicas, formatação condicional)
Conhecimento em redes neurais e Deep Learning e programação LLM
Experiência em Cloud Computing (AWS)
Versionamento: Familiaridade em versionamento de código (Git)
Manipulação de dados: interação com bancos de dados, Delta Lake e manipulação de dados usando a linguagem SQL
'''

differentials = '''
Cursos ou pós-graduação / mestrado na Área de Ciência de Dados
Conhecimento em NLP / LLM
Conhecimento básico em ETL para gerenciamento de dados
Experiência em desenvolvimento de soluções utilizando GPTs e outras ferramentas de IA
Familiaridade com BERT
Conhecimento em IA generativa
'''

job = Job(
    id=str(uuid.uuid4()),
    name=name,
    main_activities=activities,
    prerequisites=prerequisites,
    differentials=differentials
)

database.jobs.insert(job.model_dump()) # O model_dump nos retorna a estrutura da classe informada em forma de dicionário e insere no banco de dados.
