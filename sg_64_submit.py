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
        self.session = self.selenium.sessionId
        if selvars.set_sauce() == True:
            print "sauce job result: http://saucelabs.com/jobs/"+str(self.session)
            


## The test cases of the subgroup.


    def test_469(self):
        """Submit flowplayer embedded videos from blip.tv.

        Tests submission of blip.tv video non-html5 subtitle and translation.
        http://litmus.pculture.org/show_test.cgi?id=469
        """
        print "starting 469 blip.tv submit embedded video"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        ext_list = ("flv",
                    #"mpeg4", "mov"
                    )
        vid_url = None
        for x in ext_list:
            try:
                print "getting a video url from blip, format: "+ x
                vid_url = offsite.get_blip_video_url(self,file_type=x)
                # Submit Video
                print "submitting the video"
                website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
                website.submit_video(self,sel,vid_url)
                # Verify embed and player
                print "verifying embed and video player"
                website.verify_submitted_video(self,sel,vid_url,embed_type="flow")
                # Start sub widget
                print "starting sub widget"
                website.start_sub_widget(self,sel)
                # Transcribe
                print "starting transcribe"
                widget.transcribe_video(self,sel,subtextfile)
                # Sync
                print "starting sync"
                widget.sync_video(self,sel,subtextfile,3,4)
                # Review
                print "starting review"
  #              widget.edit_text(self,sel,subtextfile)
                widget.submit_sub_edits(self,sel)
            except:
                self.verificationErrors.append("error submitting "+ str(x)+ " video: "+str(vid_url))
                # check for Site Error notification and submit
                
        
                
    def test_532(self):
        """Submit html5 videos from blip.tv.

        Tests submission of blip.tv video non-html5 subtitle and translation.
        http://litmus.pculture.org/show_test.cgi?id=532
        """
        print "starting 469 blip.tv submit html5 video"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        ext_list = ("ogv",)
        vid_url = None
        for x in ext_list:
            try:
                print "submitting a blip video, format: "+ x
                vid_url = offsite.get_blip_video_url(self,file_type=x)
                # Submit Video
                website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
                website.submit_video(self,sel,vid_url)
                # Verify embed and player
                print "verifying embed and video player"
                website.verify_submitted_video(self,sel,vid_url,embed_type="html5")
                # Start sub widget
                print "starting sub widget"
                website.start_sub_widget(self,sel)
                # Transcribe
                print "starting transcribe"
                widget.transcribe_video(self,sel,subtextfile)
                # Sync
                print "starting sync"
                widget.sync_video(self,sel,subtextfile,3,4)
                # Review
                print "starting review"
                widget.submit_sub_edits(self,sel)
            except:
                self.verificationErrors.append("error submitting "+ str(x)+ " video: "+str(vid_url))
                # check for Site Error notification and submit
                


    def test_533(self):
        """Submit and subtitle vimeo videos.

        http://litmus.pculture.org/show_test.cgi?id=533
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        
        vid_url = offsite.get_vimeo_video_url(self)
        # Submit Video
        print "logging in and submitting video"
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        website.submit_video(self,sel,vid_url)
        # Verify embed and player
        print "verifying embed"
        website.verify_submitted_video(self,sel,vid_url,embed_type="vimeo")
        # Start sub widget
        print "starting sub widget"
        website.start_sub_widget(self,sel)
        # Transcribe
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile,3,4)
        # Review
        print "review step - just submitting video"
        widget.submit_sub_edits(self,sel)

    def test_534(self):
        """Submit and subtitle youtube videos.

        http://litmus.pculture.org/show_test.cgi?id=534
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        print "submitting a youtube video"
        vid_url = offsite.get_youtube_video_url(self)
        # Submit Video
        print ("logging in and submitting video")
        website.submit_video(self,sel,vid_url)
        # Verify embed and player
        print ("verifying embed")
        website.verify_submitted_video(self,sel,vid_url,embed_type="youtube")
        # Start sub widget
        print ("starting sub widget")
        website.start_sub_widget(self,sel)
        # Transcribe
        print ("transcribing video")
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print ("syncing video")
        widget.sync_video(self,sel,subtextfile,3,4)
        # Review
        print ("review step - just submitting video")
        widget.submit_sub_edits(self,sel)

         
    def test_538(self):
        """Submit and subtitle dailymotion videos.

        http://litmus.pculture.org/show_test.cgi?id=538
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        print "submitting a dailymotion video, format: "
        vid_url = offsite.get_dailymotion_video_url(self)
        # Submit Video
        print "logging in and submitting video"
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        website.submit_video(self,sel,vid_url)
        # Verify embed and player
        print "verifying embed"
        website.verify_submitted_video(self,sel,vid_url,embed_type="dailymotion")
        # Start sub widget
        print "starting sub widget"
        time.sleep(5)
        website.start_sub_widget(self,sel)
        # Transcribe
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile,3,4)
        # Review
        print "review step - just submitting video"
        widget.submit_sub_edits(self,sel)


    def test_376(self):
        """Widget requires login to submit subtitles.

        http://litmus.pculture.org/show_test.cgi?id=376 .

               
        """
                
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        website.SiteLogout(self,sel)
        # Submit Video
        website.submit_video(self,sel,"http://www.youtube.com/watch?v=KakZkh9Iu7U&feature=")
        website.start_sub_widget(self,sel,login=False)        
        # Check message in transcribe step
        widget.verify_login_message(self,sel)
        widget.transcribe_video(self,sel,subtextfile)
        
        # Check message in sync step
        widget.verify_login_message(self,sel)
        widget.sync_video(self,sel,subtextfile,2,2)

        # Check message in review step and click done
        widget.verify_login_message(self,sel)
        sel.click(testvars.WidgetUI["Next_step"])
        self.failUnless(sel.is_element_present("css=.mirosubs-modal-login"))
        sel.click("css=.mirosubs-log")
        #Login
        widget.site_login_auth(self,sel)
        sel.select_window("null")
        time.sleep(3)
        if sel.is_element_present(testvars.WidgetUI["Must_Login"]):
            self.fail("User not correctly logged in.")
        self.assertTrue(sel.is_element_present(testvars.WidgetUI["Next_step"]),"Done button not found, maybe widget not redisplayed after login")
        sel.click(testvars.WidgetUI["Next_step"])
        widget.set_subs_complete(self,sel)
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"]) 
        print "logging out from site"
        website.SiteLogout(self,sel)



# Close the browser, log errors, perform cleanup
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        
        #give it back the session id in case it's lost it
        self.selenium.sessionId = self.session
        #Check for an error page, then close the browser
        try:
            website.handle_error_page(self,self.selenium,self.id())
        finally:
            self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)
      


if __name__ == "__main__":
    unittest.main()





 
