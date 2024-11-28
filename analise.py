from helper import extract_data_analysis, get_pdf_paths, read_pdf
from database import AnalyseDatabase
from ai import GroqClient
from models.resum import Resum
from models.file import File
import uuid

database = AnalyseDatabase()
ai = GroqClient()
job = database.get_job_by_name('Vaga de Cientista de Dados')

cv_paths = get_pdf_paths(dir='curriculos')

for path in cv_paths:
    content = read_pdf(path)
    resum = ai.resume_cv(content)
    opinion = ai.generate_opinion(content, job)
    score = ai.generate_score(content, job)

    resum_schema = Resum(
        id=str(uuid.uuid4()),
        job_id=job.get('id'),
        content=resum,
        file=str(path),
        opinion=opinion
    )

    file_schema = File(
        file_id=str(uuid.uuid4()),
        job_id=job.get('id'),
    )

    analysis = extract_data_analysis(resum, resum_schema.job_id, resum_schema.id, score)

    # Insere os modelos no nosso banco de dados.
    database.resums.insert(resum_schema.model_dump())
    database.analysis.insert(analysis.model_dump())
    database.files.insert(file_schema.model_dump())