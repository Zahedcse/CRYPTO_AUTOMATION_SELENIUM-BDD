import time
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from App.Application import Application


def browser_init(context):
    context.driver = webdriver.Chrome()
    ''' MOBILE EMULATION'''
    # mobile_emulation = {"deviceName": "iPad Air"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(options=chrome_options)
    # driver_path = GeckoDriverManager().install()  # Use GeckoDriverManager for Firefox
    # context.driver = webdriver.Firefox(executable_path=driver_path)  # Use Firefox WebDriver here
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


"""it will be called for all the feature which will have @login_required"""


def login(context, username, password):
    context.driver.get('https://moops-dev.tulip-tech.com/login')
    username_field = context.driver.find_element(By.CSS_SELECTOR, '.moops-input [id="identifier"]')
    password_field = context.driver.find_element(By.XPATH, "//input[@name='password']")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(3)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    if 'login_required' in scenario.tags:
        login(context, 'admin@moops.com', 'Admin@123')


def after_scenario(context, scenario):
    # context.driver.delete_all_cookies()
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)