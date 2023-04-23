from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from robber import expect
import os


file = os.path.abspath("test_data/test.txt")


@given('the website is launched')
def step_impl(context):
    context.browser.get(context.base_url)

@step('the web page loads')
def step_impl(context):
    WebDriverWait(context.browser, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"body").is_displayed())

@then('the header is displayed and the text is {text}')
def step_impl(context, text):
    header = WebDriverWait(context.browser, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"h1"))
    expected_conditions.visibility_of(header)
    expected_conditions.text_to_be_present_in_element(header.text,text)

@step('the sub header is displayed and the text is {text}')
def step_impl(context, text):
    sub_header = context.browser.find_element(By.TAG_NAME,"h2")
    expected_conditions.visibility_of(sub_header)
    expected_conditions.text_to_be_present_in_element(sub_header.text,text)

@given('the {text} link is displayed and clickable')
def step_impl(context, text):
    link = context.browser.find_element(By.XPATH, f"//a[contains(text(),'{text}')]")
    expected_conditions.visibility_of(link)
    expected_conditions.element_to_be_clickable(link)

@when('the {text} link is clicked')
def step_impl(context, text):
    link = context.browser.find_element(By.XPATH, f"//a[contains(text(),'{text}')]")
    link.click()

@step('verify the h3 header on the new page is displayed and the text is {text}')
def step_impl(context, text):
    h3 = WebDriverWait(context.browser, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"h3"))
    expected_conditions.visibility_of(h3)
    expected_conditions.text_to_be_present_in_element(h3.text,text)

@step('there is a clickable {text} button displayed')
def step_impl(context, text):
    button = context.browser.find_element(By.XPATH, f"//button[contains(text(),'{text}')]")
    expected_conditions.visibility_of(button)
    expected_conditions.element_to_be_clickable(button)

@step('the {text} button is clicked')
def step_impl(context, text):
    button = context.browser.find_element(By.XPATH, f"//button[contains(text(),'{text}')]")
    button.click()

@step('the Delete button does not exist')
def step_impl(context):
    button = context.browser.find_elements(By.XPATH,"//button[contains(text(),'Delete')]")
    expect(len(button)).to.equal(0)

@step('the h2 header on the new page is displayed and the text is {text}')
def step_impl(context, text):
    h2 = WebDriverWait(context.browser, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"h2"))
    expected_conditions.visibility_of(h2)
    expected_conditions.text_to_be_present_in_element(h2.text,text)

@step('the email input is displayed and enabled')
def step_impl(context):
    email_input = context.browser.find_element(By.ID, "email")
    expected_conditions.visibility_of(email_input)
    expect(email_input.is_enabled()).to.be.true()

@step('the Retrieve Password button is displayed and enabled')
def step_impl(context):
    button = context.browser.find_element(By.ID, "form_submit")
    expected_conditions.text_to_be_present_in_element(button.text, "Retrieve password")
    expected_conditions.visibility_of(button)
    expected_conditions.element_to_be_clickable(button)

@when('a valid email is typed into the email input')
def step_impl(context):
    email_input = context.browser.find_element(By.ID, "email")
    email_input.send_keys("test@email.com")

@when('the Retrieve password button is pressed')
def step_impl(context):
    button = context.browser.find_element(By.ID, "form_submit")
    button.click()

@then('Internal Server Error message is displayed')
def step_impl(context):
    body = context.browser.find_element(By.TAG_NAME, "body")
    expected_conditions.text_to_be_present_in_element(body.text, "Internal Server Error")

@step('the file upload input is displayed and enabled')
def step_impl(context):
    file_input = context.browser.find_element(By.ID, "file-upload")
    expected_conditions.visibility_of(file_input)
    expect(file_input.is_enabled()).to.be.true()

@step('the Upload input is displayed and enabled')
def step_impl(context):
    upload_input = context.browser.find_element(By.ID, "file-submit")
    expected_conditions.visibility_of(upload_input)
    expect(upload_input.is_enabled()).to.be.true()

@step('the test file is uploaded to the file upload input')
def step_impl(context):
    file_input = context.browser.find_element(By.ID, "file-upload")
    file_input.send_keys(file)

@step('the upload input is clicked')
def step_impl(context):
    upload_input = context.browser.find_element(By.ID, "file-submit")
    upload_input.click()

@step('the success message should appear')
def step_impl(context):
    success_message = context.browser.find_element(By.TAG_NAME, "h3")
    expected_conditions.visibility_of(success_message)
    expected_conditions.text_to_be_present_in_element(success_message,"File Uploaded!")

@step('verify the test file path is shown in the uploaded files div')
def step_impl(context):
    uploaded_files = context.browser.find_element(By.ID, "uploaded-files")
    expected_conditions.visibility_of(uploaded_files)
    expected_conditions.text_to_be_present_in_element(uploaded_files,"test.txt")

@step('press the Click Here link and navigate to the next window')
def step_impl(context):
    first_window = context.browser.current_window_handle
    context.browser.find_element(By.LINK_TEXT, "Click Here").click()
    for window in context.browser.window_handles:
        if window != first_window:
            context.browser.switch_to.window(window)
        break 

@step('verify the title of the page is New Window')
def step_impl(context):
    expected_conditions.title_is("New Window")

@step('the Click Here link is displayed and clickable')
def step_impl(context):
    link = context.browser.find_element(By.XPATH, "//a[contains(@href,'windows/new')]")
    expected_conditions.visibility_of(link)
    expected_conditions.element_to_be_clickable(link)

@step('verify the hot spot is visible')
def step_impl(context):
    hot_spot_div = context.browser.find_element(By.ID, "hot-spot")
    expected_conditions.visibility_of(hot_spot_div)

@step('the hotspot is clicked with the right mouse button')
def step_impl(context):
    action = ActionChains(context.browser)
    hot_spot_div = context.browser.find_element(By.ID, "hot-spot")
    action.context_click(hot_spot_div).perform()

@step('a JS alert appears with You selected a context menu in the message')
def step_impl(context):
    alert_displayed = expected_conditions.alert_is_present()
    expected_conditions.text_to_be_present_in_element(alert_displayed, "You selected a context menu")

import time
@step('the JS alert is accepted')
def step_impl(context):
    window_alert = context.browser.switch_to.alert
    window_alert.accept()

#helper function that checks if the alert window can be switched to
def alert_closed(context):
        #if it can, we do nothing
        try:
            context.browser.switch_to.alert
        #if the alert can't be accessed, it must be closed
        except:
            return True

@step('the JS alert should no longer be displayed')
def step_impl(context):
    WebDriverWait(context.browser, timeout=10).until(alert_closed)
