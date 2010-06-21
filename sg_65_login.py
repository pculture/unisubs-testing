# Litmus Subgroup 65 - Login / Logout Tests
# 1. 378 Site Login
# 2. 379 Twitter Account
# 3. 380 Open ID
# 4. 381 Gmail

from selenium import selenium
import unittest, time, re, sys
import mslib, website, widget, testvars

# ----------------------------------------------------------------------


class tc_378(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def tc_378_site_login(self):
        sel = self.selenium
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        # verify
        website.verifyLogIn(self,sel,testvars.siteuser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()





 
