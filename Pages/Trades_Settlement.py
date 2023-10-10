from selenium.webdriver.common.by import By

from Pages.Base import Page


class TradeSettlement(Page):
    Home = (By.XPATH, "//a[@href='/app']")
    Trades_settlement = (By.XPATH, "//li/span[text()='Trades Settlement']")
    Asset_Transfer = (By.XPATH, "//li/span[text()='Asset Transfer']")

    Asset_transfer = (By.XPATH, "//span[@class='ant-radio-button ant-radio-button-checked']")
    Asset_swap_settlement = (By.XPATH, "//span[@class='ant-radio-button ant-radio-button-checked']")
    Fiat_settlement = (By.XPATH, "//span[@class='ant-radio-button ant-radio-button-checked']")

    Search = (By.XPATH, "(//input[@class='ant-input css-2dphzb'])[2]")

    Drop_down = (By.XPATH, "//input[@id='rc_select_86']")
    Filter_by_status_all = (By.XPATH, "//span[@class='ant-select-selection-item']")
    Filter_by_status_pending = (By.XPATH, "//span[@class='ant-select-selection-item']")
    Filter_by_status_executed = (By.XPATH, "//span[@class='ant-select-selection-item']")
    Filter_by_status_rejected = (By.XPATH, "//span[@class='ant-select-selection-item']")

    Asset = (By.XPATH, "//th[text()='Asset']")
    Quantity = (By.XPATH, "//th[text()='Quantity']")
    Current_value_usd = (By.XPATH, "//th[text()='Current Value (USD)']")
    From_venue = (By.XPATH, "//th[text()='From Venue']")
    From_account_wallet = (By.XPATH, "//th[text()='From Account/Wallet']")
    From_account_name = (By.XPATH, "//th[text()='From Account Name']")
    To_venue = (By.XPATH, "//th[text()='To Venue']")
    To_account_wallet = (By.XPATH, "//th[text()='To Account/Wallet']")
    To_account_name = (By.XPATH, "//th[text()='To Account Name']")
    Reason = (By.XPATH, "//th[text()='Reason']")
    Execute_order = (By.XPATH, "//th[text()='Execute Order']")
    Status = (By.XPATH, "//th[text()='Status']")

    Footer = (By.XPATH, "//footer[@class='ant-layout-footer p-4 text-right text-white bg-sidebar css-2dphzb']")

    """Asset Swap Settlement"""
    A_from_asset = (By.XPATH, "//th[text()='From Asset']")
    A_from_quantity = (By.XPATH, "//th[text()='From Quantity']")
    A_from_venue = (By.XPATH, "//th[text()='From Venue']")
    A_from_account = (By.XPATH, "//th[text()='From Account']")
    A_from_account_name = (By.XPATH, "//th[text()='From Account Name']")
    A_to_asset = (By.XPATH, "//th[text()='To Asset']")
    A_to_quantity = (By.XPATH, "//th[text()='To Quantity']")
    A_To_venue = (By.XPATH, "//th[text()='To Venue']")
    A_counterparty_name = (By.XPATH, "//th[text()='Counterparty Name']")
    A_to_account_wallet = (By.XPATH, "//th[text()='To Account/Wallet']")
    A_to_account_name = (By.XPATH, "//th[text()='To Account Name']")
    A_reason = (By.XPATH, "//th[text()='Reason']")
    A_execute_order = (By.XPATH, "//th[text()='Execute Order']")
    A_status = (By.XPATH, "//th[text()='Status']")

    def click_on_trade_settlement(self):
        self.click(self.Trades_settlement)

