from selenium import webdriver

driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get("https://platzi.com")
driver.close()