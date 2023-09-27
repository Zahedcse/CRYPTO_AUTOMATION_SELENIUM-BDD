import time
from behave import when, then


@when("the user on the Trade processing page")
def click_on_Trade_processing_page(context):
    time.sleep(5)
    context.app.trade_processing.click_on_Trade_processing_tab()


@then("the user will verify the All Trade, Exchange and OTC text")
def verify_tabs(context):
    context.app.trade_processing.get_all_tabs()
    time.sleep(2)


@then("the user will be able to click Exchange and OTC tab")
def Click_on_particular_tab(context):
    context.app.trade_processing.click_on_tab()
    time.sleep(2)


@then("the user will see the contents of table")
def verify_table_headers(context):
    context.app.trade_processing.table_header_list()
    time.sleep(2)


@then("the user will create some Trade, will verify the price and will confirm it")
def enter_all_the_fields_info(context):
    TP = context.app.trade_processing
    for i in range(1, 2):
        TP.click_on_new_trade_button()
        print("New Trade button Clicked")
        time.sleep(2)
        TP.click_on_asset_name_filed()
        time.sleep(2)
        # context.app.trade_processing.select_asset_WBC()
        # context.app.trade_processing.select_asset_BNB()
        # context.app.trade_processing.select_asset_ETH()
        TP.select_asset_BTC()
        TP.enter_portfolio_ID()
        TP.click_on_venue_field()
        if i == 1:
            TP.select_venue_Exchange()
            TP.click_on_instrument_type_field()
            TP.select_instrument_type_Spot()
        elif i == 2:
            TP.select_venue_OTC()
            TP.click_on_instrument_type_field()
            TP.select_instrument_type_Future()
        elif i == 3:
            TP.select_venue_Exchange()
            TP.click_on_instrument_type_field()
            TP.select_instrument_type_Perpetuals()
        elif i == 4:
            TP.select_venue_Exchange()
            TP.click_on_instrument_type_field()
            TP.select_instrument_type_Options()

        TP.click_on_position_filed()
        TP.select_position_value()
        TP.enter_Quantity()
        TP.enter_price()
        TP.Click_on_initiate_button()
        time.sleep(5)
        TP.click_on_all_trade_tab()
        time.sleep(5)
        TP.assert_quantity_price_trade()
        TP.click_on_check_box()
        TP.click_on_confirm_button()
        time.sleep(2)


# @then("the user will perform edit functions on the created trade")
# def edit_function(context):
#     context.app.trade_processing.edit_trade()
#     context.app.trade_processing.clear_portfolio_ID()
#     context.app.trade_processing.Edit_Portfolio_ID()
#     context.app.trade_processing.clear_quantity()
#     context.app.trade_processing.Edit_quantity()
#     context.app.trade_processing.click_on_update_trade_button()
#     time.sleep(5)


@then("the user will go to portfolio management")
def go_to_portfolio_management(context):
    context.app.portfolio_management.click_portfolio_management()
    time.sleep(2)
    context.app.portfolio_management.click_portfolio()
    time.sleep(2)


@then("the user will validate the P&L and P&L %")
def validate_PnL_and_Percent(context):
    context.app.trade_processing.validate_PnL_and_percentage()
