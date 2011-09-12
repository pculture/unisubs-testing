from selenium import selenium
import unittest
import time
import os
import StringIO
import re
import mslib
import website
import widget
import offsite
import testvars
import selvars
import litmusresult



class subgroup_88(unittest.TestCase):
    """
    Litmus Subgroup 88 - Teams Tests
    Tests designed to test the Teams feature.
    """
    
    # Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), selvars.set_site())
        self.selenium.start()
        self.session = self.selenium.sessionId
        
        
    # The tests in the subgroup
    def test_603(self):
        """Create a new team - open membership.

        http://litmus.pculture.org/show_test.cgi?id=603.      
        """
        sel = self.selenium
        sel.set_timeout(testvars.timeout)
        #test data
        team = "miro"+time.strftime("%m%d%H%M%S", time.gmtime())
        team_logo_path = os.path.join(testvars.MSTestVariables["DataDirectory"],"sheep.png")
        
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        #create team
        website.open_teams_page(self,sel)
        sel.click(testvars.start_team)
        sel.wait_for_page_to_load(testvars.timeout)
        website.create_team(self,sel,team,team_logo_path)
        sel.open("teams/"+team)
        # logout
        sel.click(testvars.WebsiteUI["Logout_Button"])


    def test_604(self):
        """Create a new team - required fields.

        http://litmus.pculture.org/show_test.cgi?id=604.      
        """
        sel = self.selenium
        sel.set_timeout(testvars.timeout)
        #test data
        team = ""
        url = "http://blip.tv/file/get/Miropcf-Miro20Introduction771.ogv"
        team_logo_path = os.path.join(testvars.MSTestVariables["DataDirectory"],"sheep.png")
        
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        #create team
        website.open_teams_page(self,sel)
        sel.click(testvars.start_team)
        sel.wait_for_page_to_load(testvars.timeout)
        website.create_team(self,sel,team,team_logo_path)
        # logout
##        website.SiteLogout(self,sel)
        

    def test_613(self):
        """Submit a video and add to team.

        http://litmus.pculture.org/show_test.cgi?id=613.      
        """
        sel = self.selenium
        sel.set_timeout(testvars.timeout)
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        #create team
        team = "miro"+time.strftime("%m%d%H%M%S", time.gmtime())
        team_logo_path = os.path.join(testvars.MSTestVariables["DataDirectory"],"sheep.png")
        website.open_teams_page(self,sel)
        sel.click(testvars.start_team)
        sel.wait_for_page_to_load(testvars.timeout)
        website.create_team(self,sel,team,team_logo_path)
        
        #submit video
        sel.window_maximize()
        test_video_url = website.submit_random_youtube(self,sel)
        print test_video_url
        mslib.wait_for_element_present(self,sel,"css=span.sort_label strong:contains('Add video')")
        vid_title = sel.get_text(testvars.vid_title)
        #add video to team and verify values
        teamli = "add/video/"+team



                  
        sel.click(testvars.video_add_to_team)
##        sel.click_at("css=span.sort_label strong:contains('Add video')","")
        sel.click_at("css=a[href*='"+teamli+"']","")
        
        sel.wait_for_page_to_load(testvars.timeout)
        print "verifying the inital add page"

        if sel.is_element_present("css=.errorlist")== True:
            print "error adding video to team"
            self.fail()
        else:
            mslib.wait_for_text_present(self,sel,"Video language")
            sel.select("id_language", "value=en")
            sel.click(testvars.teams_save)
            sel.wait_for_page_to_load(testvars.timeout)
        self.assertTrue(sel.is_element_present("css=li.active a:contains('"+team+"')"))
        sel.click(testvars.teams_video_tab)
        sel.wait_for_page_to_load(testvars.timeout)
        print "verifying team videos list"
        self.assertTrue(sel.is_element_present("css=tr.video-container td a[href*='"+test_video_url+"info/']"),"test_video_url error")
#        self.assertTrue(sel.is_element_present("css=tr.video-container td:contains('"+vid_title[0:10]+"')"),"vid_title error")
        # delete the video from the team
        sel.click("css=td a:contains('"+vid_title[0:10]+"') +div +div +div.small.grey a.remove-video")
        self.failUnless(re.search(r"^Remove this video[\s\S]$", sel.get_confirmation()))

        # logout
        sel.click(testvars.WebsiteUI["Logout_Button"])


    def test_609(self):
        """Team Privacy Settings.

        http://litmus.pculture.org/show_test.cgi?id=609.      
        """
        sel = self.selenium
        sel.set_timeout(testvars.timeout)

        
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        #locate or create your team
        team = website.get_own_team(self,sel)
        print "testing with team: " +team
        #open team manager settings and mark as not public
        sel.open("teams/"+team)
        sel.click(testvars.manage_team)
        sel.wait_for_page_to_load(testvars.timeout)
        if str(sel.get_value("is_visible")) == "on":
            sel.click("is_visible")
            time.sleep(1)
        self.failIf(str(sel.get_value("is_visible")) == "on","is_visible not set to off")
        website.save_team_settings(self,sel)
        # logout and verify team no longer displayed
        sel.click(testvars.WebsiteUI["Logout_Button"])
        website.open_teams_page(self,sel)
        website.search_teams(self,sel,team)
        self.failIf(sel.is_element_present("link="+team))
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        website.open_teams_page(self,sel)
        website.search_teams(self,sel,team)
        self.assertTrue(sel.is_element_present("css=a[href*='/teams/"+team.lower()+"']"))
        # reset setting
        sel.open("teams/"+team.lower())
        sel.click(testvars.manage_team)
        sel.wait_for_page_to_load(testvars.timeout)
        if sel.get_value("id_is_visible") == "off":
            sel.click("id_is_visible")
            website.save_team_settings(self,sel)
        
    def test_605(self):
        """Team Edit Description

        http://litmus.pculture.org/show_test.cgi?id=605.      
        """
        sel = self.selenium
        sel.set_timeout(testvars.timeout)
        
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        #locate or create your team
        team = website.get_own_team(self,sel)
        print "testing team: " + team
        #open team manager settings and edit the description
        sel.open("teams/"+team)
        sel.click(testvars.manage_team)
        sel.wait_for_page_to_load(testvars.timeout)
        timestamp = time.strftime("%m%d%H%M%S", time.gmtime())
        print timestamp
        new_text = "Test 605: edit description for http://pculture.org "
        sel.type("id_description", new_text+timestamp)
        website.save_team_settings(self,sel)
        sel.wait_for_page_to_load(testvars.timeout)
        # logout and verify team no longer displayed   
        sel.open("teams/"+team)
        self.assertTrue(sel.is_text_present(new_text))


    def test_693(self):
        """Launch widget from Teams page.

        Currently testing on al-jazeera teams page.

        """
        sel = self.selenium
        sel.set_timeout(testvars.timeout)
        
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        team = "al-jazeera"
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")


        #Edit original language
        print "testing edit original lang"
        sel.open("/teams/"+team)
        sel.wait_for_page_to_load(testvars.timeout)
#        website.teampage_lang_select(self,sel)
        mslib.wait_for_element_present(self,sel,testvars.vid_add_subs_button)
        sel.click(testvars.vid_add_subs_button)
        time.sleep(5)
        widget.starter_dialog_edit_orig(self,sel)
        widget.transcribe_video(self,sel,subtextfile)
        widget.close_sub_widget(self,sel)        

        #Edit translation
        print "testing edit translation"
        sel.open("/teams/"+team)
        sel.wait_for_page_to_load(testvars.timeout)
#        website.teampage_lang_select(self,sel)
        mslib.wait_for_element_present(self,sel,testvars.vid_add_subs_button)
        sel.click(testvars.vid_add_subs_button)
        time.sleep(5)
        widget.starter_dialog_translate_from_orig(self,sel,to_lang='hr')
        widget.edit_translation(self,sel,subtextfile)
        widget.close_sub_widget(self,sel)

        #New fork
        print "testing new fork"
        sel.open("teams/"+team)
        sel.wait_for_page_to_load(testvars.timeout)
#        website.teampage_lang_select(self,sel)
        mslib.wait_for_element_present(self,sel,testvars.vid_add_subs_button)
        sel.click(testvars.vid_add_subs_button)
        time.sleep(5)
        widget.starter_dialog_fork(self,sel,to_lang='pl')
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile,3,4)
        # Review
        print "review step - just submitting video"
        widget.submit_sub_edits(self,sel,offsite=True)


    def test_697(self):
        """Open Al Jazeera team page and see if Language Dialog goes away after lang selected.

        http://litmus.pculture.org/show_test.cgi?id=697      
        """
        
        errors = []
        for x in range(1,5):
            try:
                self.selenium.stop()
                self.selenium.start()
                self.session = self.selenium.sessionId
                sel = self.selenium
                sel.set_timeout(testvars.timeout)
                sel.open("/teams/al-jazeera")
                sel.wait_for_page_to_load(testvars.timeout)
                website.teampage_lang_select(self,sel)
                
            except:
                print "got an error on run#:" +str(x)
                errors.append(str(x))
        self.assertEqual([], errors)
         

    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        
        #give it back the session id in case it's lost it
        self.selenium.sessionId = self.session
        #Check for an error page, then close the browser
        website.handle_error_page(self,self.selenium,self.id())
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)
        if selvars.set_sauce() == True:
            output = StringIO.StringIO()
            output.write("sauce job result: http://saucelabs.com/jobs/"+str(self.session))
       
if __name__ == "__main__":
    unittest.main()

    
