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

class subgroup_94_pagedemo(unittest.TestCase):
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
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), selvars.set_site()))
        self.selenium.start()
        self.session = self.selenium.sessionId
        self.selenium.set_timeout(testvars.timeout)
        
   
# The test cases of the subgroup.

   

    def test_687(self):
        """Pagedemo Khan Widgetizer - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=687
        """
        test_id = 687
        sel = self.selenium
        testpage = "/pagedemo/khan_widgetizer"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Current_playing_offsite"])
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height(testvars.WidgetUI["Current_playing_offsite"])
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)

    def test_701(self):
        """Pagedemo Khan Widgetizer async - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=687
        """
        test_id = 701
        sel = self.selenium
        testpage = "/pagedemo/async_widgetizer"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        sel.click("link=Widgetize it!")
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Current_playing_offsite"])
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height(testvars.WidgetUI["Current_playing_offsite"])
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)

    def test_739(self):
        """Pagedemo Boing-Boing Widgetizer - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=739
        Testing with 3rd video on the test page, Reefer madness.
        """
        test_id = 739
        sel = self.selenium
        testpage = "/boingboing_widgetizer"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[2].play()')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Current_playing_offsite"])
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[2].pause()')
        caption_position =  sel.get_element_height(testvars.WidgetUI["Current_playing_offsite"])
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)

  
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Check for an error page, then close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


class subgroup_94_mcsite(unittest.TestCase):
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

    def test_738(self):
        """widgetizer on MC site youtube iframe.
        http://litmus.pculture.org/show_test.cgi?id=738
        Video with widget embedded on Miro Community test page.
        """
        print self.shortDescription()
        sel = self.selenium
        mc_page = "widgetizer_tests"
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


    def test_741(self):
        """widgetizer on MC site html5 mp4.
        http://litmus.pculture.org/show_test.cgi?id=741
        Video with widget embedded on Miro Community test page.
        """
        print self.shortDescription()
        sel = self.selenium
        mc_page = "widgetizer_tests"
        test_page = selvars.set_unisubs_mc_page(self,mc_page)
        sel.open(test_page)
        sel.wait_for_page_to_load(testvars.timeout)
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(3)
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[1].openMenu()')
        time.sleep(2)
        if sel.is_element_present(testvars.WebsiteUI["AddSubtitles_menuitem"]) == True:
            print "has subtitles - edit and revert"
            subtextfile = "subs.txt"
            orig_rev = store_subs(self,sel)
            sel.open(test_page)
            sel.wait_for_page_to_load(testvars.timeout)
            mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
            time.sleep(3)
            sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[1].openMenu()')
            widget.starter_dialog_edit_orig(self,sel)
            edit_subs(self,sel,orig_rev,subtextfile)          
        else:
            make_new_subs(self,sel,subtextfile)


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
    widget.sync_video(self,sel,subtextfile,2,3)
    #Login
    time.sleep(3)
    sel.click("css=div.unisubs-needLogin a")
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


def verify_submenu_present(self,sel):
    sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
    time.sleep(2)
    self.failUnless(sel.is_element_present(testvars.WebsiteUI["Subhomepage_menuitem"]))


     

if __name__ == "__main__":
    unittest.main()

 
