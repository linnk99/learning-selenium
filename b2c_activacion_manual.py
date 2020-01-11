from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get("https://platzi.com/")

driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'T')
driver.get("https://platzi.com/platzi-admin")

""" user_name = driver.find_element_by_id("id_username")
user_name.send_keys("linnk99@gmail.com")
password = driver.find_element_by_id("id_password")
password.send_keys("987654abc")
password.send_keys(Keys.ENTER) """



