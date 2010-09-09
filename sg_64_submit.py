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
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"] )
        self.selenium.start()

# The test cases of the subgroup.


    def test_469(self):
        """
        Tests submission of blip.tv video subtitle and translation.
        http://litmus.pculture.org/show_test.cgi?id=469
        """
        print "starting 469 blip.tv submit video"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        ext_list = ("flv","mpeg4", "mov", "ogg", "wmv")
        for x in ext_list:
            vid_url = offsite.get_blip_video_url(self,file_type=x)
            # Submit Video
            sel.open("/logout/?next=/")
            website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
            website.submit_video(self,sel,vid_url)
            # Verify embed and player
            website.verify_submitted_video(self,sel,vid_url,embed_type="flow")
            # Start sub widget
            website.start_sub_widget(self,sel)
            # Transcribe
            widget.transcribe_video(self,sel,subtextfile)
            # Sync
            widget.sync_video(self,sel,subtextfile,6,8)
            # Review
            widget.edit_text(self,sel,subtextfile)
            sel.click(testvars.WidgetUI["Next_step"])
            mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Close_widget"])
            sel.click(testvars.WidgetUI["Close_widget"])
            mslib.wait_for_element_present(self,sel,"css=.mirosubs-link")
            sel.click("css=.mirosubs-link:contains(\"Submit subtitles\")")

      




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





 
