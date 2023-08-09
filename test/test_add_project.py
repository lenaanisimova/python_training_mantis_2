from model.project import Project
from generator.project import testdata


def test_add_project(app):
    app.project.open_projects_page()
    #old_projects = app.project.get_projects_list()
    old_projects = app.soap.get_projects_list()
    project = testdata
    app.project.add_project(project)

    old_projects.append(project)
    #new_projects = app.project.get_projects_list()
    new_projects = app.soap.get_projects_list()
    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
