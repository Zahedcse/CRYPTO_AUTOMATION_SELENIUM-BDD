import time

from selenium.webdriver.common.by import By
from Pages.Base import Page


class ClientManagement(Page):
    Client_management_Tab = (By.XPATH, "(//li[@role='menuitem'])[2]")
    Client_management_link = (By.CSS_SELECTOR, ":nth-child(3) > .ant-breadcrumb-link")
    """Table Elements---------------------------------------"""
    Table_headings_list = (By.XPATH, "//thead/tr/th")

    Sort_by = (By.CSS_SELECTOR, "span.ant-select-selection-search")
    Sort_by_options = (By.CSS_SELECTOR, "div.ant-select-item-option")
    setting_icon = (By.CSS_SELECTOR, ".mt-3 > .flex > .ant-btn")
    close_setting_icon = (By.CSS_SELECTOR, ".w-full > .ant-btn > span")
    settings_update = (By.CSS_SELECTOR, ".w-full > .ant-btn > span")
    Checkbox_chat_history = (By.CSS_SELECTOR, ".grid > :nth-child(7) > :nth-child(2)")
    checkbox_tags = (By.CSS_SELECTOR, ".grid > :nth-child(9) > :nth-child(2)")
    checkbox_address = (By.CSS_SELECTOR, ":nth-child(12) > :nth-child(2)")
    Close_button = (By.XPATH, "//button[@class='ant-modal-close']")
    Add_client_button = (By.XPATH, "//button/span[text()='Add Client ']")
    # ------------------Retail Client---------------------------------------------
    Retail_client = (By.LINK_TEXT, "Retail Client")
    Client_Id = (By.ID, "clientId")
    Client_Name = (By.NAME, "name")
    Date_Of_Birth = (By.XPATH, "//input[@placeholder='DD/MM/YY']")
    Nationality = (By.NAME, "nationality")
    # Nationality_Options =
    Residence_Address = (By.ID, "address")
    Phone_Number = (By.ID, "phoneNumber")
    Mobile_Number = (By.ID, "mobileNumber")
    Email = (By.ID, "email")
    Emergency_Contact = (By.ID, "emergencyContact")
    Emergency_Telephone = (By.ID, "emergencyPhone")
    KYC_Submit = (By.ID, "rc_select_1")
    # KYC_Options =
    Account_Manager = (By.ID, "accountManager")
    AML_Screening = (By.ID, "amlScreening")
    Remark = (By.ID, "remark")
    Chat_History = (By.ID, "chatHistory")
    Tags = (By.CSS_SELECTOR, "div.ant-select-selection-overflow-item")
    Document_Upload = (By.XPATH, "//p[text()='Document Upload']")
    Cancel_Button = (By.XPATH, "//button[@type='reset']")
    Save_Button = (By.XPATH, "//button[@type='submit']")
    # --------------------Institutional Client-------------------------------
    Institutional_client = (By.LINK_TEXT, "Institutional Client")
    Institutional_client_id = (By.ID, "clientId")
    Institute_name = (By.ID, "name")
    Institute_address = (By.ID, "address")
    Institutional_client_phone = (By.ID, "phoneNumber")
    Institutional_client_Mobile_Number = (By.ID, "mobileNumber")
    Institutional_client_email = (By.ID, "email")
    Institutional_client_KYC = (By.NAME, "kyc")
    Institutional_client_account_manager = (By.ID, "accountManager")
    Institutional_client_AML_screening = (By.ID, "amlScreening")
    Institutional_client_remark = (By.ID, "remark")
    Institutional_client_chat_history = (By.ID, "chatHistory")
    Institutional_client_document = (By.XPATH, "//p[text()='Document Upload']")
    Institutional_close_button = (By.XPATH, "//button[@type='reset']")
    Institutional_client_save_button = (By.XPATH, "//button[@type='submit']")

    def click_on_Client_Management(self):
        time.sleep(5)
        self.click(self.Client_management_Tab)

    def get_table_header(self):
        header_elements = self.find_elements(self.Table_headings_list)
        print(len(header_elements))
        actual_column_names = [column_header.text for column_header in header_elements]
        print(actual_column_names)
        expected_column_names = ['Type', 'ClientID', 'Client Name', 'Client Manager', 'KYC', 'AML Screening']
        if actual_column_names == expected_column_names:
            print("Column names matches the expected list.")
        else:
            print("Column names do not match the expected list.")

    def open_settings_icon(self):
        self.click(self.setting_icon)

    def add_some_headers(self):
        self.click(self.Checkbox_chat_history)
        self.click(self.checkbox_tags)
        self.click(self.checkbox_address)
        self.click(self.settings_update)
        time.sleep(4)

    def verify_the_table_headers(self):
        header_elements = self.find_elements(self.Table_headings_list)
        actual_column_names = [column_header.text for column_header in header_elements]
        print(actual_column_names)
        expected_column_names = ['Type', 'ClientID', 'Client Name', 'Client Manager', 'KYC', 'AML Screening',
                                 'Chat History', 'Tags', 'Address']
        if actual_column_names == expected_column_names:
            print("Column names matches the expected list.")
        else:
            print("Column names do not match the expected list.")

    def add_new_client(self):
        self.click(self.Add_client_button)

    def add_retail_client(self):
        self.click(self.Retail_client)

    def enter_clientID(self):
        self.input_text(self.Client_Id, "MPSPD")

    def enter_Client_Name(self):
        self.input_text(self.Client_Name, "Zahed Alam")

    def enter_Date_Of_Birth(self):
        self.input_text(self.Date_Of_Birth, "10-02-1998")

    def enter_Residence_Address(self):
        self.input_text(self.Residence_Address, "Dhaka, Bangladesh")

    def enter_Email(self):
        self.input_text(self.Email, "Zha@gmail.com")

    def enter_Emergency_Contact(self):
        self.input_text(self.Emergency_Contact, "01873634543")

    def enter_Account_Manager(self):
        self.input_text(self.Account_Manager, "Rakib Khan")

    def enter_Remark(self):
        self.input_text(self.Remark, "Hello")

    def enter_Save_Button(self):
        self.click(self.Save_Button)

    def click_on_Client_Management_link(self):
        self.click(self.Client_management_link)

    def add_new_client_again(self):
        self.click(self.Add_client_button)

    def add_institutional_client(self):
        self.click(self.Institutional_client)

    def input_clientID(self):
        self.input_text(self.Institutional_client_id, "MPSJH")

    def input_clientName(self):
        self.input_text(self.Institute_name, "TulipTech LTD")

    def input_address(self):
        self.input_text(self.Institute_address, "Leicester, UK")

    def input_client_phone(self):
        self.input_text(self.Institutional_client_phone, "98843756375")

    def input_mobile(self):
        self.input_text(self.Institutional_client_Mobile_Number, "01846899956")

    def input_email(self):
        self.input_text(self.Institutional_client_email, "tt@tulip-tech.com")

    def input_rest_of_the_details(self):
        self.input_text(self.Institutional_client_account_manager, "Rakib Khan")
        self.input_text(self.Institutional_client_AML_screening, "Hello AML")
        self.input_text(self.Institutional_client_remark, "Hello remark")
        self.input_text(self.Institutional_client_chat_history, "Hello chat history")

    def click_on_save(self):
        self.click(self.Institutional_client_save_button)
