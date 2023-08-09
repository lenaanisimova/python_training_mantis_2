#Задание 26
class Project:
    def __init__(self, name=None, status=None, inherit_global_categories=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.inherit_global_categories = inherit_global_categories
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.name, self.status, self.view_status, self.description)
    def __eq__(self, other):
        return self.name == other.name and self.status == other.status and self.view_status == other.view_status\
               and self.description == other.description

    def name(self):
        return self.name