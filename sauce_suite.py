"""
Subset of full regression tests designed for x-browser verification.
This particular suite is set up to run on sauce labs.
See http://saucelabs.com/products/docs/sauce-ondemand/browsers for correct Browser and version combos
"""

from selenium import selenium
import json
import unittest
import sauce_auth
import testvars
import sg_69_demoUI
import sg_64_subwidget

#----------------------------------------------------------------------
sauce_localhost = "saucelabs.com"
sauce_data = {\
                    "username": sauce_auth.sauce_user,\
                    "access-key": sauce_auth.sauce_key,\
                    "os": "Windows 2003",\
                    "browser": "opera",\
                    "browser-version": "10.",\
                    "record-video": False ,\
                    "job-name": "UniSubs x-browser ie8"\
                }

sauce_browser = json.dumps(sauce_data)


class demo_UI_suite(sg_69_demoUI.subgroup_69):
    """
    Selection of tests from subgroup 69, Demo UI tests.
    """
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        self.selenium = selenium(sauce_localhost, 4444, sauce_browser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def demo_UI_tests(self):
        subgroup_69.test_388
        subgroup_69.test_415
        
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)
       

class offsite_widget_suite(sg_64_subwidget.subgroup_64):
    """
    Selection of tests from subgroup 64 offsite widget tests
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """      
        self.verificationErrors = []
        self.selenium = selenium(sauce_localhost, 4444, sauce_browser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def offsite_widget_tests(self):
        subgroup_64.test_369
        subgroup_64.test_370
        
                         
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
