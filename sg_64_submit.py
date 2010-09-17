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
import selvars
import json
import sauce_auth


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
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), selvars.set_site() )
        self.selenium.start()

## The test cases of the subgroup.


    def test_469_blip_submit_embedded(self):
        """Submit videos from blip.tv.

        Tests submission of blip.tv video non-html5 subtitle and translation.
        http://litmus.pculture.org/show_test.cgi?id=469
        """
        print "starting 469 blip.tv submit embedded video"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        ext_list = ("flv", "mpeg4", "mov")
        for x in ext_list:
            try:
                print "submitting an embedded blip video, format: "+ x
                vid_url = offsite.get_blip_video_url(self,file_type=x)
                # Submit Video
                website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
                website.submit_video(self,sel,vid_url)
                # Verify embed and player
                website.verify_submitted_video(self,sel,vid_url,embed_type="flow")
                # Start sub widget
                website.start_sub_widget(self,sel)
                # Transcribe
                widget.transcribe_video(self,sel,subtextfile)
                # Sync
                widget.sync_video(self,sel,subtextfile,3,4)
                # Review
                widget.edit_text(self,sel,subtextfile)
                sel.click(testvars.WidgetUI["Next_step"])
            except:
                print "error testing submit video format: " + x
                
    def test_469_blip_submit_html5(self):
        """Submit videos from blip.tv.

        Tests submission of blip.tv video non-html5 subtitle and translation.
        http://litmus.pculture.org/show_test.cgi?id=469
        """
        print "starting 469 blip.tv submit html5 video"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        ext_list = ("ogg", "ogv")
        for x in ext_list:
            try:
                print "submitting a blip video, format: "+ x
                vid_url = offsite.get_blip_video_url(self,file_type=x)
                # Submit Video
                website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
                website.submit_video(self,sel,vid_url)
                # Verify embed and player
                website.verify_submitted_video(self,sel,vid_url,embed_type="html5")
                # Start sub widget
                website.start_sub_widget(self,sel)
                # Transcribe
                widget.transcribe_video(self,sel,subtextfile)
                # Sync
                widget.sync_video(self,sel,subtextfile,3,4)
                # Review
                widget.edit_text(self,sel,subtextfile)
                sel.click(testvars.WidgetUI["Next_step"])
            except:
                print "error testing submit video format: " + x


    def test_vimeo_submit(self):
        """Submit and subtitle vimeo videos.

        http://litmus.pculture.org/show_test.cgi?id=469
        """
        print "starting 999 vimeo.com submit video"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        print "submitting a vimeo video, format: "
        vid_url = offsite.get_vimeo_video_url(self)
        # Submit Video
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        website.submit_video(self,sel,vid_url)
        # Verify embed and player
        website.verify_submitted_video(self,sel,vid_url,embed_type="vimeo")
        # Start sub widget
        website.start_sub_widget(self,sel)
        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,3,4)
        # Review
 #       widget.edit_text(self,sel,subtextfile, "vimeo video text edit")
        sel.click(testvars.WidgetUI["Next_step"])
           





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





 
