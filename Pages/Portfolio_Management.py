import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.Base import Page


class PortfolioManagement(Page):
    Portfolio_Management = (By.XPATH, "(//li[@role='menuitem'])[3]")
    portfolio_list = (By.XPATH, "//div[@class='grid grid-cols-12 md:gap-8 gap-y-8' ]/div")

    All_Portfolio_Id = (By.XPATH, "//div[@class='text-[12px] font-thin text-white']")
    Total_PnL = (By.CSS_SELECTOR,
                 "div#__next div.p-8.rounded-md.cursor-pointer.bg-sidebar > div.block.mb-6 > div.text-xl.font-medium")
    Portfolio_valuation = (By.CSS_SELECTOR,
                           "div#__next div.p-9.mb-6.rounded-md.cursor-pointer.bg-sidebar > div.block.mb-6 > div.text-xl.font-medium")
    All_Value = (By.XPATH, "//tr/td[position()=9]")
    All_PnL_Value = (By.XPATH, "//tr/td[position()=10]")
    Next_Page_Button = (By.CSS_SELECTOR, "li.ant-pagination-next")
    Previous_Page = (By.XPATH, "//div[normalize-space()='1']")
    valuation_amount = (By.XPATH, "(//div[@class='mt-8 text-[28px] font-medium'])[1]")
    Valuation_amount_tooltip = (By.XPATH, "(//div[@role='tooltip'])[1]")
    Total_PnL_text = (By.XPATH, "(//div[@class='mt-8 text-[28px] font-medium'])[2]")
    Total_PnL_tooltip = (By.XPATH, "(//div[@role='tooltip'])[2]")
    Portfolio_management_Tab = (By.XPATH, "(//li[@role='menuitem'])[3]")
    # Portfolio_Management = (By.XPATH, "//ol/li/span[text()='Portfolio Management']")
    Portfolio_Id = (By.XPATH, "//div[@class='text-[12px] font-thin text-white']")
    Total_PV = (By.XPATH, "//div/div[@class='text-sm text-primary']")
    # Portfolio_valuation = (By.XPATH, "//div[text()='Portfolio Valuation']")
    Portfolio = (By.XPATH, "//span[text()='Portfolio']")

    """"Portfolio Management Table"""
    table_headings = (By.XPATH, "//thead/tr/th")

    """"Asset swap Transfer"""
    Asset_transfer = (By.XPATH, "//span[normalize-space()='Asset Transfer']")
    Asset_transfer_form = (By.XPATH, "//span[text()='Asset Swap Form']")
    From_venue = (By.XPATH, "(//input[@type='search'])[2]")
    Venue_options = (By.XPATH, "//div[@class='rc-virtual-list-holder-inner']")
    From_account = (By.XPATH, "//input[@id='fromPortfolioId']")
    Form_asset_input = (By.XPATH, "(//input[@type='search'])[3]")
    From_asset_options = (By.XPATH, "//div[@class='ant-select-item ant-select-item-option']")
    From_quantity = (By.CSS_SELECTOR, "#fromQuantity")
    From_reason = (By.CSS_SELECTOR, "#reason")
    To_venue = (By.XPATH, "(//input[@type='search'])[4]")
    Counter_party = (By.ID, "toClientId")
    To_account = (By.ID, "toPortfolioId")
    To_Asset = (By.XPATH, "(//input[@type='search'])[5]")
    To_quantity = (By.ID, "toQuantity")
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

    def click_portfolio(self, portfolio):
        all_portfolio_Id = self.find_elements(self.All_Portfolio_Id)
        for Id in all_portfolio_Id:
            if Id.text == portfolio:
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
        self.hover_over_element(self.valuation_amount)
        time.sleep(2)
        tooltip_element = self.find_element(self.Valuation_amount_tooltip)
        portfolio_valuation = tooltip_element.text
        print(portfolio_valuation)
        portfolio_summation = self.calculate_summation(num_pages, self.All_Value)
        self.verify_summation(portfolio_valuation, portfolio_summation)

        # portfolio_valuation = self.find_element(self.Valuation_amount).text
        # portfolio_summation = self.calculate_summation(num_pages, self.All_Value)
        # self.verify_summation(portfolio_valuation, portfolio_summation)

    def click_on_first_Page(self):
        self.click(self.Previous_Page)

    def verify_TotalPnL_summation(self, num_pages=2):
        self.hover_over_element(self.Total_PnL_text)
        time.sleep(2)
        tooltip_element = self.find_element(self.Total_PnL_tooltip)
        portfolio_PnL = tooltip_element.text
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
        assert expected_headers == actual_headers, f"expected headers {expected_headers} but got {actual_headers}"

    def click_asset_transfer(self):
        self.wait_for_element_to_be_present(self.Asset_transfer)
        self.click(self.Asset_transfer)

    def fill_swap_fields(self):
        self.click(self.From_venue)
        time.sleep(2)
        self.input_text(self.From_venue, "Portfolio")
        self.find_element(self.From_venue).send_keys(Keys.ENTER)
        # options = self.find_elements(self.Venue_options)
        # for option in options:
        #     if option.text == 'Portfolio':
        #         option.click()
        #         break
        self.input_text(self.From_account, "MPS001")
        self.click(self.Form_asset_input)
        time.sleep(2)
        self.input_text(self.Form_asset_input, "Bitcoin")
        self.find_element(self.Form_asset_input).send_keys(Keys.ENTER)
        self.input_text(self.From_quantity, '100')

    def fill_To_fields(self):
        self.click(self.To_venue)
        time.sleep(2)
        self.input_text(self.To_venue, 'Portfolio')
        self.find_element(self.To_venue).send_keys(Keys.ENTER)
        self.input_text(self.Counter_party, "MPSNN")
        self.input_text(self.To_account, "MPS017")
        self.click(self.To_Asset)
        time.sleep(2)
        self.input_text(self.To_Asset, 'Ethereum')
        self.find_element(self.To_Asset).send_keys(Keys.ENTER)
        self.input_text(self.To_quantity, '10')
        self.click(self.Initiate_Transfer)
        time.sleep(2)







