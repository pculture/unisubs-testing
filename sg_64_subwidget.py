from selenium import selenium
import unittest
import time
import sys
import mslib
import website
import widget
import offsite
import testvars


class subgroup_64(unittest.TestCase):
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
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The test cases of the subgroup.


    def test_369(self):
        """
        Tests YouTube video embedded in offsite widget
        http://litmus.pculture.org/show_test.cgi?id=389
        """
        print "369 starting youtube widget test"
        sel = self.selenium
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt"
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
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt"
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        offsite.start_ogg_widget_null(self,sel)

        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,5,5)
        # Review
        widget.edit_text(self,sel,subtextfile)


      
    def test_376(self):
        """Test demo widget not logged in
        http://litmus.pculture.org/show_test.cgi?id=376
        """
        print "starting 376 demo forced login"
        #FIX ME - this test probably belongs in subgroup 69, demo UI
        
        sel = self.selenium
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"OctopusGarden.txt"
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(testvars.MSTestVariables["Site"] +"logout")
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)        
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
        widget.site_login_auth(self,sel)
        self.failUnless(sel.is_element_present(testvars.WidgetUI["Translate_now_button"]))
        
        #Finish up by logging out
        print "logging out from site"
        website.SiteLogout(self,sel)

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





 
