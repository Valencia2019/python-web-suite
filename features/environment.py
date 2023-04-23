from behave import fixture, use_fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@fixture
def chrome_browser(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    yield context.browser

@fixture
def safari_browser(context):
    context.browser = webdriver.Safari()
    yield context.browser

#defaults to chrome browser
def before_all(context):
    context.base_url = "https://the-internet.herokuapp.com/"
    use_fixture(chrome_browser, context)

def before_feature(context, feature):
    if "android.device" in feature.tags:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('androidPackage', 'com.android.chrome')
        context.browser = webdriver.Chrome('./chromedriver', options=options)

#allows user to use tags to change browser
def before_scenario(context, scenario):
    if "chrome.browser" in scenario.tags:
        use_fixture(chrome_browser, context)
    if "safari.browser" in scenario.tags:
        use_fixture(safari_browser, context)


#cleanup
def after_all(context):
    context.browser.quit()