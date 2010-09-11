from selenium import selenium
import unittest
import os
import time
import re
import sys
import codecs
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class testtest(unittest.TestCase):
    """
    
    412 Step 3 Hold down to delay sub start
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The test cases of the subgroup
    def test_382(self):
         """
         Gmail login from widget
         http://litmus.pculture.org/show_test.cgi?id=382
         """
         sel = self.selenium
         sel.set_timeout(testvars.MSTestVariables["TimeOut"])
         #login
         website.SiteLogout(self,sel)
         website.start_demo(self,sel)
         widget.Login(self,sel,"google")
         offsite.GmailAuth(self,sel,testvars.gmailuser,testvars.passw)
         # verify

         widget.wait_for_offsite_login(self,sel)
         widget.close_widget(self,sel)
##         sel.select_window("null")
##         sel.refresh() 
         website.verify_login(self,sel,testvars.gmailuser)
         # logout
         website.SiteLogout(self,sel)             
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
  #      self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors) 


if __name__ == "__main__":
    unittest.main()
