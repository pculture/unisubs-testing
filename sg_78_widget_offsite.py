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
        mslib.wait_for_element_present(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
        website.start_sub_widget(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
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
        mslib.wait_for_element_present(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
        website.start_sub_widget(self,sel,"css=.left_column span.mirosubs-tabTextchoose")

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


class subgroup_78_subtesting(unittest.TestCase):
    """
    Litmus Subgroup 78 - offsite subwidget:
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
        self.selenium.set_timeout(testvars.timeout)
        
   
# The test cases of the subgroup.


    def test_601(self):
        """Widgetizer offsite on wordpress with youtube video.
        
        http://litmus.pculture.org/show_test.cgi?id=601

        We are explicitly testing the Right-Wing Radio Duck in 1st position on the page
        """
        test_id = 601
        vid_pos = "css=div:nth-child(3) > a span"
        vid_title = "Right-Wing Radio Duck"
        print self.shortDescription()
        sel = self.selenium
        test_page = (selvars.set_subtesting_wordpress_page(self,test_id))
        sel.open(test_page)
        mslib.wait_for_element_present(self,sel,vid_pos)
        if sel.get_text(vid_pos) == "Subtitle Me":
            make_new_subs(self,sel)
        else:
            edit_subs_and_revert(self,sel,test_page,vid_pos,vid_title)

    def test_622(self):
        """widgetizer offsite wordpress in-page script element youtube
        
        http://litmus.pculture.org/show_test.cgi?id=622

        We are explicitly testing the Right-Wing Radio Duck in 1st position on the page
        """
        test_id = 622
        vid_pos = "css=div:nth-child(3) > a span"
        vid_title = "Right-Wing Radio Duck"
        print self.shortDescription()
        sel = self.selenium
        test_page = (selvars.set_subtesting_wordpress_page(self,test_id))
        sel.open(test_page)
        sel.open(selvars.set_subtesting_wordpress_page(self,test_id))
        mslib.wait_for_element_present(self,sel,vid_pos)
        if sel.get_text(vid_pos) == "Subtitle Me":
            make_new_subs(self,sel,vid_pos)
        else:
            edit_subs_and_revert(self,sel,test_page,vid_pos,vid_title)

       



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
    """
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
        self.selenium.set_timeout(testvars.timeout)
        
   
# The test cases of the subgroup.




    def test_623(self):
        """widgetizer offsite wordpress in-page script element youtube
        
        http://litmus.pculture.org/show_test.cgi?id=622

        We are explicitly testing the Right-Wing Radio Duck in 1st position on the page
        """
        test_id = 623
        vid_pos = "css=p.pElementTest span span.mirosubs-widget div.mirosubs-videoTab a span.mirosubs-tabTextchoose"
        vid_title = "hunter.s.thompson.avi"
        print self.shortDescription()
        sel = self.selenium
        test_page = selvars.set_unisubs_mc_page(self,test_id)
        sel.open(test_page)
        mslib.wait_for_element_present(self,sel,vid_pos)
        if sel.get_text(vid_pos) == "Subtitle Me":
            make_new_subs(self,sel,vid_pos)
        else:
            edit_subs_and_revert(self,sel,test_page,vid_pos,vid_title)

       



# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Check for an error page, then close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


      

def make_new_subs(self,sel,vid_pos):

    print "no subs yet - making new ones"
    subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
    website.start_sub_widget(self,sel,vid_pos)
    # Transcribe
    widget.transcribe_video(self,sel,subtextfile)
    # Sync
    widget.sync_video(self,sel,subtextfile,6,8)
    # Review
    widget.edit_text(self,sel,subtextfile)


def edit_subs_and_revert(self,sel,test_page,vid_pos,vid_title):
        print "has subs - going to editing then revert"
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

 
