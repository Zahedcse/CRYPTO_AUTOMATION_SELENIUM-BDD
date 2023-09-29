from behave import given, when, then


@given("the user is on the Moops login page")
def open_moops_page(context):
    context.driver.get('https://moops-dev.tulip-tech.com/login')


@when('the user enters their email "{email}"')
def input_email(context, email):
    context.app.login_page.input_email(email)


@when('the user enters their password "{password}"')
def input_password(context, password):
    context.app.login_page.input_password(password)


@when("the user clicks the login button")
def click_button(context):
    context.app.login_page.click_submit()


@then("they should be on the home page")
def click_button(context):
    context.app.dashboard_page.verify_home_text()
