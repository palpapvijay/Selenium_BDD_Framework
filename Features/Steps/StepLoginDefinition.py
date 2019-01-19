from behave import *
from selenium import webdriver

@given(u'user in login page')
def step_impl(context):
    context.driver.get("http://www.thetestingworld.com/testings/")


@when(u'user enters username')
def step_impl(context):
    context.driver.find_element_by_name('fld_username').send_keys("User1")


@when(u'user enters password')
def step_impl(context):
    context.driver.find_element_by_name('fld_password').send_keys("vijay123")


@when(u'user enters Email ID')
def step_impl(context):
    context.driver.find_element_by_name('fld_email').send_keys("vijay@iqs.com")


@when(u'user enter login button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@type = "submit" and @value = "Sign up"]').click()


@then(u'user should be logged in successfully')
def step_impl(context):
    print("Logged in successfully")


@when(u'user enters duplicate username')
def step_impl(context):
    print("Duplicated user name")