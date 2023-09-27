# Created by Nabia at 9/22/2023
Feature: Trade-Processing

@login_required
  Scenario: User will be able to create new trade
    When the user on the Trade processing page
    Then the user will verify the All Trade, Exchange and OTC text
    Then the user will be able to click Exchange and OTC tab
    Then the user will see the contents of table
    Then the user will create some Trade, will verify the price and will confirm it
    Then the user will go to portfolio management
#    Then the user will validate the P&L and P&L %
#    Then the user will perform sell trade
#    Then the user will perform edit functions on the created trade




