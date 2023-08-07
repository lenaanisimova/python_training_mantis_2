from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    old_projects = app.project.get_projects_list()
    app.project.add_project(Project(name='Project_name', status='release', view_status='private',
                                    description='Project_description', inherit_global_categories=False))

    old_projects.append(Project)
    new_projects = app.project.get_projects_list()
    assert sorted(old_projects, key=Project.for_sorted_by_name) == sorted(new_projects, key=Project.for_sorted_by_name)