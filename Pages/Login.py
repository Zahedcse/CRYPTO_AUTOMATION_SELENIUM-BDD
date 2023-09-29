from selenium.webdriver.common.by import By
from Pages.Base import Page


class Login(Page):
    Email_field = (By.CSS_SELECTOR, '.moops-input [id="identifier"]')
    Password_field = (By.XPATH, "//input[@name='password']")
    Checkbox = (By.CSS_SELECTOR, '.ant-checkbox-input')
    Click_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    def input_email(self, email):
        self.input_text(self.Email_field, email)

    def input_password(self, password):
        self.input_text(self.Password_field, password)

    def click_checkbox(self):
        self.click(self.Checkbox)

    def click_submit(self):
        self.click(self.Click_button)

