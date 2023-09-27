# Created by Zahed
Feature: Client-Management

@login_required
  Scenario: User will be able to create New Clients
    When the user on the Client Management Page
    Then the user will see the table of contents
    Then the user will Click on the Settings icon
    Then the user will add some new header in the Table and Update it
    Then then the user will see the updated table headers in the Table
#    Then the user will Close the Settings Tab
    Then the user will click on the New Clients Button
    Then the user will click on the retail client button
    Then the user will fill the fields for retail client
    Then the user will click on the client Management link
    Then User will be click on the Client Management Table and will create a Institutional Client
