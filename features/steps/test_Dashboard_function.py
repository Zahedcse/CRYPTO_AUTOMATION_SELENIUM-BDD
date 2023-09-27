from behave import given, then


@given("the user is on the dashboard")
def verify_dashboard_page(context):
    context.app.dashboard_page.verify_home_text()


@then("they should see the total assets text")
def verify_total_assets_text(context):
    context.app.dashboard_page.verify_total_asset_text()


@then("they should see the total asset amount")
def verify_total_assets_amount(context):
    context.app.dashboard_page.verify_total_asset_amount()


@then("they should see the total deposit text")
def verify_total_deposits_text(context):
    context.app.dashboard_page.verify_total_deposit_text()


@then("they should see the total deposit amount")
def verify_total_deposits_amount(context):
    context.app.dashboard_page.verify_total_deposit_amount()


@then("they should see the total liability text")
def verify_total_liabilities_text(context):
    context.app.dashboard_page.verify_total_liability_text()


@then("they should see the total liability amount")
def verify_total_liabilities_amount(context):
    context.app.dashboard_page.verify_total_liability_amount()


@then("they should see the total withdrawals text")
def verify_total_withdrawals_text(context):
    context.app.dashboard_page.verify_total_withdrawal_text()


@then("they should see the total withdrawals amount")
def verify_total_withdrawals_amount(context):
    context.app.dashboard_page.verify_total_withdrawal_amount()


@then("they should check all the table headers")
def verify_table_headers(context):
    context.app.dashboard_page.get_table_header_text()


@then("they should check all the Pie Chart Elements")
def verify_table_headers(context):
    context.app.dashboard_page.get_pie_chart_text()
