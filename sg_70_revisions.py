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



class subgroup_70(unittest.TestCase):
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

    def test_485(self):
        """Revisions - display history info for original subtitle language.

        http://litmus.pculture.org/show_test.cgi?id=485
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        print "submitting a youtube video, format: "
        vid_url = offsite.get_youtube_video_url(self)
        # Submit Video
        print "logging in and submitting video"
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        website.front_page_submit(self,sel,vid_url)
        # Verify embed and player
        print "verifying embed"
        website.verify_submitted_video(self,sel,vid_url,embed_type="youtube")
        # Start sub widget
        print "starting sub widget"
        website.start_sub_widget(self,sel)
        # Transcribe
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile,8,6)
        # Review
        print "review step - just submitting video"
        sel.click(testvars.WidgetUI["Next_step"])
        mslib.wait_for_element_present(self,sel,testvars.video_video_info)
        website.verify_subs(self,sel,subtextfile)
        # Click History tab
        website.verify_latest_history(self,sel,rev="#0",user="sub_writer",time="100%",text="100%")


    def test_486a(self):
        """Revisions - edit subtitles timing and verify in history table.

        http://litmus.pculture.org/show_test.cgi?id=485
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        print "submitting a youtube video, format: "
        vid_url = offsite.get_youtube_video_url(self)
        # Submit Video
        print "logging in and submitting video"
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        website.front_page_submit(self,sel,vid_url)
        # Verify embed and player
        print "verifying embed"
        website.verify_submitted_video(self,sel,vid_url,embed_type="youtube")
        # Start sub widget
        print "starting sub widget"
        website.start_sub_widget(self,sel)
        # Transcribe
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile,8,6)
        # Review
        print "review step - just submitting video"
        sel.click(testvars.WidgetUI["Next_step"])
        mslib.wait_for_element_present(self,sel,testvars.video_video_info)
        website.verify_subs(self,sel,subtextfile)
        sel.click(testvars.video_edit_subtitles)
        widget.close_howto_video(self,sel)
        widget.goto_step(self,sel,"2")
        widget.resync_video(self,sel,subtextfile)
        widget.submit_sub_edits(self,sel)
        # Click History tab
        website.verify_latest_history(self,sel,rev="#1",user="sub_writer",time="100%",text="0%")
                
    def test_487b(self):
        """Revisions - edit subtitles text and verify in history table.

        http://litmus.pculture.org/show_test.cgi?id=485
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        print "submitting a youtube video, format: "
        vid_url = offsite.get_youtube_video_url(self)
        # Submit Video
        print "logging in and submitting video"
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        website.front_page_submit(self,sel,vid_url)
        # Verify embed and player
        print "verifying embed"
        website.verify_submitted_video(self,sel,vid_url,embed_type="youtube")
        # Start sub widget
        print "starting sub widget"
        website.start_sub_widget(self,sel)
        # Transcribe
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile,8,6)
        # Review
        print "review step - just submitting video"
        sel.click(testvars.WidgetUI["Next_step"])
        mslib.wait_for_element_present(self,sel,testvars.video_video_info)
        website.verify_subs(self,sel,subtextfile)
        sel.click(testvars.video_edit_subtitles)
        widget.close_howto_video(self,sel)
        widget.goto_step(self,sel,"3")
        widget.edit_text(self,sel,subtextfile)
        widget.submit_sub_edits(self,sel)
        # Click History tab
        website.verify_latest_history(self,sel,rev="#1",user="sub_writer",time="0%",text="100%")
    

 

# Close the browser, log errors, perform cleanup
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        
        #Close the browser
 #       self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)
      


if __name__ == "__main__":
    unittest.main()





 
