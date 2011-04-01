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

class subgroup_78_pagedemo(unittest.TestCase):
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
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://dev.universalsubtitles.org"))
        self.selenium.start()
        self.session = self.selenium.sessionId
        self.selenium.set_timeout(testvars.timeout)
        
   
# The test cases of the subgroup.

    def test_684(self):
        """Pagedemo New York Times video 1 - sub position on playback.
        Open the testpage
        Start Playback
        Verify subs are in the correct position on the video.
        
        http://litmus.pculture.org/show_test.cgi?id=684
        """
        sel = self.selenium

        #test 1st video on the page
        testpage = "/pagedemo/nytimes_youtube_embed"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)
        

        #test 2nd video on the page
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)

    def test_688(self):
        """Pagedemo New York Times video 1 - translation playback
        
        http://litmus.pculture.org/show_test.cgi?id=688
        """
        test_id = 688
        sel = self.selenium
        testpage = "/pagedemo/nytimes_youtube_embed"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
#        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].click()') should be this when implemented to be sure correct video
        sel.click("css=div.mirosubs-dropdown div ul li:contains('100%')")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')       
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)





    def test_689(self):
        """Pagedemo New York Times video 1 - edit original subs
        
        http://litmus.pculture.org/show_test.cgi?id=689
        """
        test_id = 689
        sel = self.selenium
        testpage = "/pagedemo/nytimes_youtube_embed"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
        sel.click(testvars.WebsiteUI['AddSubtitles_menuitem'])
#        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].click()') should be this when implemented to be sure correct video
        edit_original_subs(self,sel)
        widget.goto_step(self,sel,step="2")
        widget.resync_video(self,sel,subtextfile)
        widget.submit_sub_edits(self,sel,offsite=True)

    def test_690(self):
        """Pagedemo New York Times video 1 - translate original
        
        http://litmus.pculture.org/show_test.cgi?id=690
        """
        test_id = 690
        sel = self.selenium
        testpage = "/pagedemo/nytimes_youtube_embed"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
        sel.click(testvars.WebsiteUI['AddSubtitles_menuitem'])
#        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].click()') should be this when implemented to be sure correct video
        translate_original(self,sel) # selects Croatian as the new language by default
        widget.edit_translation(self,sel,subtextfile)
        widget.submit_sub_edits(self,sel,offsite=True)
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
        
        sel.click("css=div.mirosubs-dropdown div ul li:contains('Croatian')")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')       
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        

    def test_691(self):
        """Pagedemo New York Times video 1 - forked the subs.
        
        http://litmus.pculture.org/show_test.cgi?id=691
        """
        test_id = 691
        sel = self.selenium
        testpage = "/pagedemo/nytimes_youtube_embed"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
        sel.click(testvars.WebsiteUI['AddSubtitles_menuitem'])
#        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].click()') should be this when implemented to be sure correct video
        new_fork(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self, sel, subtextfile)
        widget.site_login_from_widget_link(self,sel)
        #verify subs still present
        print "verifying subtitles are still present"
        sel.select_window("null")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
        widget.verify_sub_text(self,sel,subtextfile)
        widget.submit_sub_edits(self,sel,offsite=True)
        
        
        

    def test_685(self):
        """Pagedemo Blog Youtube Embed - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=685
        """
        test_id = 685
        sel = self.selenium
        testpage = "/pagedemo/pagedemo/blog_youtube_embed"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()

        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)



    def test_686(self):
        """Pagedemo Gapminder - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=686
        """
        test_id = 686
        sel = self.selenium
        testpage = "/pagedemo/gapminder"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()

        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)

    def test_687(self):
        """Pagedemo Gapminder - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=687
        """
        test_id = 687
        sel = self.selenium
        testpage = "pagedemo/khan_widgetizer"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()

        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)


          
##
##        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].play()')
##        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
##        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].pause()')
##        print "widget 1"
##        print sel.get_element_position_top("css=.mirosubs-captionSpan")
##        print sel.get_element_height("css=.mirosubs-captionSpan")

        
##        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getWidgetByURL("http://www.youtube.com/watch?v=O6ZFFDmeqZ8").play()')
##        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
##        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getWidgetByURL("http://www.youtube.com/watch?v=O6ZFFDmeqZ8").pause()')
##        print sel.get_element_position_top("css=.mirosubs-captionSpan")
##        print sel.get_element_height("css=.mirosubs-captionSpan")

            #            if int(sel.get_element_position_top("css=.mirosubs-captionSpan")) > 300




        
##        widget = sel.get_eval("this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()")
##        time.sleep(10)
##        sel.get_eval("this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].play()")
##        time.sleep(10)
##        sel.get_eval("this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].pause()")
##        widget = sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getWidgetByURL("").play()')
##        widget = sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getWidgetByURL("http://www.youtube.com/watch?v=O6ZFFDmeqZ8").click()')
                     
  
        
    

# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Check for an error page, then close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


def edit_original_subs(self,sel):
    """Start the Subtitle Widget using the Subtitle Me menu.

    This will handle the language choice for demo or submitted videos.
    skip is set to true by default and gets passed to widget.close_howto_video
    to prevent further how-to video displays.

    Pre-condition: On a page where the widget is present. Video with or without subs.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])        
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Select_language"])
    widget.select_video_language(self,sel,vid_lang='en',sub_lang='en')
    time.sleep(5)
    widget.close_howto_video(self,sel)
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")

def translate_original(self,sel):
    """Start the Subtitle Widget using the Subtitle Me menu.

    This will handle the language choice for demo or submitted videos.
    skip is set to true by default and gets passed to widget.close_howto_video
    to prevent further how-to video displays.

    Pre-condition: On a page where the widget is present. Video with or without subs.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])        
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Select_language"])
    widget.select_video_language(self,sel,vid_lang='en',sub_lang='hr')
    time.sleep(5)
    widget.close_howto_video(self,sel)
    mslib.wait_for_element_present(self,sel,"css=h2:contains('Editing Translation')")

def new_fork(self,sel):
    sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])        
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Select_language"])
    widget.select_video_language(self,sel,sub_lang='hr',from_lang='forkk')
    time.sleep(5)
    widget.close_howto_video(self,sel)
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")


def verify_caption_position(self,sel,caption_position):
    if int(caption_position) > 80:
            self.fail("captions are too high on the video")
    if int(caption_position) < 10:
            self.fail("captions are too lown on the video")

      

def make_new_subs(self,sel,vid_pos):

    print  ("no subs yet - making new ones")
    subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
    website.start_sub_widget(self,sel,vid_pos)
    # Transcribe
    widget.transcribe_video(self,sel,subtextfile)
    # Sync
    widget.sync_video(self,sel,subtextfile,6,8)
    # Review
    widget.edit_text(self,sel,subtextfile)


def edit_subs_and_revert(self,sel,test_page,vid_pos,vid_title):
        print "video has subs - going to editing then revert"
        sel.click(vid_pos)
        sel.click(testvars.WebsiteUI["Subhomepage_menuitem"])
        sel.wait_for_page_to_load(testvars.timeout)
        website.store_subs(self,sel,modify=True)
        orig_rev = website.get_current_rev(self,sel)
        print "starting revision is: "+str(orig_rev)
        subtextfile = "subs.txt"
        sel.open(test_page)
        mslib.wait_for_element_present(self,sel,vid_pos)
        website.start_sub_widget(self,sel,vid_pos)
        widget.goto_step(self,sel,"3")
        widget.edit_text(self,sel,subtextfile)
        widget.site_login_from_widget_link(self,sel)
        widget.submit_sub_edits(self,sel,offsite=True)
        mslib.wait_for_element_present(self,sel,testvars.offsite_goto_subs)
        sel.click(testvars.offsite_goto_subs)
        sel.wait_for_page_to_load(testvars.timeout)
        print " * verify edits"
        mslib.wait_for_element_present(self,sel,testvars.video_video_info)
        self.assertEqual("sub_writer edited English subtitles for "+vid_title, sel.get_text("css=tr td:nth-child(1)"))
        sel.click("css=tr td:nth-child(1) > a:contains('English subtitles')")
        sel.wait_for_page_to_load(testvars.timeout)
        sel.click(testvars.history_tab)
        mslib.wait_for_element_present(self,sel,testvars.video_compare_revisions)

        rev_num = orig_rev.lstrip('#')
        website.check_the_box(self,sel,2) #check the box
        new_rev = int(rev_num) + 1
        sel.click(testvars.video_compare_revisions)
        sel.wait_for_page_to_load(testvars.timeout)
        print " * comparing revisions and rolling back to original"
        website.verify_compare_revisions(self,sel,str(rev_num),str(new_rev),rollback=True)
        sel.click(testvars.transcripts_tab)
        website.verify_subs(self,sel,"subs.txt")   

if __name__ == "__main__":
    unittest.main()

 
