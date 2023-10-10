Feature: Trade Settlement Page

  Scenario: User will navigate to Trade Settlement and Will be able to Confirm Trades
    @when user is navigate to trade settlement
    @and user will click on asset swap settlement
    @then user will check the status of the trade
    @then user will click on confirm swap settlement