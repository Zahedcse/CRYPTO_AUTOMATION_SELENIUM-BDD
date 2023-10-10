from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def input_text(self, locator, text: str):
        self.driver.find_element(*locator).send_keys(text)

    def assert_text(self, expected_text: str, locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def assert_partial_text(self, expected_text: str, locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text}, but got {actual_text}"

    def wait_for_element_to_be_clickable(self, *locator, timeout=10):
        element = WebDriverWait(self, timeout).until(
            EC.element_to_be_clickable(*locator)
        )
        element.click()

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_elements_to_be_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_for_element_to_be_present(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements_to_be_present(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located(locator))

    def switch_to_iframe(self, *locator):
        iframe = self.find_element(*locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def scroll_element_into_view(self, *locator):
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def clear_input_field(self, locator):
        self.find_element(*locator).clear()

    def select_dropdown_option_by_text(self, *locator, option_text):
        select = Select(self.find_element(*locator))
        select.select_by_visible_text(option_text)

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    def switch_to_new_tab(self, index=-1):
        # Use index -1 to switch to the most recently opened tab
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[index])

    def hover_over_element(self, *locator):
        element = self.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def perform_double_click(self, *locator):
        element = self.find_element(*locator)
        ActionChains(self.driver).double_click(element).perform()

    def perform_right_click(self, *locator):
        element = self.find_element(*locator)
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element(*source_locator)
        target_element = self.find_element(*target_locator)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def key_down(self, key):
        ActionChains(self.driver).key_down(key).perform()

    def key_up(self, key):
        ActionChains(self.driver).key_up(key).perform()

    def move_to_element(self, *locator):
        element = self.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def move_by_offset(self, x_offset, y_offset):
        ActionChains(self.driver).move_by_offset(x_offset, y_offset).perform()

    def click_and_hold(self, *locator):
        element = self.find_element(*locator)
        ActionChains(self.driver).click_and_hold(element).perform()

    def release(self):
        ActionChains(self.driver).release().perform()
