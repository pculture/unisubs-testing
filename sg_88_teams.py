from selenium import selenium
import unittest
import time
import os
import StringIO
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
        #test data
                
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        #create team
        team = website.get_own_team(self,sel)
        
        #submit video
        sel.window_maximize()
        test_video_url = website.submit_random_youtube(self,sel)
        print test_video_url
        self.assertTrue(sel.is_element_present("css=strong:contains('Add video to team')"))
        vid_title = sel.get_text(testvars.vid_title)
        #add video to team and verify values
        sel.click_at("css=strong:contains('Add video to team')","")
        sel.click("css=li a:contains('"+team+"')")
        sel.wait_for_page_to_load(testvars.timeout)
        print "verifying the inital add page"

        if sel.is_element_present("css=.errorlist:contains('Team has this')"):
            print "video already part of team"
        else:
            mslib.wait_for_element_present(self,sel,"css=p label[for=id_language]")
            sel.select("id_language", "label=English (English)")
            sel.click("css=.green_button.small:contains('Save')")
            sel.wait_for_page_to_load(testvars.timeout)
        self.assertTrue(sel.is_element_present("css=li.active a:contains('"+team+"')"))
        sel.click(testvars.teams_video_tab)
        sel.wait_for_page_to_load(testvars.timeout)
        print "verifying team videos list"
        self.assertTrue(sel.is_element_present("css=tr.video-container td a[href*='"+test_video_url+"info/']"),"test_video_url error")
        self.assertTrue(sel.is_element_present("css=tr.video-container td:contains('"+vid_title[0:10]+"')"),"vid_title error")
        # delete the video from the team
        sel.click("css=td:contains('"+vid_title[0:10]+"') > div a.remove-video")
        try:
            self.failUnless("Remove this video", sel.get_confirmation())
        except:
            print "no confirmation - hitting enter"
            sel.key_press_native('10') #workaround for FF 4 selenium confirmation bug


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


        #Edit original language
        sel.open("teams/"+team)
        sel.wait_for_page_to_load(testvars.timeout)        
        sel.click(testvars.vid_add_subs_button)
        vid_lang_str = sel.get_text("css=h3:contains('Create subtitles') + div p")
        vid_lang = vid_lang_str.split("in ")[1]
        widget.starter_dialog_edit_orig(self,sel)
        widget.submit_sub_edits(self,sel)

        #Edit translation
        vid_lang_str = sel.get_text("css=h3:contains('Create subtitles') + div p")
        vid_lang = vid_lang_str.split("in ")[1]
        sel.open("teams/"+team)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.click(testvars.vid_add_subs_button)
        starter_dialog_translate_from_orig(self,sel,to_lang='hr')
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        widget.edit_translation(self,sel,subtextfile)

        #New fork
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.open("teams/"+team)
        sel.wait_for_page_to_load(testvars.timeout)        
        sel.click(testvars.vid_add_subs_button)
        starter_dialog_fork(self,sel,to_lang='hr')
        print "transcribing video"
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        print "syncing video"
        widget.sync_video(self,sel,subtextfile,3,4)
        # Review
        print "review step - just submitting video"
        widget.submit_sub_edits(self,sel)


    def test_697(self):
        """Open Al Jazeera team page and see if Language Dialog goes away after lang selected.

        http://litmus.pculture.org/show_test.cgi?id=---.      
        """
        errors = []
        for x in range(1,5):
            try:
                sel.open("/teams/al-jazeera")
                if (sel.is_element_present("css=.language_modal")):
                    sel.click("css=button.green_button.small")
                    mslib.wait_for_element_not_present(self,sel,"css=h2:contains('What languages do you speak')")                    
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

    
