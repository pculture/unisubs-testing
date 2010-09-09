from selenium import selenium
import unittest
import time
import sys
import os
import mslib
import website
import widget
import offsite
import testvars


class subgroup_78(unittest.TestCase):
    """
    Litmus Subgroup 64 - offsite subwidget:
        Tests designed to exercise the subtitle widget embedded
        in sites external to universalsubtitles.org (live, dev or staging)  
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, "http://pculture.org/mirosubs_tests/")
        self.selenium.start()

# The test cases of the subgroup.


    def test_369(self):
        """
        Tests YouTube video embedded in offsite widget
        http://litmus.pculture.org/show_test.cgi?id=389
        """
        print "starting 369 youtube widget test"
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        offsite.start_youtube_widget_null(self,sel)
        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,6,8)
        # Review
        widget.edit_text(self,sel,subtextfile)

      

    def test_370(self):
        """
        Tests ogg video embedded in offsite widget
        http://litmus.pculture.org/show_test.cgi?id=370
        """
        print "starting 370 - ogg widget test"
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        offsite.start_ogg_widget_null(self,sel)

        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,5,5)
        # Review
        widget.edit_text(self,sel,subtextfile)




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





 
