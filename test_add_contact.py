# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/edit.php")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Ivan")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Vasilyevich")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Ryurikovich")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("Grozny")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Tsar")
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("Russia")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Palaty")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
