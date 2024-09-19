from patent_client import Inpadoc, Assignment, USApplication

def find_patent_by_id(patent_id: str):
    app = USApplication.objects.get(patent_id)
    return app

    