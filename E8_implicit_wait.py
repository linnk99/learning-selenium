import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = "./geckodriver")
        
    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #segundos
        driver.get("https://www.google.com")
        myDynamicElement = driver.find_element_by_name("q")
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()