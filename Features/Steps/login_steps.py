from behave import given, when, then
from selenium import webdriver

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://amazon.com/login")

@when('I enter valid credentials')
def step_impl(context):
    username_input = context.driver.find_element_by_name("username")
    password_input = context.driver.find_element_by_name("password")

    username_input.send_keys("myusername")
    password_input.send_keys("mypassword")

@when('I click the login button')
def step_impl(context):
    login_button = context.driver.find_element_by_id("login_button")
    login_button.click()

@then('I should see the dashboard page')
def step_impl(context):
    assert "dashboard" in context.driver.current_url

@when('I enter invalid credentials')
def step_impl(context):
    username_input = context.driver.find_element_by_name("username")
    password_input = context.driver.find_element_by_name("password")

    username_input.send_keys("invalid_username")
    password_input.send_keys("invalid_password")

@then('I should see an error message')
def step_impl(context):
    error_message = context.driver.find_element_by_id("error_message")
    assert error_message.is_displayed()

