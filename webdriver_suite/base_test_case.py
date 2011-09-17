import unittest
import logging
from selenium import webdriver
import testsetup

class BaseTestCase(unittest.TestCase):       

    def setUp(self):
        print " - starting: ",self.shortDescription()
        
      
    def tearDown(self):
        print " - completed: ",self.id()
        testsetup.browser.quit()
        
        
