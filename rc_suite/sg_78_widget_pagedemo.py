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
    Litmus Subgroup 78 - offsite subwidget embedded in pagedemo:
        Tests designed to mimic important partner sites css and widget behavior
        see /pagedemo/index for sites to test.  
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
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
        widget.starter_dialog_edit_orig(self,sel)
        widget.goto_step(self,sel,step="2")
        widget.edit_text(self,sel,subtextfile)
        #Login

        if sel.is_element_present("css=div div.unisubs-needLogin a"):
            sel.click("css=div div.unisubs-needLogin a")
            mslib.wait_for_element_present(self,sel,"css=.unisubs-modal-login")
            sel.click("css=.unisubs-log")
            widget.site_login_auth(self,sel)
            sel.select_window("null")
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
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
        time.sleep(5)
        widget.open_starter_dialog(self,sel)
        widget.starter_dialog_translate_from_orig(self,sel,to_lang='pl')
        widget.edit_translation(self,sel,subtextfile)
        
        

    def test_691(self):
        """Pagedemo New York Times video 1 - forked the subs and create a fresh set of captions in hr lang.
        
        http://litmus.pculture.org/show_test.cgi?id=691
        """
        test_id = 691
        sel = self.selenium
        testpage = "/pagedemo/nytimes_youtube_embed"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().unisubs.widget.Widget.getAllWidgets()[0].openMenu()')
        widget.open_starter_dialog(self,sel)
        widget.starter_dialog_fork(self,sel,to_lang='hr')
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self, sel, subtextfile)
        widget.site_login_from_widget_link(self,sel)
        #verify subs still present
        print "verifying subtitles are still present"
        sel.select_window("null")
        mslib.wait_for_element_present(self,sel,"css=.unisubs-titlesList")
        widget.verify_sub_text(self,sel,subtextfile)
        if sel.is_element_present("css=.unisubs-modal-login"): #Login
            sel.click("css=.unisubs-log")
            widget.site_login_auth(self,sel)
            sel.select_window("null")
        widget.submit_sub_edits(self,sel,offsite=True)
        


    

# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Check for an error page, then close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)

def verify_caption_position(self,sel,caption_position):
    if int(caption_position) > 80:
            self.fail("captions are too high on the video")
    if int(caption_position) < 10:
            self.fail("captions are too lown on the video")

      

if __name__ == "__main__":
    unittest.main()

 
