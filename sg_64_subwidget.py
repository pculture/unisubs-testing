# Open a youtube video and walk through the subtitle widget


from selenium import selenium
import unittest, time, re, sys
import mslib, website, widget, testvars

# ----------------------------------------------------------------------


class tc_369(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_youtube_full_subtitle(self):
        sel = self.selenium

        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        # Submit Video
        website.start_new_video_sub(self,sel,"http://www.youtube.com/watch?v=CUFcfXgW_dQ")

        # Transcribe
        widget.transcribe_video(self,sel,testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt")

        # Sync

        widget.sync_video(self,sel,testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt",8)

        # Review
        widget.review_time_shift_sync_hold(self,sel,testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt")
        widget.review_edit_text(self,sel,testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt")
        
        
        sel.click(testvars.WidgetUI["Next_step"])
        
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
    def test_ogg_full_subtitle(self):
        sel = self.selenium

        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        # Submit Video
        website.start_new_video_sub(self,sel,"http://pculture.org/mirosubs_tests/octopus_garden.ogg")

        # Transcribe
        widget.transcribe_video(self,sel,testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt")

        # Sync

        widget.sync_video(self,sel,testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt",8)

        # Review
        widget.review_time_shift_sync_hold(self,sel,testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt")
        widget.review_edit_text(self,sel,testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt")
        
        
        sel.click(testvars.WidgetUI["Next_step"])
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()





 
