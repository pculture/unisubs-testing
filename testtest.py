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

    def test_408(self):
        """
        Tests Back To Typing link in Step 2 Sync
        http://litmus.pculture.org/show_test.cgi?id=408
        """
        print "starting testcase 408"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        # start demo and proceed to step 2 and sync subs
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile,step="Stop")
        # go back to typing step
        widget.back_step(self,sel)
        # verify step 1 display and subs
        widget.steps_display(self,sel,1)
        widget.verify_sub_text(self,sel,subtextfile)     

                         
        
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
