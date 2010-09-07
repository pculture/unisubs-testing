# Open a youtube video and walk through the subtitle widget


from selenium import selenium
import unittest, time, re, sys
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class tc_999(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_ogg_offsite_translate_immediately(self):
        sel = self.selenium
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"womoz_fosdem.txt"
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("http://pculture.org/mirosubs_tests/translate_immediately.html")
        website.start_sub_widget(self,sel)
        
        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)

        # Sync
        widget.sync_video(self,sel,subtextfile,2,2)

 #       widget.sync_video(self,sel,subtextfile)

        # Review
        sel.click(testvars.WidgetUI["Next_step"])
      
        
### Close the browser, log errors, perform cleanup 
##    def tearDown(self):
###        self.selenium.stop()
### the command on the previous line should close the browser
##        self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()





 
