Feature: Five test scenarios in one spec file
    Background: reoccurring steps
        Given the website is launched
        When the web page loads
        Then the header is displayed and the text is Welcome to the-internet
        And the sub header is displayed and the text is Available Examples

    Scenario: Add and remove elements test
        Given the Add/Remove Elements link is displayed and clickable
        When the Add/Remove Elements link is clicked
        Then the web page loads
        And verify the h3 header on the new page is displayed and the text is Add/Remove Elements
        And there is a clickable Add Element button displayed
        When the Add Element button is clicked
        Then there is a clickable Delete button displayed
        And there is a clickable Add Element button displayed
        When the Delete button is clicked
        Then the Delete button does not exist
        And there is a clickable Add Element button displayed

    @chrome.browser
    Scenario: Forgot Password test
        Given the Forgot Password link is displayed and clickable
        When the Forgot Password link is clicked
        Then the web page loads
        And the h2 header on the new page is displayed and the text is Forgot Password
        And the email input is displayed and enabled
        And the Retrieve password button is displayed and enabled
        When a valid email is typed into the email input
        And the Retrieve password button is pressed
        Then Internal Server Error message is displayed

    Scenario: File Upload test
        Given the File Upload link is displayed and clickable
        When the File Upload link is clicked
        Then the web page loads
        And verify the h3 header on the new page is displayed and the text is File Uploader
        And the file upload input is displayed and enabled
        And the Upload input is displayed and enabled
        When the test file is uploaded to the file upload input
        And the upload input is clicked
        Then the success message should appear
        And verify the test file path is shown in the uploaded files div

    Scenario: Context Menu test
        Given the Context Menu link is displayed and clickable
        When the Context Menu link is clicked
        Then the web page loads
        And verify the h3 header on the new page is displayed and the text is Context Menu
        And verify the hot spot is visible
        When the hotspot is clicked with the right mouse button
        Then a JS alert appears with You selected a context menu in the message
        When the JS alert is accepted
        Then the JS alert should no longer be displayed

    
    Scenario: Multiple Windows test
        Given the Multiple Windows link is displayed and clickable
        When the Multiple Windows link is clicked
        Then the web page loads
        And verify the h3 header on the new page is displayed and the text is Opening a new window
        When the Click Here link is displayed and clickable
        Then press the Click Here link and navigate to the next window
        When the web page loads
        Then verify the title of the page is New Window

