import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = "./geckodriver")
    
    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("https://www.google.com")
        buscar_por_xpath = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        buscar_por_xpath.send_keys("selenium")
        buscar_por_xpath.send_keys(Keys.ARROW_DOWN)
        buscar_por_xpath.send_keys(Keys.ARROW_DOWN)
        sleep(3)
        buscar_por_xpath.send_keys(Keys.RETURN)
        sleep(3)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
        



#xpath = una estructura de objetos
#xpath relativo: //*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input
#xpath absoluto: 