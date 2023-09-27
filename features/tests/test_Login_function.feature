Feature: Authentication

  Scenario: User logs in to the application successfully
    Given the user is on the Moops login page
    When the user enters their email
    And the user enters their password
    And the user clicks the login button
    Then they should be on the home page
