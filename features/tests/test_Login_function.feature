Feature: Authentication
  @login
  Scenario Outline: User logs in to the application successfully as "<email>"
    Given the user is on the Moops login page
    When the user enters their email "<email>"
    And the user enters their password "<password>"
    And the user clicks the login button
    Then they should be on the home page
    Examples:
      |email                          |password     |
      |admin@moops.com                |Admin@123    |
      |admin@tulip-tech.com           |Admin@456    |
      |custody@tulip-tech.com         |Custody@456  |

  @login
  Scenario: User logged in using valid email and Invalid Password
    Given the user is on the Moops login page
    When the user enters their email "admin@moops.com"
    And the user enters their password "1234688"
    And the user clicks the login button
    Then they should be on the home page

  @login
  Scenario: User logged in using Invalid email and valid Password
    Given the user is on the Moops login page
    When the user enters their email "admin65@moops.com"
    And the user enters their password "Admin@123"
    And the user clicks the login button
    Then they should be on the home page

