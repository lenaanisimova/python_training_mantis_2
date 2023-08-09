from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        client = Client(self.app.config['web']['baseUrl'] + "/api/soap/mantisconnect.php?wsdl")
        projects_list = []
        try:
            projects_list_1 = client.service.mc_projects_get_user_accessible \
                (self.app.config["admin"]["username"], self.app.config["admin"]["password"])
            for item in projects_list_1:
                projects_list.append(Project(name=item['name'], status=item['status']['name'],
                                             view_status=item['view_state']['name'], description=item['description']))
            return projects_list
        except WebFault:
            return None



