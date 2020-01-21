import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = "./geckodriver")
    
    def test_usando_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        sleep(3)
        toggle = driver.find_element_by_xpath("//*[@id='main']/label[3]/div")
        toggle.click()
        sleep(3)
        toggle.click()
        sleep(3)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()