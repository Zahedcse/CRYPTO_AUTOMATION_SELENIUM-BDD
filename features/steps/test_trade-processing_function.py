import time
from behave import when, then


@when("the user on the Trade processing page")
def click_on_Trade_processing_page(context):
    time.sleep(3)
    context.app.trade_processing.click_on_Trade_processing_tab()


@then("the user will verify the All Trade, Exchange and OTC text")
def verify_tabs(context):
    context.app.trade_processing.get_all_tabs()
    time.sleep(2)


@then("the user will be able to click Exchange and OTC tab")
def Click_on_particular_tab(context):
    context.app.trade_processing.click_on_tab()
    time.sleep(1)


@then("the user will see the contents of table")
def verify_table_headers(context):
    context.app.trade_processing.table_header_list()
    # context.app.trade_processing.click_on_all_trade_tab()
    # time.sleep(2)


@then("the user will click on New Trade Button")
def click_new_trade_button(context):
    context.app.trade_processing.click_on_new_trade_button()


@then('the user will create some Trade by {PortfolioID}, {Quantity}, {price}')
def enter_all_the_fields_info(context, PortfolioID, Quantity, price):
    TP = context.app.trade_processing
    TP.click_on_asset_name_filed()
    time.sleep(2)
    TP.select_asset_BTC()
    TP.enter_portfolio_ID(PortfolioID)
    TP.click_on_venue_field()
    TP.select_venue_Exchange()
    TP.click_on_instrument_type_field()
    TP.select_instrument_type_Spot()
    TP.click_on_position_filed()
    TP.select_position_value()
    TP.enter_Quantity(Quantity)
    TP.enter_price(price)
    TP.Click_on_initiate_button()


@then('then I will create some Trade by Negative Values "{PortfolioID}", "{Quantity}", "{message}"')
def enter_all_the_fields(context, PortfolioID, Quantity, message):
    Tp = context.app.trade_processing
    Tp.click_on_asset_name_filed()
    time.sleep(2)
    Tp.select_asset_BTC()
    Tp.enter_portfolio_ID(PortfolioID)
    Tp.click_on_venue_field()
    Tp.select_venue_Exchange()
    Tp.click_on_instrument_type_field()
    Tp.select_instrument_type_Spot()
    Tp.click_on_position_filed()
    Tp.select_position_value()
    Tp.enter_Quantity(Quantity)
    Tp.verify_error_message(message)
    Tp.Click_on_initiate_button()


@then('the user should see successful message "{text}"')
def verify_message(context, text):
    context.app.trade_processing.verify_success_message(text)


# @then('the user should see error message "{message}"')
# def verify_errorMessage(context, message):
#     context.app.trade_processing.verify_error_message(message)


@then("the user will verify the price")
def verify_price(context):
    context.app.trade_processing.assert_quantity_price_trade()


@then("the user will confirm it")
def confirm_trade(context):
    TP = context.app.trade_processing
    TP.click_on_check_box()
    TP.click_on_confirm_button()
    time.sleep(1)


@then("the user will perform edit functions on the created trade")
def edit_function(context):
    context.app.trade_processing.click_on_edit_trade()
    context.app.trade_processing.clear_all_input_fields()
    context.app.trade_processing.edit_trade()
    time.sleep(5)


@then("the user will go to portfolio management")
def go_to_portfolio_management(context):
    context.app.portfolio_management.click_portfolio_management()
    time.sleep(2)
    context.app.portfolio_management.click_portfolio()
    time.sleep(2)


@then("the user will validate the P&L and P&L %")
def validate_PnL_and_Percent(context):
    context.app.trade_processing.validate_PnL_and_percentage()
