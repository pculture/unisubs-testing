# Open a youtube video and walk through the subtitle widget


from selenium import selenium
import unittest, time, re, sys
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class tc_369(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_youtube_offsite_subtitle(self):
        sel = self.selenium
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt"
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        offsite.start_youtube_widget_null(self,sel)
        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)

        # Sync

        widget.sync_video(self,sel,subtextfile,6,8)

        # Review
        widget.review_time_shift_sync_hold(self,sel,subtextfile,7,5)
        widget.review_edit_text(self,sel,subtextfile)
      
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_370(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_ogg_offsite_subtitle(self):
        sel = self.selenium
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt"
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        offsite.start_ogg_widget_null(self,sel)

        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)

        # Sync

        widget.sync_video(self,sel,subtextfile,5,5)

        # Review
        widget.review_time_shift_sync_hold(self,sel,subtextfile,8,4)
        widget.review_edit_text(self,sel,subtextfile)
      
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_376(unittest.TestCase):

# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_demo_not_logged_in(self):
        sel = self.selenium
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt"
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(testvars.MSTestVariables["Site"] +"logout")
        sel.open(testvars.MSTestVariables["Site"] +"demo")
        website.start_demo(self,sel)
        
        # Check message in transcribe step
        widget.verify_login_message(self,sel)
        widget.transcribe_video(self,sel,subtextfile)
        
        # Check message in sync step
        widget.verify_login_message(self,sel)
        widget.sync_video(self,sel,subtextfile,2,2)

        # Check message in review step and click done
        widget.verify_login_message(self,sel)
        sel.click(testvars.WidgetUI["Next_step"])
        self.assertEqual("In order to finish and save your work, you need to log in.", sel.get_alert())
        #Login
        sel.click(".css=.mirosubs-log")
        mslib.wait_for_element_present(self,sel,"id_username")
        sel.type("id_username", testvars.siteuser)
        sel.type("id_password", testvars.passw)
        sel.click("//button[@value='login']")
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        
        sel.click(testvars.WidgetUI["Video_playPause"])
        for line in open(subtextfile):
            mslib.wait_for_element_present(self,sel,"css=.mirosubs.captionDiv:contains(subtext)")

        #Finish up by logging out
        sel.open(testvars.MSTestVariables["Site"] +"logout")        
      
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()





 
