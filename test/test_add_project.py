from model.project import Project
from generator.project import testdata


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    old_projects = app.project.get_projects_list()
    #app.project.add_project(Project(name='Project_name', status='release', view_status='private',
                                    #description='Project_description', inherit_global_categories=False))
    project = testdata
    app.project.add_project(project)

    old_projects.append(project)
    new_projects = app.project.get_projects_list()
    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
