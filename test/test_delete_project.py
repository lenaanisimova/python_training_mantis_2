#Задание 26
from model.project import Project
from generator.project import testdata
import random

def test_delete_project(app):
    app.project.open_projects_page()
    # выбираем проект для удаления
    if len(app.project.get_projects_list()) == 0:
        project = testdata
        app.project.add_project(project)

    old_projects = app.soap.get_projects_list()
    #projects = app.project.get_projects_list()
    proj = random.choice(old_projects)


    app.project.delete_project(proj)
    old_projects.remove(proj)

    #new_projects = app.project.get_projects_list()
    new_projects = app.soap.get_projects_list()

    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)