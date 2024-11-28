from tinydb import TinyDB, Query

class AnalyseDatabase(TinyDB):
    # Definimos as tabelas do banco de dados. Os atributos das tabelas estão definidos na pasta 'models'.
    def __init__(self, db_path='db.json'):
        super().__init__(db_path)
        self.jobs = self.table('jobs')
        self.resums = self.table('resums')
        self.analysis = self.table('analysis')
        self.files = self.table('files')

    # A partir daqui, vamos definir as querys para criar, deletar e inserir dados.
    def get_job_by_name(self, name):
        job = Query()
        result = self.jobs.search(job.name == name)
        return result[0] if result else None # A resposta desta query é uma lista, mas queremos somente o primeiro elemento que corresponde à query.

    def get_resum_by_id(self, id):
        resum = Query()
        result = self.resums.search(resum.id == id)
        return result[0] if result else None
    
    def get_analysis_by_job_id(self, job_id):
        analysis = Query()
        result = self.analysis.search(analysis.job_id == job_id)
        return result
    
    def get_resums_by_job_id(self, job_id):
        resum = Query()
        result = self.resums.search(resum.job_id == job_id)
        return result
    
    def delete_all_resums_by_job_id(self, job_id):
        resum = Query()
        self.resums.remove(resum.job_id == job_id)
    
    def delete_all_analysis_by_job_id(self, job_id):
        analysis = Query()
        self.analysis.remove(analysis.job_id == job_id)
    
    def delete_all_files_by_job_id(self, job_id):
        file = Query()
        self.files.remove(file.job_id == job_id)