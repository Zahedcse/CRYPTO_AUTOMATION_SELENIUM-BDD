# Created by Zahed
Feature: Portfolio Management
@login_required
  Scenario: User Will be able to see portfolios and Transfer assets
    When the user is on the Portfolio Management
    Then the user will be able to click on a portfolio
    Then the user will be able to see the portfolio valuations and total PnL
    Then the user will be able to verify the portfolio valuations summations
    Then the user will be able to verify the Total P&L summations
    Then the user will able to see the portfolio Assets Table
