import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sleep import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = "./geckodriver")
    
    def test_next_or_previous_page()