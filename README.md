# Python Webdriver Testsuite

This project requires python3 and pip to both be installed. Please do so before following installation instructions.


## Installation
1. Clone the repo
3. In terminal, type in `pip install -r requirements.txt` and hit enter.
4. Verify that behave is in your PATH
5. Create venv
6. In terminal, type in `behave` and hit enter.

## Running specific browser
Since this testsuite is so small, I implemented browser tagging at the scenario level and they can be used with `@chrome.browser` or `@safari.browser`

## Safari setup instructions
Unlike Chromedriver, Safari doesn't have the same installation ease so instructions for installing safaridriver can be found here: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari. After following those steps, you should be able to use browser tagging to run on it. Please note that use of this project with Safari is untested.