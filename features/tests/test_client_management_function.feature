# Created by Zahed
Feature: Client-Management

@login_required
Scenario Outline: User can create New Clients
    When the user navigates to the Client Management Page
    Then the user should see the table of contents
    Then the user clicks on the Settings icon
    Then the user adds new headers to the table and updates it
    Then the user should see the updated table headers
    Then the user clicks on the New Clients Button
    Then the user selects the retail client option
    Then the user fills in the details for the retail client
      | ClientID    | ClientName | ClientDOB    | ClientAddress        | ClientEmail       | ClientMobile   | ClientAccManager | ClientRemark |
      | ABC1236     | John Doe   | 01-01-1990   | 123 Main St          | john56@example.com| 1234567890     | Jane Smith       | Some remark  |
    Then the user clicks on the client Management link
    Then the user will create an Institutional Client with the following details
      | InsClientID | InsName   | InsDOB      | InsAddress           | InsEmail          | InsPhone     | InsMobile    | InsAccManager | InsAMLScre | Remark        | InsChatHistory |
      | XYZ456      | ACME Inc. | 02-02-1985  | 456 Elm St, Suite 1  | acme@example.com  | 9876543210   |  7567567567  |Mark Johnson   | Passed     | Great service | Yes            |

Examples:
   |
   |


