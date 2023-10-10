import time

from behave import when, then


@when('the user is on the Portfolio Management')
def user_on_the_portfolio_management(context):
    time.sleep(5)
    context.app.portfolio_management.click_portfolio_management()


@then('the user will be able to click on a portfolio {portfolio}')
def user_click_on_portfolio(context, portfolio):
    context.app.portfolio_management.click_portfolio(portfolio)
    time.sleep(2)


@then('the user will be able to see the portfolio valuations and total PnL')
def portfolio_valuation_and_pnl(context):
    PV = context.app.portfolio_management
    PV.verify_valuation_text()
    PV.verify_total_pnl()


@then('the user will be able to verify the portfolio valuations summations')
def verify_portfolio_valuations(context):
    time.sleep(3)
    PV = context.app.portfolio_management
    PV.verify_valuation_summation()


@then('the user will be able to verify the Total P&L summations')
def verify_pnl_valuations(context):
    time.sleep(3)
    PV = context.app.portfolio_management
    PV.click_on_first_Page()
    PV.verify_TotalPnL_summation()


@then("the user will able to see the portfolio Assets Table")
def verify_table_contents(context):
    context.app.portfolio_management.verify_asset_table_headings()


"""Asset Transfer Table"""


@then('the user will click on the Asset transfer Table')
def click_on_asset_transfer(context):
    context.app.portfolio_management.click_asset_transfer()


@then('user will fill all the fields for FROM portfolio')
def fill_all_fields(context):
    context.app.portfolio_management.fill_swap_fields()


@then('user will fill all the fields for TO Portfolio')
def fill_to_fields(context):
    context.app.portfolio_management.fill_To_fields()
