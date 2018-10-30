import selenium
from selenium import webdriver

def rewardsSignIn(driver, email, password):
    # This focuses the email field of the page, inputs the email from the user and then send the 'enter' command
    search_field = driver.find_element_by_name("loginfmt")
    search_field.send_keys(email + u'\ue007')

    # This focuses the password field of the page, inputs the password from the user and then send the 'enter' command
    search_field = driver.find_element_by_name("passwd")
    search_field.send_keys(password + u'\ue007')

