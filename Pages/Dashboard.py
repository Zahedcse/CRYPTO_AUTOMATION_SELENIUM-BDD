from selenium.webdriver.common.by import By

from Pages.Base import Page


class Dashboard(Page):
    Home_text = (By.CSS_SELECTOR, 'span.ant-breadcrumb-link')
    Total_asset_text = (By.XPATH, "//div[.='Total Asset']")
    Total_asset = (By.XPATH, "//div[.='$5.3 B']")
    Total_deposit_text = (By.XPATH, "//div[.='Total Deposit']")
    Total_deposit = (By.XPATH, "//div[.='$2.9 M']")
    Total_Liability_text = (By.XPATH, "//div[.='Total Liability']")
    Total_Liability = (By.XPATH, "//div[.='$430 M']")
    Total_Withdrawals_text = (By.XPATH, "//div[.='Total Withdrawals']")
    Total_Withdrawals = (By.XPATH, "//div[.='$1.83 M']")

    """Trading Activities Table"""
    table_column_headers = (By.XPATH, "//tr/th[contains(@scope,'col')]")

    """Pie Chart Elements"""
    pie_chart_columns = (By.XPATH, "//div[@class='pb-6']//div/span[2]")

    def verify_home_text(self):
        self.assert_partial_text('Home', self.Home_text)

    def verify_total_asset_text(self):
        self.assert_text("Total Asset", self.Total_asset_text)

    def verify_total_asset_amount(self):
        self.assert_text("$5.3 B", self.Total_asset)

    def verify_total_deposit_text(self):
        self.assert_text("Total Deposit", self.Total_deposit_text)

    def verify_total_deposit_amount(self):
        self.assert_text("$2.9 M", self.Total_deposit)

    def verify_total_liability_text(self):
        self.assert_text("Total Liability", self.Total_Liability_text)

    def verify_total_liability_amount(self):
        self.assert_text("$430 M", self.Total_Liability)

    def verify_total_withdrawal_text(self):
        self.assert_text("Total Withdrawals", self.Total_Withdrawals_text)

    def verify_total_withdrawal_amount(self):
        self.assert_text("$1.83 M", self.Total_Withdrawals)

    def get_table_header_text(self):
        header_elements = self.find_elements(self.table_column_headers)
        actual_column_names = [column_header.text for column_header in header_elements]
        expected_column_names = ["Assets Name", "Trade ID", "Client ID", "Venue", "Instrument", "Price", "Quantity",
                                 "Value"]
        if actual_column_names == expected_column_names:
            print("Column names matches the expected list.")
        else:
            print("Column names do not match the expected list.")

    def get_pie_chart_text(self):
        header_elements = self.find_elements(self.table_column_headers)
        actual_column_names = [column_header.text for column_header in header_elements]
        expected_column_names = ["Spot", "Future", "Perpetual", "Op3on", "Transfer - in", "Transfer - Out"]
        if actual_column_names == expected_column_names:
            print("Column names matches the expected list for Pie Chart.")
        else:
            print("Column names do not match the expected list.")
