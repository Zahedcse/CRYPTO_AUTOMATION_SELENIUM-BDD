import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.Base import Page


class TradeProcessing(Page):
    Trade_Processing_Tab = (By.XPATH, "(//li[@role='menuitem'])[4]")

    """Trade processing Table"""
    Trade_processing = (By.XPATH, "//ol /li /span[text()='Trades Processing']")
    All_tabs = (By.XPATH, "//div/label[contains(@class,'ant-radio-button')]")
    All_trade = (By.XPATH, "//span[text()='All Trade']")
    Exchange = (By.XPATH, "//span[text()='Exchange']")
    Otc = (By.XPATH, "//span[text()='OTC']")
    allvenue = (By.XPATH,
                "(//div[@class='ant-select-dropdown bg-sidebar rounded-sm moops-dropdown-style css-2dphzb ant-select-dropdown-placement-bottomLeft'])[1]/div")

    Table_headings = (By.XPATH, "//thead/tr/th")
    """New Trade Button"""
    Add_new_trade_button = (By.XPATH, "//span[@class='!flex items-center gap-x-2']")
    Asset_name_field = (By.XPATH, "(//div[@class ='ant-select-selector'])[1]")
    asset_1 = (By.XPATH, "//div[contains(@title, 'Bitcoin')]")
    asset_2 = (By.XPATH, "//div[contains(@title, 'Ethereum')]")
    asset_3 = (By.XPATH, "//div[contains(@title, 'BNB')]")
    asset_4 = (By.XPATH, "//div[contains(@title, 'Wrapped Bitcoin')]")
    Portfolio_id = (By.CSS_SELECTOR, "#portfolioId")
    Venue = (By.XPATH, "(//div[@class ='ant-select-selector'])[2]")
    Venue_portfolio_Exchange = (By.XPATH, "//div[@title = 'Exchange']")
    Venue_portfolio_OTC = (By.XPATH, "//div[@title = 'OTC']")
    Instrument_type = (By.XPATH, "(//div[@class ='ant-select-selector'])[3]")
    Instrument_type_list = (By.XPATH, "(//div[@class='rc-virtual-list-holder']//div)[2]")
    Instrument_value_Spot = (By.XPATH, "//div[@title = 'Spot']")
    Instrument_value_Future = (By.XPATH, "//div[@title = 'Future']")
    Instrument_value_Perpetuals = (By.XPATH, "//div[@title = 'Perpetuals']")
    Instrument_value_Options = (By.XPATH, "//div[@title = 'Options']")
    Position = (By.XPATH, "(//div[@class ='ant-select-selector'])[4]")
    Position_value = (By.XPATH, "//div[@title = 'Buy']")
    Quantity = (By.CSS_SELECTOR, "#quantity")
    Price = (By.CSS_SELECTOR, "#price")
    Initiate_trade_button = (By.XPATH, "//div/button/span[.='Initiate Trade']")
    Notification = (By.CSS_SELECTOR, 'div > div.ant-notification-notice-description')
    error_message = (By.CSS_SELECTOR, "div[class='text-[11px] right-0 bottom-50 h-4 mt-1 mb-2 text-red-500']")
    # Current_value_usd = (By.XPATH, "//th[text()='Current Value (USD)']")
    # Action = (By.XPATH, "//th[text()='Action']")
    All_trade_tab = (By.XPATH, "//label/span[.='All Trade']")

    """Got 10 checkboxes"""
    Check_box = (By.XPATH, "(//label/span/input[@type = 'checkbox'])[2]")
    edit_button = (By.XPATH, "(//td/div/div)[1]")
    input_fields = (By.TAG_NAME, 'input')

    """Edit Trade Form"""
    Edit_trade = (By.XPATH, "//div[@class='ant-modal-title']")
    E_Asset_name = (By.XPATH, "//span[@title='Bitcoin-(BTC)']")
    E_Client_id = (By.XPATH, "//input[@id='clientId']")
    E_Portfolio_id = (By.CSS_SELECTOR, "#portfolioId")
    E_Portfolio_name = (By.XPATH, "//input[@id='toName']")
    E_Venue = (By.XPATH, "//span[@title='OTC']")
    # E_Instrument_type =
    E_Position = (By.XPATH, "//span[@title='Sell']")
    E_Quantity = (By.XPATH, "//input[@id='quantity']")
    E_Price = (By.XPATH, "//input[@id='price']")
    E_Update_trade = (By.XPATH, "//span[text()='Update Trade']")

    Confirm_button = (By.XPATH, "(//div/button/span)[2]")

    """Validate trade current Value things"""
    Asset_quantity = (By.XPATH, "//tbody/tr[1]/td[9]")
    Asset_Price = (By.XPATH, "//tbody/tr[1]/td[10]")
    Current_Trade_value = (By.XPATH, "//tbody/tr[1]/td[11]")

    """Portfolio pnl and % Calc"""
    Available_asset_value = (By.XPATH, "//tbody/tr[1]/td[9]")
    ActualPnLPercentage = (By.XPATH, "//tbody/tr[1]/td[11]")
    ActualPnL = (By.XPATH, "//tbody/tr[1]/td[10]")
    Actual_Quantity = (By.XPATH, "//tbody/tr[1]/td[4]")

    def click_on_Trade_processing_tab(self):
        self.click(self.Trade_Processing_Tab)

    def get_all_tabs(self):
        tabs = self.find_elements(self.All_tabs)
        expected_tabs = ['All Trade', 'Exchange', 'OTC']
        actual_tabs = []
        print(expected_tabs)
        for tab in tabs:
            element = tab.text
            actual_tabs.append(element)
        print(actual_tabs)
        if actual_tabs == expected_tabs:
            print("Tabs name matches the expected list")
        else:
            print("Tabs name not matches with the expected list")

    def click_on_tab(self):
        tabs = self.find_elements(self.All_tabs)
        for tab in tabs:
            if tab.text == "Exchange":
                tab.click()
                print("Exchange tab clicked")
            if tab.text == "OTC":
                tab.click()
                print("OTC tab Clicked")
            if tab.text == "OTC":
                tab.click()
                print("OTC tab Clicked")

    def table_header_list(self):
        headers = self.find_elements(self.Table_headings)
        actual_headers = []
        expected_column_headers = ["", "Assets", "Client ID", "Portfolio ID", "Portfolio Name", "Venue", "Instrument",
                                   "Position", "Quantity", "Price", "Current Value (USD)", "Action"]
        print(expected_column_headers)
        for header in headers:
            element = header.text
            actual_headers.append(element)
        print(actual_headers)
        if actual_headers == expected_column_headers:
            print("Column headers matches the expected column headers.")
        else:
            print("Column headers do not match the expected headers.")

    def click_on_new_trade_button(self):
        self.click(self.Add_new_trade_button)

    def click_on_asset_name_filed(self):
        self.click(self.Asset_name_field)

    def select_asset_BTC(self):
        self.click(self.asset_1)

    def select_asset_ETH(self):
        self.click(self.asset_2)

    def select_asset_BNB(self):
        self.click(self.asset_3)

    def select_asset_WBC(self):
        self.click(self.asset_4)

    def enter_portfolio_ID(self, PortfolioID):
        self.input_text(self.Portfolio_id, PortfolioID)

    def click_on_venue_field(self):
        self.click(self.Venue)
        time.sleep(2)

    # def select_venue(self):
    #     venue_locator = self.allvenue
    #     wait = WebDriverWait(self.driver, 10)
    #     elements = wait.until(EC.presence_of_all_elements_located(venue_locator))
    #     for element in elements:
    #         print(element.text)
    #         if element.text == 'Exchange':
    #             element.click()

    def select_venue_Exchange(self):
        self.click(self.Venue_portfolio_Exchange)

    #
    # def select_venue_OTC(self):
    #     self.click(self.Venue_portfolio_OTC)

    def click_on_instrument_type_field(self):
        self.click(self.Instrument_type)

    def select_instrument_type_Spot(self):
        self.click(self.Instrument_value_Spot)

    def select_instrument_type_Future(self):
        self.click(self.Instrument_value_Future)

    def select_instrument_type_Perpetuals(self):
        self.click(self.Instrument_value_Perpetuals)

    def select_instrument_type_Options(self):
        self.click(self.Instrument_value_Options)

    def click_on_position_filed(self):
        self.click(self.Position)

    def select_position_value(self):
        self.click(self.Position_value)

    def enter_Quantity(self, Quantity):
        self.input_text(self.Quantity, Quantity)

    def enter_price(self, price):
        self.input_text(self.Price, price)

    def Click_on_initiate_button(self):
        self.click(self.Initiate_trade_button)

    def verify_success_message(self, text):
        element = self.find_element(self.Notification)
        actual_text = element.text.strip()
        assert actual_text == text, f"Expected '{text}' but got '{actual_text}'"

    def verify_error_message(self, message):
        element = self.find_element(self.error_message)
        actual_text = element.text.strip()
        assert actual_text == message, f"Expected '{message}' but got '{actual_text}'"

    def assert_quantity_price_trade(self):
        quantity_element = self.find_element(self.Asset_quantity)
        price_element = self.find_element(self.Asset_Price)
        trade_element = self.find_element(self.Current_Trade_value)
        quantity = float(''.join(filter(str.isdigit, quantity_element.text)))
        price = float(''.join(filter(str.isdigit, price_element.text)))
        trade_value = float(''.join(filter(str.isdigit, trade_element.text)))

        expected_result = quantity * price
        print(f"Expected Price: {expected_result}")
        print(f"Actual Trade Price: {trade_value}")
        assert expected_result == trade_value, f"Expected {expected_result} but got {trade_value}"

    def click_on_all_trade_tab(self):
        self.click(self.All_trade_tab)

    def click_on_check_box(self):
        self.click(self.Check_box)

    def click_on_edit_trade(self):
        self.click(self.edit_button)

    def clear_all_input_fields(self):
        # Find all input elements on the page
        input_elements = self.input_fields
        for input_element in input_elements:
            input_element.clear()

    def edit_trade(self):
        self.click(self.E_Portfolio_id)
        self.input_text(self.E_Portfolio_id, "MPS001")
        self.input_text(self.E_Quantity, "50")
        self.input_text(self.E_Price, "23000")
        self.click(self.E_Update_trade)

    def click_on_confirm_button(self):
        self.click(self.Confirm_button)

    def validate_PnL_and_percentage(self):
        Buying_Price = 26086.176666666666
        print(f"Buying price: {Buying_Price}")
        Quan = self.find_element(self.Actual_Quantity)
        quantity = int(''.join(filter(str.isdigit, Quan.text)))
        element = self.find_element(self.Available_asset_value).text
        available_asset_value = float(element.replace(',', ''))
        print(f"Available asset value: {available_asset_value}")
        pnl_result = round(available_asset_value - (Buying_Price * quantity), 2)
        print(f"pnl_result = {pnl_result}")
        pnl_percentage_result = round((pnl_result / (Buying_Price * quantity)) * 100, 2)
        print(f"pnl_percentage_result = {pnl_percentage_result}")

        element1 = self.find_element(self.ActualPnL).text
        Actual_pnl = float(element1.replace(',', ''))
        Actual_pnl_percentage = self.find_element(self.ActualPnLPercentage).text
        print(Actual_pnl_percentage)
        assert pnl_result == Actual_pnl, f"Expected PNL = {pnl_result} but got {Actual_pnl}"
        assert pnl_percentage_result == float(
            Actual_pnl_percentage), f"Expected PNL = {pnl_percentage_result} but got {Actual_pnl_percentage}"
