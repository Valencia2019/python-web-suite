Feature: Test using background steps from previous test
    Scenario: Smoke test the website
        Given the website is launched
        When the web page loads
        Then the header is displayed and the text is Welcome to the-internet
        And the sub header is displayed and the text is Available Examples