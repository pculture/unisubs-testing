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
    Litmus Subgroup 70 - revisions tests.
    
    Tests designed to exercise versioning of subtitles.  
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
        unisubs_url = website.verify_submitted_video(self,sel,vid_url,embed_type="youtube")
        # Start sub widget
        print "starting sub widget"
        website.start_sub_widget(self,sel)
        # Transcribe
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile)
        # Review
        widget.submit_sub_edits(self,sel)
        time.sleep(5)
        sel.select_frame("relative=top")
        sel.click(testvars.video_original)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        website.verify_subs(self,sel,subtextfile)
        # Click History tab
        sel.click(testvars.history_tab)
        time.sleep(2)
        rev_num = website.get_current_rev(self,sel)
        website.verify_latest_history(self,sel,rev=str(rev_num),user="sub_writer",tm="100%",text="100%")
        #cleanup
        website.admin_delete_video(self,sel,unisubs_url)


    def test_486(self):
        """Revisions - edit subtitles timing and verify in history table.

        http://litmus.pculture.org/show_test.cgi?id=486
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
        website.submit_video(self,sel,vid_url)
        # Verify embed and player
        print "verifying embed"
        unisubs_url = website.verify_submitted_video(self,sel,vid_url,embed_type="youtube")
        # Start sub widget
        print "starting sub widget"
        website.start_sub_widget(self,sel)
        # Transcribe
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile)
        # Review
        print "review step - just submitting video"
        widget.submit_sub_edits(self,sel)
        mslib.wait_for_element_present(self,sel,testvars.video_video_info)
        sel.select_frame("relative=top")
        sel.click(testvars.video_original)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        # Verify subtitles
        website.verify_subs(self,sel,subtextfile)
        sel.click(testvars.video_add_translation)
        widget.starter_dialog_edit_orig(self,sel)
        widget.goto_step(self,sel,"2")
        widget.resync_video(self,sel,subtextfile)
        widget.submit_sub_edits(self,sel)
        time.sleep(2)
        sel.select_frame("relative=top")
        # Click History tab
        sel.click(testvars.video_original)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        sel.click(testvars.history_tab)
        rev_num = website.get_current_rev(self,sel)
        website.verify_latest_history(self,sel,rev=str(rev_num),user="sub_writer",tm="100%",text="0%")
        website.admin_delete_video(self,sel,unisubs_url)
                
    def test_602(self):
        """Revisions - edit subtitles text and verify in history table.

        http://litmus.pculture.org/show_test.cgi?id=602
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
        website.submit_video(self,sel,vid_url)
        
        # Verify embed and player
        print "verifying embed"
        website.verify_submitted_video(self,sel,vid_url,embed_type="youtube")
        # Start sub widget
        print "starting sub widget"
        time.sleep(5)
        website.start_sub_widget(self,sel)
        # Transcribe
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile)
        # Review
        print "review step - just submitting video"
        widget.submit_sub_edits(self,sel)
        #Website verify subs        
        sel.select_frame("relative=top")
        sel.click(testvars.video_original)
        website.verify_subs(self,sel,subtextfile)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        #Edit subtitles
        sel.click(testvars.video_add_translation)
        widget.starter_dialog_edit_orig(self,sel)
        widget.goto_step(self,sel,"3")
        widget.edit_text(self,sel,subtextfile)
        widget.submit_sub_edits(self,sel)
        time.sleep(2)
        sel.select_frame("relative=top")
        
        # Click Original language then History tab
        sel.click(testvars.video_original)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.click(testvars.history_tab)
        rev_num = website.get_current_rev(self,sel)      
        website.verify_latest_history(self,sel,rev=str(rev_num),user="sub_writer",tm="0%",text="100%")



    def test_492(self):
        """Revisions - compare translation revisions.

        http://litmus.pculture.org/show_test.cgi?id=492
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        website.SiteLogIn(self,sel,testvars.siteuser, testvars.passw)
        #get a video and open page    
        test_video_url = website.get_video_with_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        language = website.get_translated_lang(self,sel)
        website.click_lang_tab(self,sel,language)
               
        website.store_subs(self,sel)
        rev_num = website.get_current_rev(self,sel)
        subtextfile = "subs.txt"
        #If there is only 1 revision - edit the subs to make a new revision
        if int(rev_num) < 1:
            print "only 1 rev - editing text first"
            sel.click(testvars.video_edit_subtitles)
            widget.goto_step(self,sel,step="3")
            widget.edit_text(self,sel,subtextfile)
            widget.submit_sub_edits(self,sel)
            website.click_lang_tab(self,sel,language)
            sel.select_frame("relative=top")  

        sel.click(testvars.history_tab)
        mslib.wait_for_element_present(self,sel,testvars.video_compare_revisions)
        #get the checkbox value for comparing
        row_num = 2
        website.check_the_box(self,sel,row_num) #check the box
        sel.click(testvars.video_compare_revisions)
        website.verify_compare_revisions(self,sel,str(int(rev_num) - 1),str(rev_num))
        if sel.get_value("//div[@id='revisions-tab']/table/tbody/tr["+str(row_num)+"]/td[1]/input") == "on":
            website.check_the_box(self,sel,row_num) #uncheck the box

        #If there are more than 2 revision, test another compare
        if int(rev_num) > 2:
            row_num = 3
            old_rev = int(rev_num)-2
            website.check_the_box(self,sel,row_num)
            sel.click(testvars.video_compare_revisions)
            website.verify_compare_revisions(self,sel,old_rev,str(rev_num))

    def test_493(self):
        """Revisions - original - invalid comparison selection

        http://litmus.pculture.org/show_test.cgi?id=493
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        website.SiteLogIn(self,sel,testvars.siteuser, testvars.passw)
        #get a video and open page    
        test_video_url = website.get_video_with_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        print "open original lang"
        sel.click(testvars.video_original)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        print "go to history tab"
        sel.click(testvars.history_tab)    
        row_num = 1
        #uncheck default 1st box checked
        website.check_the_box(self,sel,row_num) #uncheck the box
        print "verifing invalid message when 1 box checked"
        while sel.is_element_present("//div[@id='revisions-tab']/table/tbody/tr["+str(row_num)+"]"):
            website.check_the_box(self,sel,row_num)   
            sel.click(testvars.video_compare_revisions)
            self.assertEqual("Select two revisions for compare, please", sel.get_alert())
            website.check_the_box(self,sel,row_num)    #uncheck the box
            row_num += 1
            if row_num == 3:
                break
            
            
    def test_494(self):
        """Revisions - translation - invalid comparison selection

        http://litmus.pculture.org/show_test.cgi?id=494
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        website.SiteLogIn(self,sel,testvars.siteuser, testvars.passw)
        #get a video and open page    
        test_video_url = website.get_video_with_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        language = website.get_translated_lang(self,sel)
        website.click_lang_tab(self,sel,language)

        
        ## if not enough revisions for comparison, edit the sub text.
        rev_num = website.get_current_rev(self,sel)
        print rev_num
        while rev_num < 2:
            print "only 2 or less revs - editing text first"
            #edit text
            sel.click(testvars.video_edit_subtitles)
            mslib.wait_for_element_present(self,sel,"css=div.unisubs-help-heading")
            if sel.is_element_present("css=h2:contains('Editing Translation')"):
                widget.edit_translation(self,sel,subtextfile)
            else:
                widget.goto_step(self,sel,step="3")
                widget.edit_text(self,sel,subtextfile)

            widget.submit_sub_edits(self,sel)
            rev_num = website.get_current_rev(self,sel)
        
        sel.click(testvars.history_tab)
        row_num = 1
        website.check_the_box(self,sel,row_num) #uncheck the box to start
        while sel.is_element_present("//div[@id='revisions-tab']/table/tbody/tr["+str(row_num)+"]"):
            website.check_the_box(self,sel,row_num)                
            sel.click(testvars.video_compare_revisions)
            self.assertEqual("Select two revisions for compare, please", sel.get_alert())
            website.check_the_box(self,sel,row_num) #uncheck the box
            row_num += 1
            if row_num == 3:
                break

    def test_495(self):
        """Revisions - original - history diffs

        http://litmus.pculture.org/show_test.cgi?id=495
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        website.SiteLogIn(self,sel,testvars.siteuser, testvars.passw)
        #get a video and open page    
        test_video_url = website.get_video_with_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        sel.click(testvars.video_original)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])

        sel.click(testvars.history_tab)
        rev_num = website.get_current_rev(self,sel)
        row_num = 2
        
                
        while sel.is_element_present("//div[@id='revisions-tab']/table/tbody/tr["+str(row_num)+"]"):
            website.check_the_box(self,sel,row_num) #check the box
            old_rev = rev_num - 1
            sel.click(testvars.video_compare_revisions)
            website.verify_compare_revisions(self,sel,str(old_rev),str(rev_num))
            row_num += 1
            if row_num == 4:
                break
          


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





 
