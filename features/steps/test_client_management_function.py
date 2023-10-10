import time

from behave import then, when

from utilities.EmailWithTimeStampGenerator import get_new_email_with_timestamp, generate_client_id


@when(u"the user navigates to the Client Management Page")
def click_on_the_Client_management_page(context):
    context.app.client_management.click_on_Client_Management()
    time.sleep(3)


@then(u"the user should see the table of contents")
def verify_table_headers(context):
    context.app.client_management.get_table_header()
    time.sleep(3)


@then(u"the user clicks on the Settings icon")
def verify_table_headers(context):
    context.app.client_management.open_settings_icon()


@then(u'the user adds new headers to the table and updates it')
def add_some_table_header(context):
    header = context.app.client_management
    header.add_some_headers()


@then(u'the user should see the updated table headers')
def check_table_headers(context):
    context.app.client_management.verify_the_table_headers()


@then(u"the user will Close the Settings Tab")
def verify_table_headers(context):
    context.app.client_management.close_settings_icon()


@then(u"the user clicks on the New Clients Button")
def verify_table_headers(context):
    context.app.client_management.add_new_client()


@then(u"the user selects the retail client option")
def verify_table_headers(context):
    context.app.client_management.add_retail_client()


@then(u"the user fills in the details for the retail client")
def fill_retail_details(context):
    client = context.app.client_management
    table = context.table
    for row in table:
        client.enter_clientID()
        client.enter_Client_Name(row['Name'])
        client.enter_Date_Of_Birth(row['DOB'])
        client.enter_Residence_Address(row['Address'])
        new_email = get_new_email_with_timestamp()
        client.enter_Email(new_email)
        client.enter_Emergency_Contact(row['Mobile'])
        client.enter_Account_Manager(row['AccManager'])
        client.enter_Remark(row['Remark'])
        client.click_Save_Button()
        time.sleep(3)


@then(u'the user clicks on the client Management link')
def click_client_management(context):
    context.app.client_management.click_on_Client_Management_link()
    time.sleep(2)


@then(u'the user will create an Institutional Client with the following details')
def create_institutional_client(context):
    ins_client = context.app.client_management
    table = context.table
    for row in table:
        ins_client.add_ins_client()
        ins_client.click_institutional_client()
        ins_client.input_clientID()
        ins_client.input_clientName(row['InsName'])
        ins_client.input_address(row['InsAddress'])
        ins_client.input_client_phone(row['InsPhone'])
        ins_client.input_mobile(row['InsMobile'])
        new_email = get_new_email_with_timestamp()
        ins_client.input_email(new_email)
        ins_client.input_rest_of_the_details(row['InsAccManager'], row['InsAMLScre'], row['InsRemark'], row['InsChatHistory'])
        ins_client.click_on_save()
        time.sleep(6)

