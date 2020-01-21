import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

class usando_unittest(unittest.TestCase):
    
    def SetUp(self):
        delf.driver = webdriver.Firefox(executable_path = "./geckodriver")
    
    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        sleep(3)
        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        options = select.find_elements_by_tag_name("option")
        sleep(3)
        
        for option in options:
            print(f"Values are: {option.get.attribute()}")
            options.click()
            sleep(1)
        
        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        sleep(3)
        
if __name__ == "__main__":
    unittest.main()