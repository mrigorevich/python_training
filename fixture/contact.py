class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_edit_page(self):
        # open edit page
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        # fill contact form
        wd = self.app.wd
        self.open_edit_page()
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()

    def delete_first(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first(self, edited_contact):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(edited_contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
