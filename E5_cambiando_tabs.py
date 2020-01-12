import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = "./geckodriver")
    
    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("https://www.google.com")
        sleep(3)
        driver.execute_script("window.open('');") #abre una nueva ventana
        sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.stackoverflow.com")
        sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        sleep(3)

if __name__ == "__main__":
    unittest.main()