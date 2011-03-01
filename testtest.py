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
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), "safari", "http://staging.universalsubtitles.org" )
        self.selenium.start()
        self.session = self.selenium.sessionId


    def test_388(self):
        """Widget Step 2, edit subtitle text from step 1.
        
        Tests smalls, caps, spaces, and non-ascii chars
        http://litmus.pculture.org/show_test.cgi?id=388
        """
        print "starting testcase 388"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile,step="Stop")
                       
        #edit subtitles
        print "verifying subtitles are still present"
        widget.edit_text(self,sel,subtextfile)
        # make it french
##        widget.edit_text(self,sel,subtextfile,new_text=testvars.eels_fr)
##        #make it japanese
##        widget.edit_text(self,sel,subtextfile,new_text=testvars.eels_jp)  
          
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
        self.selenium.sessionId = self.session
        print self.selenium.sessionId
 #       self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors) 


if __name__ == "__main__":
    unittest.main()
