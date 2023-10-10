from behave import *


@when('user is navigate to trade settlement')
def navigate_to_trade_settlement(context):
    context.app.trade_settlement.click_on_trade_settlement()
