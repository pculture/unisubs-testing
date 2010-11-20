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
   
# The test cases of the subgroup.


    def stest_369(self):
        """Subtitle Youtube video in offsite embed.
        
        http://litmus.pculture.org/show_test.cgi?id=369
        """
        print "starting 369 youtube widget test"
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(selvars.set_widget_null_page())
        mslib.wait_for_element_present(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
        website.start_sub_widget(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,6,8)
        # Review
        widget.edit_text(self,sel,subtextfile)

      

    def stest_370(self):
        """Subtitle ogg video in offsite embed.
       
        http://litmus.pculture.org/show_test.cgi?id=370
        """
        print "starting 370 - ogg widget test"
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(selvars.set_widget_null_page())
        mslib.wait_for_element_present(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
        website.start_sub_widget(self,sel,"css=.left_column span.mirosubs-tabTextchoose")

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
        # check for Site Error notification and submit
        website.handle_error_page(self,self.selenium,self.id())
        #Close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


class subgroup_78_subtesting(unittest.TestCase):
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
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://subtesting.com/"))
        self.selenium.start()
   
# The test cases of the subgroup.


    def test_601(self):
        """Subtitle Youtube video in offsite Wordpress embed.
        
        http://litmus.pculture.org/show_test.cgi?id=601

        We are explicitly testing the Right-Wing Radio Duck in 1st position on the page
        """
        youtube_vid1 = "css=div:nth-child(3) > a span"
        print self.shortDescription()
        sel = self.selenium
        
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(selvars.set_subtesting_wordpress_page())
        mslib.wait_for_element_present(self,sel,"css=div:nth-child(3) > a span")
        if sel.get_text(youtube_vid1) == "Subtitle Me":
            print "no subs yet - making new ones"
            subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
            website.start_sub_widget(self,sel,youtube_vid1)
            # Transcribe
            widget.transcribe_video(self,sel,subtextfile)
            # Sync
            widget.sync_video(self,sel,subtextfile,6,8)
            # Review
            widget.edit_text(self,sel,subtextfile)
        else:
            print "has subs - going to editing then revert"
            sel.click(testvars.WebsiteUI["Subhomepage_menuitem"])
            sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
            website.store_subs(self,sel)
            orig_rev = website.get_current_rev(self,sel)
            subtextfile = "subs.txt"
            sel.open(selvars.set_subtesting_wordpress_page())
            mslib.wait_for_element_present(self,sel,"css=div:nth-child(3) > a span")
            website.start_sub_widget(self,sel,youtube_vid1)
            widget.goto_step(self,sel,"3")
            widget.edit_text(self,sel,subtextfile)
            widget.SiteLogin(self,sel)
            widget.submit_sub_edits(self,sel)
            mslib.wait_for_element_present(testvars.video_video_info)
            self.assertEqual("PCF Sub-writer edited English subtitles for Right-Wing Radio Duck", sel.get_text("css=tr td:nth-child(1)"))
            sel.click("css=tr td:nth-child(1) > a:contains('English subtitles')")
            sel.click(testvars.history_tab)
            mslib.wait_for_element_present(self,sel,testvars.video_compare_revisions)
            sel.click("td a:contains('"+ orig_rev+"')")
            sel.click(testvars.video_compare_revisions)
            mslib.wait_for_element_present(self,sel,testvars.rev_rollback)
            sel.click(testvars.rev_rollback)
            self.assertEqual("Subtitles will be rolled back to a previous version", sel.get_confirmation())
            sel.click(testvars.transcripts_tab)
            website.verify_subs(self,sel,"subs.txt")
            


            



# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        # check for Site Error notification and submit
        website.handle_error_page(self,self.selenium,self.id())
        #Close the browser
#        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)
      


if __name__ == "__main__":
    unittest.main()

 
