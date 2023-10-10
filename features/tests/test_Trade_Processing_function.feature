# Created by Nabia at 9/22/2023
Feature: Trade-Processing

@login_required
  Scenario: User will be able to create new trade
    When the user on the Trade processing page
    Then the user will verify the All Trade, Exchange and OTC text
    Then the user will be able to click Exchange and OTC tab
    Then the user will see the contents of table

@login_required
Scenario Outline: User will create trade with Valid Data and confirm it
  When the user on the Trade processing page
  Then the user will click on New Trade Button
  Then the user will create some Trade by <PortfolioID>, <Quantity>, <Price>
  Then the user should see successful message "The Trade has been successfully stored"
  Then the user will verify the price
  Then the user will confirm it
  Examples:
    |PortfolioID| Quantity| Price|
    |MPS002     | 100     |26500 |
    |MPS003     | 50      |24500 |
    |MPS004     | 70      |25500 |

@login_required
Scenario: User will try to create trade with Invalid Data (Negative Quantity)
   When the user on the Trade processing page
   Then the user will click on New Trade Button
   Then then I will create some Trade by Negative Values "MPS002", "-100", "Number must be greater than or equal to 1"
