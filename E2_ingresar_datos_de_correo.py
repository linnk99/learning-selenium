from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get("https://gmail.com")

user = driver.find_element_by_id("identifierId")
user.send_keys("linnk99@gmail.com")
user.send_keys(Keys.ENTER)
sleep(3)

password = driver.find_element_by_name("password")
password.send_keys("")
password.send_keys(Keys.ENTER)

sleep(5)

driver.close()
