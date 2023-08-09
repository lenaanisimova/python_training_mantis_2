#Задание 26
from model.project import Project
from selenium.webdriver.support.ui import Select

class ProjectHelper:
    def __init__(self, app):
        self.app = app
# открыть страницу где можно создать новый проект, видеть созданные и удалять\редактировать
    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
    def add_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # заполнить Project Name
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        # заполнить Description
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        # кликаем по чек-боксу, если он отличается от требуемого
        if not project.inherit_global_categories:
            wd.find_element_by_name("inherit_global").click()
        # Выбираем в выпадающих списках то что требуется
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_status)
        wd.find_element_by_css_selector("input.button").click()
    def get_projects_list(self):
        wd = self.app.wd
        self.open_projects_page()
        table = wd.find_elements_by_tag_name("table")[2]
        row1 = table.find_elements_by_class_name("row-1")
        row2 = table.find_elements_by_class_name("row-2")
        project_list = []
        for element in row1:
            name = element.find_elements_by_tag_name("td")[0].text
            status = element.find_elements_by_tag_name("td")[1].text
            view_status = element.find_elements_by_tag_name("td")[3].text
            description = element.find_elements_by_tag_name("td")[4].text
            project_list.append(Project(name=name, status=status, view_status=view_status, description=description))
        for element in row2:
            name = element.find_elements_by_tag_name("td")[0].text
            status = element.find_elements_by_tag_name("td")[1].text
            view_status = element.find_elements_by_tag_name("td")[3].text
            description = element.find_elements_by_tag_name("td")[4].text
            project_list.append(Project(name=name, status=status, view_status=view_status, description=description))
       # return list(project_list)
        return project_list
    def delete_project(self, proj):
        wd = self.app.wd
        self.open_project_page(proj.name)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
    def open_project_page(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath(f"//a[text() = '{name}']").click()