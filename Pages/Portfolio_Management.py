import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.Base import Page


class PortfolioManagement(Page):
    Portfolio_Management = (By.XPATH, "(//li[@role='menuitem'])[3]")
    portfolio_list = (By.XPATH, "//div[@class='grid grid-cols-12 md:gap-8 gap-y-8' ]/div")
    portfolio_1 = (By.XPATH, "//div[@id='fund_card_0']")
    All_Portfolio_Id = (By.XPATH, "//div[@class='text-[12px] font-thin text-white']")
    Total_PnL = (By.CSS_SELECTOR,
                 "div#__next div.p-8.rounded-md.cursor-pointer.bg-sidebar > div.block.mb-6 > div.text-xl.font-medium")
    Portfolio_valuation = (By.CSS_SELECTOR,
                           "div#__next div.p-9.mb-6.rounded-md.cursor-pointer.bg-sidebar > div.block.mb-6 > div.text-xl.font-medium")
    All_Value = (By.XPATH, "//tr/td[position()=9]")
    All_PnL_Value = (By.XPATH, "//tr/td[position()=10]")
    Next_Page_Button = (By.CSS_SELECTOR, "li.ant-pagination-next")
    Previous_Page = (By.XPATH, "//div[normalize-space()='1']")
    Valuation_amount = (By.XPATH, "//span[@class='text-base font-medium']")
    Total_PnL_text = (By.XPATH, "(//div[@class='mt-8 text-[28px] font-medium'])[2]")
    Total_PnL_tooltip = (By.XPATH, "(//div[@role='tooltip'])[2]")
    # Portfolio = (By.XPATH, "//span[text()='Portfolio']")

    Portfolio_management_Tab = (By.XPATH, "(//li[@role='menuitem'])[3]")
    # Portfolio_Management = (By.XPATH, "//ol/li/span[text()='Portfolio Management']")
    Portfolio_Id = (By.XPATH, "//div[@class='text-[12px] font-thin text-white']")
    Total_PV = (By.XPATH, "//div/div[@class='text-sm text-primary']")
    # Portfolio_valuation = (By.XPATH, "//div[text()='Portfolio Valuation']")
    Portfolio = (By.XPATH, "//span[text()='Portfolio']")

    """"Portfolio Management Table"""
    table_headings = (By.XPATH, "//thead/tr/th")

    portfolio_Id = (By.XPATH, "//th[text()='Portfolio ID']")
    Assets = (By.XPATH, "//th[text()='Assets']")
    Instrument = (By.XPATH, "//th[text()='Instrument']")
    Quantity = (By.XPATH, "//th[text()='Quantity']")
    Value_USD = (By.ID, "//th[text()='Value (USD)']")
    Locked_assets = (By.XPATH, "//th[text()='Locked Assets']")
    Locked_value = (By.XPATH, "//th[text()='Locked Value (USD)']")
    Available_asset = (By.XPATH, "//th[text()='Available Assets']")
    Available_asset_value = (By.XPATH, "//th[text()='Available Assets Value (USD)']")
    P_L = (By.XPATH, "//th[text()='P&L (USD)']")
    Percent_of_P_L = (By.XPATH, "//th[text()='P&L (%)']")

    """"Asset swap Transfer"""
    Asset_transfer = (By.XPATH, "//span[text()='Asset Transfer']")
    Asset_transfer_form = (By.XPATH, "//span[text()='Asset Swap Form']")
    From_venue = (By.XPATH, "//input[@id='rc_select_1']")
    Venue_options = (By.CSS_SELECTOR, ".ant-select-item-option-content")
    From_account = (By.XPATH, "//input[@id='fromPortfolioId']")
    Form_asset_input = (By.CSS_SELECTOR, "#rc_select_1")
    From_asset_options = (By.XPATH, "//div[@class='ant-select-item ant-select-item-option']")
    From_quantity = (By.CSS_SELECTOR, "#fromQuantity")
    From_reason = (By.CSS_SELECTOR, "#reason")
    To_venue = (By.CSS_SELECTOR, "#rc_select_3")
    Counter_party = (By.CSS_SELECTOR, "#clientId")
    To_account = (By.CSS_SELECTOR, "#toPortfolioId")
    To_quantity = (By.CSS_SELECTOR, "#toQuantity")
    Initiate_Transfer = (By.XPATH, "//button[@type='submit']")

    """"All other transfer form"""
    Venue = (By.ID, "rc_select_5")
    All_other_Venue_options = (By.CSS_SELECTOR, ".ant-select-item-option-content")
    All_other_account = (By.XPATH, "//input[@id='fromPortfolioId']")
    All_other_quantity = (By.CSS_SELECTOR, "#quantity")
    All_other_reason = (By.CSS_SELECTOR, "#reason")
    Button = (By.XPATH, "//span[text()='Initiate Transfer']")

    def click_portfolio_management(self):
        self.click(self.Portfolio_management_Tab)

    def click_portfolio(self):
        all_portfolio_Id = self.find_elements(self.All_Portfolio_Id)
        for Id in all_portfolio_Id:
            if Id.text == "MPS001":
                Id.click()
                break

    def calculate_summation(self, num_pages, element_locator):
        summation = 0
        current_page = 1
        try:
            while current_page <= num_pages:
                all_value_data = self.find_elements(element_locator)
                for element in all_value_data:
                    value = element.text
                    value_without_commas = value.replace(',', '')
                    summation += float(value_without_commas)
                try:
                    next_button = self.find_element(self.Next_Page_Button)
                    if next_button.is_enabled():
                        next_button.click()
                        current_page += 1
                    else:
                        break
                except NoSuchElementException:
                    break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        return summation

    def verify_valuation_summation(self, num_pages=2):
        portfolio_valuation = self.find_element(self.Valuation_amount).text
        portfolio_summation = self.calculate_summation(num_pages, self.All_Value)
        self.verify_summation(portfolio_valuation, portfolio_summation)

    def click_on_first_Page(self):
        self.click(self.Previous_Page)

    def verify_TotalPnL_summation(self, num_pages=2):
        self.hover_over_element(self.Total_PnL_text)
        time.sleep(2)
        tooltip_element = self.find_element(self.Total_PnL_tooltip)
        portfolio_PnL = tooltip_element.text
        # locator_value = self.find_element(self.Total_PnL_Amount).text
        # numeric_value = float("".join(filter(str.isdigit, locator_value)))
        # portfolio_PnL = numeric_value * 1000000
        print(portfolio_PnL)
        PnL_summation = self.calculate_summation(num_pages, self.All_PnL_Value)
        self.verify_summation(portfolio_PnL, PnL_summation)

    def verify_summation(self, expected_value, calculated_sum):
        print(f"Total summation: {calculated_sum}")
        cleaned_expected = expected_value.replace(',', '')
        print(cleaned_expected)
        assert float(
            cleaned_expected).__floor__() == calculated_sum.__floor__(), f"Expected {cleaned_expected} but got {calculated_sum}"

    def verify_valuation_text(self):
        self.assert_text("Portfolio Valuation", self.Portfolio_valuation)

    def verify_total_pnl(self):
        self.assert_text("Total P&L", self.Total_PnL)

    def verify_asset_table_headings(self):
        headers = self.find_elements(self.table_headings)
        actual_headers = []
        expected_headers = ["Portfolio ID", "Assets", "Instrument", "Quantity", "Value (USD)", "Locked Assets",
                            "Locked Value (USD)",
                            "Available Assets", "Available Assets Value (USD)", "P&L (USD)", "P&L (%)"]
        print(expected_headers)
        for header in headers:
            element = header.text
            actual_headers.append(element)
        print(actual_headers)

        if actual_headers == expected_headers:
            print("Actual Column headers matches the expected column headers.")
        else:
            print("Actual Column headers do not match the expected headers.")
        assert expected_headers == actual_headers
