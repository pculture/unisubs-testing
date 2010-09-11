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

    def test_398(self):
        """
        Tests Expert setting in Step 1 Typing
        http://litmus.pculture.org/show_test.cgi?id=398
        """
        print "starting testcase 398"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        #Type sub-text in the video, then wait stay on Step-1 screen
        widget.transcribe_video(self, sel, subtextfile, step="Stop")
        #verify that playback continues to the end
        while int(sel.get_element_width("css=.mirosubs-played")) != 250:
            self.failIf(sel.is_element_present(testvars.WidgetUI["Video_play_button"]))   

                         
        
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
