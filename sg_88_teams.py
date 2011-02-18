from selenium import selenium
import unittest
import time
import os
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
        team = "Miro"+time.strftime("%m%d%H%M%S", time.gmtime())
        url = "http://blip.tv/file/get/Miropcf-Miro20Introduction771.ogv"
        team_logo_path = os.path.join(testvars.MSTestVariables["DataDirectory"],"sheep.png")
        
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        #create team
        website.open_teams_page(self,sel)
        sel.click(testvars.start_team)
        sel.wait_for_page_to_load(testvars.timeout)
        website.create_team(self,sel,team,url,team_logo_path)
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
        website.create_team(self,sel,team,url,team_logo_path)
        # logout
        sel.click(testvars.WebsiteUI["Logout_Button"])
        

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
        test_video_url = website.get_video_no_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        self.assertTrue(sel.is_element_present("css=strong:contains('Add video to team')"))
        vid_title = sel.get_text("css=.main-title a")
        #add video to team and verify values
        sel.click_at("css=strong:contains('Add video to team')")
        sel.click("css=li a:contains('"+team+"')")
        sel.wait_for_page_to_load(testvars.timeout)
        print "verifying the inital add page"
        try:
            self.assertEqual(selvars.set_site()+test_video_url, sel.get_value("css=input#id_video_url"))
            team_vid_title = sel.get_value("css=input#id_title")
            self.assertEqual(vid_title[0:10], team_vid_title[0:10])
        except AssertionError, e: self.verificationErrors.append("error verify video add page:"+str(e))
        if sel.is_element_present("css=.errorlist:contains('Team has this')"):
            print "video already part of team"
        else:
            sel.select("id_language", "label=English (English)")
            sel.click("css=.green_button.small:contains('Save')")
            sel.wait_for_page_to_load(testvars.timeout)
        self.assertTrue(sel.is_element_present("css=li.active a:contains('"+team+"')"))
        sel.click(testvars.teams_video_tab)
        sel.wait_for_page_to_load(testvars.timeout)
        print "verifying team videos list"
        try:
            self.assertTrue(sel.is_element_present("css=tr.video-container td a[href*='"+test_video_url+"info/']"),"test_video_url error")
            self.assertTrue(sel.is_element_present("css=tr.video-container td:contains('"+vid_title[0:10]+"')"),"vid_title error")
        except AssertionError, e: self.verificationErrors.append(str(e))
        # delete the video from the team
        sel.click("css=td:contains('"+vid_title[0:10]+"') > div a.remove-video")
        self.failUnless("Remove this video", sel.get_confirmation())


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
        if sel.get_value("id_is_visible") == "on":
            sel.click("id_is_visible")
        website.save_team_settings(self,sel)
        # logout and verify team no longer displayed
        sel.click(testvars.WebsiteUI["Logout_Button"])
        website.open_teams_page(self,sel)
        website.search_teams(self,sel,team)
        self.failIf(sel.is_element_present("link="+team))
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        website.open_teams_page(self,sel)
        website.search_teams(self,sel,team)
        self.assertTrue(sel.is_element_present("css=a[href*='/teams/"+team+"']"))
        # reset setting
        sel.open("teams/"+team)
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
             
        
        

        
# Close the browser, log errors, perform cleanup
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

if __name__ == "__main__":
    unittest.main()
