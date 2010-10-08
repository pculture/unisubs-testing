from selenium import selenium

import unittest
import os
import time
import re
import sys
import codecs
import selvars
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class subgroup_test(unittest.TestCase):
    """Subgroup 69: Widget functionality tests using the site demo.

    Litmus Subgroup 69 - Demo Wiget UI tests
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        testid = self.id()
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://staging.universalsubtitles.org" )
        self.selenium.start()

    def test_382(self):
        """Login from widget using gmail account.

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
        website.verify_login(self,sel,testvars.gmailuser)
        # logout
        website.SiteLogout(self,sel)


          
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
#        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors) 


if __name__ == "__main__":
    unittest.main()
