import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = "./geckodriver")
    
    def test_next_or_previous_page(self):
        driver = self.driver
        driver.get("https://www.google.com")
        sleep(3)
        driver.get("https://www.gmail.com")
        sleep(3)
        driver.get("https://www.youtube.com")
        sleep(3)
        driver.back()
        sleep(3)
        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()