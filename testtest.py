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


    def test_414(self):
        """Widget Step 3, click time arrows to modify time.
        
        http://litmus.pculture.org/show_test.cgi?id=414
        """
        print "starting testcase 414"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile)
        #on Step 3 resync video times
        widget.click_time_shift_arrows(self,sel,subtextfile) 


          
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
