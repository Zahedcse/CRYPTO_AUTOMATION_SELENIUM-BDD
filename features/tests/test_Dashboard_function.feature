Feature: Dashboard

@login_required
Scenario: User views the dashboard
    Given the user is on the dashboard
    Then they should see the total assets text
    And they should see the total asset amount
    And they should see the total deposit text
    And they should see the total deposit amount
    And they should see the total liability text
    And they should see the total liability amount
    And they should see the total withdrawals text
    And they should see the total withdrawals amount
    And they should check all the table headers
    And they should check all the Pie Chart Elements
