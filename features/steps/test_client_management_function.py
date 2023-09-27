import time

from behave import then, when


@when("the user on the Client Management Page")
def click_on_the_Client_management_page(context):
    context.app.client_management.click_on_Client_Management()
    time.sleep(5)


@then("the user will see the table of contents")
def verify_table_headers(context):
    context.app.client_management.get_table_header()
    time.sleep(3)


@then("the user will Click on the Settings icon")
def verify_table_headers(context):
    context.app.client_management.open_settings_icon()


@then('the user will add some new header in the Table and Update it')
def add_some_table_header(context):
    header = context.app.client_management
    header.add_some_headers()


@then('then the user will see the updated table headers in the Table')
def check_table_headers(context):
    context.app.client_management.verify_the_table_headers()


@then("the user will Close the Settings Tab")
def verify_table_headers(context):
    context.app.client_management.close_settings_icon()


@then("the user will click on the New Clients Button")
def verify_table_headers(context):
    context.app.client_management.add_new_client()


@then("the user will click on the retail client button")
def verify_table_headers(context):
    context.app.client_management.add_retail_client()


@then("the user will fill the fields for retail client")
def fill_retail_details(context):
    client = context.app.client_management
    client.enter_clientID()
    client.enter_Client_Name()
    client.enter_Date_Of_Birth()
    client.enter_Residence_Address()
    client.enter_Email()
    client.enter_Emergency_Contact()
    client.enter_Account_Manager()
    client.enter_Remark()
    client.enter_Save_Button()
    time.sleep(3)


@then('the user will click on the client Management link')
def click_client_management(context):
    context.app.client_management.click_on_Client_Management_link()


@then('User will be click on the Client Management Table and will create a Institutional Client')
def create_institutional_client(context):
    ins_client = context.app.client_management
    ins_client.add_new_client_again()
    ins_client.add_institutional_client()
    ins_client.input_clientID()
    ins_client.input_clientName()
    ins_client.input_address()
    ins_client.input_client_phone()
    ins_client.input_mobile()
    ins_client.input_email()
    ins_client.input_rest_of_the_details()
    ins_client.click_on_save()
    time.sleep(5)

