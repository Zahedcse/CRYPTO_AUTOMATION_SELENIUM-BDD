# Created by Zahed
Feature: Portfolio Management
@login_required
  Scenario Outline: User Will be able to see portfolios and Transfer assets
    When the user is on the Portfolio Management
    Then the user will be able to click on a portfolio <portfolio>
    Then the user will be able to see the portfolio valuations and total PnL
    Then the user will be able to verify the portfolio valuations summations
    Then the user will be able to verify the Total P&L summations
    Then the user will able to see the portfolio Assets Table
  Examples:
  |portfolio|
#  |MPS001   |
  |MPS002   |
#  |MPS003   |

  @login_required
  Scenario Outline: User will be able to initiate SWAP Transfer
    When the user is on the Portfolio Management
    Then the user will be able to click on a portfolio <portfolio>
    Then the user will click on the Asset transfer Table
    Then user will fill all the fields for FROM portfolio
    Then user will fill all the fields for TO Portfolio
    Then User will go to the Trade Settlement Page to check the status
    Examples:
      | portfolio |
      | MPS002    |