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


    def test_412(self):
        """
        Tests modifying times by holding down then releasing down arrow
        on Step 3 Review
        http://litmus.pculture.org/show_test.cgi?id=412
        """
        print "starting testcase 412"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile,start_delay=5, sub_int=2)
        #on Step 3 resync video times
#        widget.hold_down_delay_sub(self,sel,subtextfile)       
                         
        
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
