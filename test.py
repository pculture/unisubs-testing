# test sandbox

from selenium import selenium
import unittest, time, re, sys
import mslib, website, widget, offsite, testvars

#----------------------------------------------------------------------


class tc_408(unittest.TestCase):
    
# Open the desired browser and set up the test
 # Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost,4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step2_back_to_typing(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        # start demo and proceed to step 2 and sync subs
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile, step="Stop")
        widget.verify_sub_text(self,sel,subtextfile)
        
        

# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()
