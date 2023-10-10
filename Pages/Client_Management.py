import time

from selenium.webdriver.common.by import By
from Pages.Base import Page
from utilities.EmailWithTimeStampGenerator import generate_client_id


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
    Institutional_client_KYC = (By.NAME, "kyc")
    Institutional_client_AML_screening = (By.ID, "amlScreening")

    def click_on_Client_Management(self):
        time.sleep(5)
        self.click(self.Client_management_Tab)

    def get_table_header(self):
        header_elements = self.find_elements(self.Table_headings_list)
        print(len(header_elements))
        actual_column_names = [column_header.text for column_header in header_elements]
        print(actual_column_names)
        expected_column_names = ['Type', 'ClientID', 'Client Name', 'Client Manager', 'KYC', 'AML Screening']
        assert actual_column_names == expected_column_names, f"expected column names {expected_column_names} but got {actual_column_names}"

    def open_settings_icon(self):
        self.click(self.setting_icon)

    def add_some_headers(self):
        headers_to_add = [self.Checkbox_chat_history, self.checkbox_tags, self.checkbox_address]
        for header in headers_to_add:
            self.click(header)
        self.click(self.settings_update)
        time.sleep(2)

    def verify_the_table_headers(self):
        header_elements = self.find_elements(self.Table_headings_list)
        actual_column_names = [column_header.text for column_header in header_elements]
        print(actual_column_names)
        expected_column_names = ['Type', 'ClientID', 'Client Name', 'Client Manager', 'KYC', 'AML Screening',
                                 'Chat History', 'Tags', 'Address']
        assert actual_column_names == expected_column_names, f"expected {expected_column_names} but got {actual_column_names}"

    def add_new_client(self):
        self.click(self.Add_client_button)

    def add_retail_client(self):
        self.click(self.Retail_client)

    def enter_clientID(self):
        clientId = generate_client_id()
        self.input_text(self.Client_Id, clientId)

    def enter_Client_Name(self, ClientName):
        self.input_text(self.Client_Name, ClientName)

    def enter_Date_Of_Birth(self, ClientDOB):
        self.input_text(self.Date_Of_Birth, ClientDOB)

    def enter_Residence_Address(self, ClientAddress):
        self.input_text(self.Residence_Address, ClientAddress)

    def enter_Email(self, ClientEmail):
        self.input_text(self.Email, ClientEmail)

    def enter_Emergency_Contact(self, ClientMobile):
        self.input_text(self.Emergency_Contact, ClientMobile)

    def enter_Account_Manager(self, ClientAccManager):
        self.input_text(self.Account_Manager, ClientAccManager)

    def enter_Remark(self, ClientRemark):
        self.input_text(self.Remark, ClientRemark)

    def click_Save_Button(self):
        self.click(self.Save_Button)

    def click_on_Client_Management_link(self):
        self.click(self.Client_management_link)

    def add_ins_client(self):
        self.click(self.Add_client_button)

    def click_institutional_client(self):
        self.click(self.Institutional_client)

    def input_clientID(self):
        client_id = generate_client_id()
        self.input_text(self.Client_Id, client_id)

    def input_clientName(self, InsName):
        self.input_text(self.Client_Name, InsName)

    def input_address(self, InsAddress):
        self.input_text(self.Residence_Address, InsAddress)

    def input_client_phone(self, InsPhone):
        self.input_text(self.Phone_Number, InsPhone)

    def input_mobile(self, InsMobile):
        self.input_text(self.Mobile_Number, InsMobile)

    def input_email(self, InsEmail):
        self.input_text(self.Email, InsEmail)

    def input_rest_of_the_details(self, InsAccManager, InsAMLScre, Remark, InsChatHistory):
        self.input_text(self.Account_Manager, InsAccManager)
        self.input_text(self.Institutional_client_AML_screening, InsAMLScre)
        self.input_text(self.Remark, Remark)
        self.input_text(self.Chat_History, InsChatHistory)

    def click_on_save(self):
        self.click(self.Save_Button)
