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



class subgroup_78_pculture(unittest.TestCase):
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
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://pculture.org/"))
        self.selenium.start()
        self.session = self.selenium.sessionId
   
# The test cases of the subgroup.


    def test_369(self):
        """Subtitle Youtube video in offsite embed.
        
        http://litmus.pculture.org/show_test.cgi?id=369
        """
        print "starting 369 youtube widget test"
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(selvars.set_widget_null_page())
        mslib.wait_for_element_present(self,sel,"css=.left_column span.unisubs-tabTextchoose")
        website.start_sub_widget(self,sel,"css=.left_column span.unisubs-tabTextchoose")
        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,6,8)
        # Review
      

      

    def test_370(self):
        """Subtitle ogg video in offsite embed.
       
        http://litmus.pculture.org/show_test.cgi?id=370
        """
        print "starting 370 - ogg widget test"
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(selvars.set_widget_null_page())
        mslib.wait_for_element_present(self,sel,"css=.left_column span.unisubs-tabTextchoose")
        website.start_sub_widget(self,sel,"css=.left_column span.unisubs-tabTextchoose")

        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,5,5)
        # Review
   
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        # check for Site Error notification and submit
        website.handle_error_page(self,self.selenium,self.id())
        #Close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


##class subgroup_78_subtesting(unittest.TestCase):
##    """
##    Litmus Subgroup 78 - offsite subwidget:
##        Tests designed to exercise the subtitle widget embedded
##        in sites external to universalsubtitles.org (live, dev or staging)  
##    """
##    
### Open the desired browser and set up the test
##    def setUp(self):
##        """
##        Sets up run envirnment for selenium server
##        """
##        self.verificationErrors = []
##        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://subtesting.com/"))
##        self.selenium.start()
##        self.session = self.selenium.sessionId
##        self.selenium.set_timeout(testvars.timeout)
##        
##   
### The test cases of the subgroup.
##
##
##    def test_601(self):
##        """test 601 Widgetizer offsite on wordpress with youtube video.
##        
##        http://litmus.pculture.org/show_test.cgi?id=601
##
##        We are explicitly testing the Right-Wing Radio http://www.youtube.com/watch?v=HfuwNU0jsk0 on the page
##        """
##        test_id = 601
##        print self.shortDescription()
##        sel = self.selenium
##        test_page = (selvars.set_subtesting_wordpress_page(self,test_id))
##        sel.open(test_page)
##        sel.wait_for_page_to_load(testvars.timeout)
##        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
##        time.sleep(1)
##        if sel.is_element_present(testvars.WebsiteUI["AddSubtitles_menuitem"]) == True:
##            print "has subtitles - edit and revert"
##            subtextfile = "subs.txt"
##            orig_rev = store_subs(self,sel)
##            sel.open(test_page)
##            sel.wait_for_page_to_load(testvars.timeout)
##            mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
##            time.sleep(3)
##            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
##            widget.starter_dialog_edit_orig(self,sel)
##            edit_subs(self,sel,orig_rev,subtextfile)          
##        else:
##            make_new_subs(self,sel)
##
##    def test_622(self):
##        """test 622 widgetizer offsite wordpress in-page script element youtube
##        
##        http://litmus.pculture.org/show_test.cgi?id=622
##
##        We are explicitly testing the Right-Wing Radio Duck http://www.youtube.com/watch?v=HfuwNU0jsk0 on the page
##        """
##        test_id = 622
##        print self.shortDescription()
##        sel = self.selenium
##        test_page = (selvars.set_subtesting_wordpress_page(self,test_id))
##        sel.open(test_page)
##        sel.wait_for_page_to_load(testvars.timeout)
##        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
##        time.sleep(1)
##        if sel.is_element_present(testvars.WebsiteUI["AddSubtitles_menuitem"]) == True:
##            print "has subtitles - edit and revert"
##            subtextfile = "subs.txt"
##            orig_rev = store_subs(self,sel)
##            sel.open(test_page)
##            sel.wait_for_page_to_load(testvars.timeout)
##            mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
##            time.sleep(3)
##            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
##            widget.starter_dialog_edit_orig(self,sel)
##            edit_subs(self,sel,orig_rev,subtextfile)          
##        else:
##            make_new_subs(self,sel)


            
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Check for an error page, then close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


class subgroup_78_unisubs_mc(unittest.TestCase):
    """offsite widget on MC site.
    Litmus Subgroup 78 - offsite subwidget embedded in mc:
        Tests designed to exercise the subtitle widget embedded
        in sites external to universalsubtitles.org (live, dev or staging)  
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://universalsubtitles.mirocommunity.org/"))
        self.selenium.start()
        self.session = self.selenium.sessionId
        self.selenium.set_timeout(testvars.timeout)
        
   
# The test cases of the subgroup.




    def test_623(self):
        """offsite widget on MC site.
        video url: http://www.youtube.com/watch?v=FNEImAIM4L4
        http://litmus.pculture.org/show_test.cgi?id=623
        Video with widget embedded on Miro Community test page.
        """
        mc_page = "hunter"
        vid_pos = "css=p.pElementTest span span.unisubs-widget div.unisubs-videoTab a span.unisubs-tabTextchoose"
        vid_title = "hunter.s.thompson.avi"
        print self.shortDescription()
        sel = self.selenium
        test_page = selvars.set_unisubs_mc_page(self,mc_page)
        sel.open(test_page)
        sel.wait_for_page_to_load(testvars.timeout)
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(3)
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
        time.sleep(2)
        if sel.is_element_present(testvars.WebsiteUI["AddSubtitles_menuitem"]) == True:
            print "has subtitles - edit and revert"
            subtextfile = "subs.txt"
            orig_rev = store_subs(self,sel)
            sel.open(test_page)
            sel.wait_for_page_to_load(testvars.timeout)
            mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
            time.sleep(3)
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
            widget.starter_dialog_edit_orig(self,sel)
            edit_subs(self,sel,orig_rev,subtextfile)          
        else:
            make_new_subs(self,sel,subtextfile)
       
            
    def test_732(self):
        """vimeo offsite widget on MC site.
 
        http://litmus.pculture.org/show_test.cgi?id=732
        Vimeo Video with widget embedded on Miro Community test page.
        """
        mc_page = "embed_tests"
        vid_title = "The Sandwich Movie"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"732_vimeo.txt")
        print self.shortDescription()
        sel = self.selenium
        test_page = selvars.set_unisubs_mc_page(self,mc_page)
        sel.open(test_page)
        sel.wait_for_page_to_load(testvars.timeout)
        time.sleep(5)
        if sel.is_element_present("css=p.vimeo_new div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')"):
            sel.click("css=p.vimeo_new div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')")
        else:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')          
        make_new_subs(self,sel,subtextfile)
        #Playback Subs
        time.sleep(5)
        try:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].play()')
            mslib.wait_for_element_present(self,sel,"css=p.vimeo_new span.unisubs-captionSpan")
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].pause()')
            caption_position =  sel.get_element_height("css=p.vimeo_new span.unisubs-captionSpan")
            verify_caption_position(self,sel,caption_position)
        except:
            print "sub position playback failed"
            self.verificationErrors.append("sub playback / position test failed")
  
      
        
       
    def test_733(self):
        """youtube offsite embed - subtitle and playback
 
        http://litmus.pculture.org/show_test.cgi?id=733
        Vimeo Video with widget embedded on Miro Community test page.
        """
        mc_page = "embed_tests"
        vid_title = "Girl wakes up"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"733_youtube.txt")
        print self.shortDescription()
        sel = self.selenium
        test_page = selvars.set_unisubs_mc_page(self,mc_page)
        sel.open(test_page)
        sel.wait_for_page_to_load(testvars.timeout)
        time.sleep(5)
        if sel.is_element_present("css=p.youtube_subtitled div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')"):
            sel.click("css=p.youtube_subtitled div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')")
        else:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[1].openMenu()')          
        make_new_subs(self,sel,subtextfile)
        #Playback Subs
        time.sleep(5)
        try:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[1].play()')
            mslib.wait_for_element_present(self,sel,"css=p.youtube_subtitled span.unisubs-captionSpan")
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[1].pause()')
            caption_position =  sel.get_element_height("css=p.youtube_subtitled span.unisubs-captionSpan")
            verify_caption_position(self,sel,caption_position)
        except:
            print "sub position playback failed"
            self.verificationErrors.append("sub playback / position test failed")
  


    def test_734(self):
        """dailymotion offsite embed - subtitle and playback
 
        http://litmus.pculture.org/show_test.cgi?id=734
        Vimeo Video with widget embedded on Miro Community test page.
        """
        mc_page = "embed_tests"
        vid_title = "Ordaemonium"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"734_dm.txt")
        print self.shortDescription()
        sel = self.selenium
        test_page = selvars.set_unisubs_mc_page(self,mc_page)
        sel.open(test_page)
        sel.wait_for_page_to_load(testvars.timeout)
        time.sleep(5)
        if sel.is_element_present("css=p.dailymotion div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')"):
            sel.click("css=p.dailymotion div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')")
        else:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[2].openMenu()')          
        make_new_subs(self,sel,subtextfile)
        #Playback Subs
        time.sleep(5)
        try:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[2].play()')
            mslib.wait_for_element_present(self,sel,"css=p.dailymotion span.unisubs-captionSpan")
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[2].pause()')
            caption_position =  sel.get_element_height("css=p.dailymotion span.unisubs-captionSpan")
            verify_caption_position(self,sel,caption_position)
        except:
            print "sub position playback failed"
            self.verificationErrors.append("sub playback / position test failed")
    

    def test_735(self):
        """blip ogg embed - subtitle and playback
 
        http://litmus.pculture.org/show_test.cgi?id=735
        Blip ogg video with widget embedded on Miro Community test page.
        """
        mc_page = "embed_tests"
        vid_title = "Girl wakes up"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"735_blip.txt")
        print self.shortDescription()
        sel = self.selenium
        test_page = selvars.set_unisubs_mc_page(self,mc_page)
        sel.open(test_page)
        sel.wait_for_page_to_load(testvars.timeout)
        time.sleep(5)
        if sel.is_element_present("css=p.ogg div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')"):
            sel.click("css=p.ogg div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')")
        else:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[3].openMenu()')          
        make_new_subs(self,sel,subtextfile)
        #Playback Subs
        time.sleep(5)
        try:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[3].play()')
            mslib.wait_for_element_present(self,sel,"css=p.ogg span.unisubs-captionSpan")
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[3].pause()')
            caption_position =  sel.get_element_height("css=p.ogg span.unisubs-captionSpan")
            verify_caption_position(self,sel,caption_position)
        except:
            print "sub position playback failed"
            self.verificationErrors.append("sub playback / position test failed")
  

    def test_736(self):
        """blip flowplayer offsite embed - subtitle and playback
 
        http://litmus.pculture.org/show_test.cgi?id=736
        Blip Flowplayer Video with widget embedded on Miro Community test page.
        """
        mc_page = "embed_tests"
        vid_title = "Girl wakes up"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"736_blipflow.txt")
        print self.shortDescription()
        sel = self.selenium
        test_page = selvars.set_unisubs_mc_page(self,mc_page)
        sel.open(test_page)
        sel.wait_for_page_to_load(testvars.timeout)
        time.sleep(5)
        if sel.is_element_present("css=p.blip-flow div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')"):
            sel.click("css=p.blip-flow div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')")
        else:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[4].openMenu()')          
        make_new_subs(self,sel,subtextfile)
        #Playback Subs
        time.sleep(5)
        try:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[4].play()')
            mslib.wait_for_element_present(self,sel,"css=p.blip-flow span.unisubs-captionSpan")
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[4].pause()')
            caption_position =  sel.get_element_height("css=p.blip-flow span.unisubs-captionSpan")
            verify_caption_position(self,sel,caption_position)
        except:
            print "sub position playback failed"
            self.verificationErrors.append("sub playback / position test failed")
    


    def test_737(self):
        """flowplayer offsite embed - subtitle and playback
 
        http://litmus.pculture.org/show_test.cgi?id=737
        Flowplayer with widget embedded on Miro Community test page.
        """
        mc_page = "embed_tests"
        vid_title = "flow player test"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"737_flow.txt")
        print self.shortDescription()
        sel = self.selenium
        test_page = selvars.set_unisubs_mc_page(self,mc_page)
        sel.open(test_page)
        sel.wait_for_page_to_load(testvars.timeout)
        time.sleep(5)
        if sel.is_element_present("css=p.other-flow div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')"):
            sel.click("css=p.other-flow div.unisubs-videoTab a.unisubs-subtitleMeLink span.unisubs-tabTextchoose:contains('Subtitle Me')")
        else:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[5].openMenu()')          
        make_new_subs(self,sel,subtextfile)
        #Playback Subs
        time.sleep(5)
        try:
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[5].play()')
            mslib.wait_for_element_present(self,sel,"css=p.other-flow span.unisubs-captionSpan")
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[5].pause()')
            caption_position =  sel.get_element_height("css=p.other-flow span.unisubs-captionSpan")
            verify_caption_position(self,sel,caption_position)
        except:
            print "sub position playback failed"
            self.verificationErrors.append("sub playback / position test failed")
   



# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Check for an error page, then close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)

     

def make_new_subs(self,sel,subtextfile):
    print "make new subs"
    time.sleep(3)
    widget.starter_dialog_edit_orig(self,sel)
    # Transcribe
    widget.transcribe_video(self,sel,subtextfile)
    # Sync
    widget.sync_video(self,sel,subtextfile,1,2)
    time.sleep(3)
    #Login
    if sel.is_element_present("css=.unisubs-modal-login"): #Login
        sel.click("css=.unisubs-log")
        widget.site_login_auth(self,sel)
        sel.select_window("null")
    # Review
    widget.submit_sub_edits(self,sel,offsite=True)
    mslib.wait_for_element_present(self,sel,testvars.offsite_goto_subs)
    sel.click(testvars.offsite_goto_site)
    sel.wait_for_page_to_load(testvars.timeout)


def verify_caption_position(self,sel,caption_position):
    if int(caption_position) > 80:
            self.fail("captions are too high on the video")
    if int(caption_position) < 10:
            self.fail("captions are too lown on the video")



def store_subs(self,sel):
        """Go to main video page and store the existing subs.

        """
        print "video has subs"
        sel.click(testvars.WebsiteUI["Subhomepage_menuitem"])
        sel.wait_for_page_to_load(testvars.timeout)
        website.store_subs(self,sel,modify=True,limit=True)
        orig_rev = website.get_current_rev(self,sel)
        print "starting revision is: "+str(orig_rev)
        return orig_rev

def edit_subs(self,sel,orig_rev,subtextfile):
        widget.goto_step(self,sel,"2")
        time.sleep(3)
        widget.edit_text(self,sel,subtextfile)
        widget.site_login_from_widget_link(self,sel)
        widget.submit_sub_edits(self,sel,offsite=True)
        mslib.wait_for_element_present(self,sel,testvars.offsite_goto_subs)
        sel.click(testvars.offsite_goto_subs)
        ###
        sel.wait_for_page_to_load(testvars.timeout)
        vid_title = sel.get_text(testvars.vid_title)
        print " * verify edits"
        mslib.wait_for_element_present(self,sel,testvars.video_video_info)
        history_text = sel.get_text("css=tr td:nth-child(1)")
        print history_text
        sel.click(testvars.video_original)
        mslib.wait_for_element_present(self,sel,testvars.history_tab)
        sel.click(testvars.history_tab)
        mslib.wait_for_element_present(self,sel,testvars.video_compare_revisions)


if __name__ == "__main__":
    unittest.main()

 
