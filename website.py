"""Functions to take care of business on the universalsubtitles website


"""

from selenium import selenium

import unittest, time, re
import mslib, testvars, widget


#Login as a user

def SiteLogIn(self,sel,user,passw):
    """
    Description: Login to site using the website login button and a site account
    
    Requires: valid site user name and password.
    
    Pre-condition: user is on the site page.


    
    Post-condition: user is still on the site page
    """
    sel.open("/logout/?next=/")
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    sel.click(testvars.WebsiteUI["Login_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("id_username", user)
    sel.type("id_password", passw)
    sel.click("//button[@value='login']")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Logout_Button"])

def SiteLogout(self,sel):
    """
    Description: Logout of site using site Logout button.

    """
    sel.open("/logout/?next=/")
    mslib.wait_for_element_present(self,sel,"css=.login_link")
    if sel.is_element_present(testvars.WebsiteUI["Logout_Button"]):
        sel.click(testvars.WebsiteUI["Logout_Button"])
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    

def Login(self,sel,auth_type):
    """
    Description: Log on using website button and select an external login option.
    auth_type can be either '.twitter', '.open-id', or '.google'

    Requires: valid account for selected login.  See testvars for existing accounts.

    Pre-condition: user is on the site page
    
    Post-condition: offsite login form displayed, see offsite
    
    
    """
    # auth_type can be either ".twitter", ".open-id", "google"
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    sel.click(testvars.WebsiteUI["Login_Button"])
    mslib.wait_for_element_present(self,sel,"css=."+auth_type)
    sel.click("css=." +auth_type)
    #After login, use offsite to do auth

def start_demo(self,sel):
    """
    Description: Starts the demo widget from the site

    Pre-condition: site page is opened

    Post-condition: /demo page is opened, usually next step is start_sub_widget
    """
    sel.open("/demo/")
#    mslib.wait_for_element_present(self,sel,"css=.try_link")
#    sel.click("css=.try_link span:contains('Demo')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])

def submit_video(self,sel,url):
    """
    Description: Submit a video using the site button

    Pre-condition: site page is opened

    Post-condition: the widget is launched immediately.
    You'll need to deal with the help video, see widget.close_howto_video
    """
    sel.open("/")
    sel.click(testvars.WebsiteUI["Subtitle_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    

def start_sub_widget(self,sel,skip="True"):
    """
    Description: Start the Subtitle Widget using the Subtitle Me menu.
    skip is set to true by default and gets passed to widget.close_howto_video
    to prevent further how-to video displays.

    Pre-condition: On a page where Subtitle Me menu is present.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    # Click Subtitle Me (Continue Subtitling -> Add Subtitles)
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
    sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
    time.sleep(5)
    if sel.is_element_present("css=.mirosubs-modal-widget"):
        print "widget opened directly - no menu displayed."
    elif sel.is_element_present("css=.mirosubs-uniLogo"):
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["AddSubtitles_menuitem"])
        sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])
    else:
        print "not sure what's going on here, no widget, not menu"
    widget.close_howto_video(self,sel,skip)
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")
    sel.select_frame("relative=top")

def verify_login(self,sel,username="sub_writer"):
    """
    Description: Verifies user is logged in by finding the logout button on the
    website and then starting the demo and looking for logout menu item on the
    Subtitle Me button.

    Pre-Condition: must be logged into site.

    Post-Condition: will be on the /demo page
    """
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Logout_Button"])
    self.failUnless(sel.is_element_present("css=.user_panel"))
    print "logged in as: " + sel.get_text("css=.user_panel a")
    self.failUnless(sel.is_element_present("css=.user_panel a:contains("+username+")"))
    #not starting demo to check logged in status anymore
##    start_demo(self,sel)
##    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
##    sel.click_at(testvars.WebsiteUI["SubtitleMe_menu"], "")
##    self.failUnless(sel.is_element_present(testvars.WebsiteUI["Logout_menuitem"]))


def verify_submitted_video(self,sel,vid_url,embed_type="html5"):
    """
    Description: Verifies the contents of the main video page of a submitted video.
    Require's the original url and expected type of embed.  Assumes html5 video if not specified.

    embed_type one of 'youtube', 'flow' 'html5' (default)

    Returns: url of the video on the universalsubtitles site.
    """
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
   
    if embed_type == "flow":
        print "verifying video embedded with flowplayer"
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-videoDiv object")
        self.failUnless(sel.is_element_present("css=.mirosubs-videoDiv object[data*='flowplayer']"))
    elif embed_type == "youtube":
        print "verifying video embedded with youtube"
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-videoDiv object[data]")
        self.failUnless(sel.is_element_present("css=.mirosubs-videoDiv object[data*='youtube.com']"))
    elif embed_type == 'vimeo':
        print "verifying video embedded with vimeo"
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-videoDiv object")
        self.failUnless(sel.is_element_present("css=.mirosubs-videoDiv object[data*='moogaloop.swf']"))

    else:
        print "verifying video is html5"
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-videoDiv")
        self.failUnless(sel.is_element_present("css=.mirosubs-videoDiv video"))
    print "verifying embedded video url is same as original"    
    self.failUnless(sel.is_element_present("css=.mirosubs-embed:contains("+vid_url+")"))
    unisubs_link = sel.get_text("css=.mirosubs-permalink[href]")
    return unisubs_link

def get_video_with_translations(self,sel):
    """Get the url of the video page for a video that has translations.

    Returns: video_url
    """
    sel.open("videos/")
    sort_videos_table(self,sel,"Translations","desc") 
    row_no = 1
    local_url = "none"
    
    subtitled_cell="css=tr:nth-child("+str(row_no)+") > "+testvars.videos_subtitled_td
    while sel.is_element_present(subtitled_cell):
        if sel.get_text(subtitled_cell) == "yes":
            local_url = sel.get_attribute("css=tr:nth-child("+str(row_no)+ ") > "+testvars.videos_url_td+" > a@href")
            if int(sel.get_text("css=tr:nth-child("+str(row_no)+ " ) > "+testvars.videos_trans_td)) == 0:
                print "no translations - have to add one"
                translate_video(self,sel,local_url)
        row_no = row_no + 1
        subtitled_cell=sel.get_text("css=tr:nth-child("+str(row_no)+") > "+testvars.videos_subtitled_td)
        
    return local_url

def get_translated_lang(self,sel):
    """Locate a language (not metadata or original) tab for a video

    Need to exclude Original, Video Info, and Metadata
    """
    tab_no = 1
    tab_li = "css=ul.left_nav li:nth-child("+str(tab_no)+")"
    skip_list = ["Original", "Video Info", "Metadata: Twitter", "Metadata: Geo", "Metadata: Wikipedia"]
    while sel.is_element_present(tab_li):
        tab_li = "css=ul.left_nav li:nth-child("+str(tab_no)+")"
        if sel.get_text(tab_li) not in skip_list:
            test_lang = sel.get_text(tab_li)
            print test_lang
            break       
        tab_no = tab_no + 1
        tab_li = "css=ul.left_nav li:nth-child("+str(tab_no)+")"
    
    return test_lang

def translate_video(self,sel,url=None,lang=None):
    """Given the local url of a video, adds a translation.

        
    """
    if url == None:
        print "adding translation from current page"
    else:
        print "opening video page to translate"
        sel.open(url)
    self.failUnless(sel.is_element_present("css=a#add_translation"))
    sel.click(testvars.add_translation_button)
        
    
        

def sort_videos_table(self,sel,column,order):
    """Sort the videos table by the specified heading in the specified order

    Current column headings are: URL, Pageloads, Subtitles Fetched, Translations, Subtitled?
    Order can be 'asc' or 'desc'

    """

    if sel.is_element_present("css=a."+order+":contains("+column+")"):
        sel.click("link="+column)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if order == "asc":
        self.failUnless(sel.is_element_present("css=a.desc:contains("+column+")"))
    if order == "desc":
        self.failUnless(sel.is_element_present("css=a.asc:contains("+column+")"))


def enter_comment_text(self,sel,comment):
    """Enter text in the Comments box and submit

    Assumes user is on the comments tab
    """
    self.failUnless(sel.is_element_present("css=li.active span:contains(\"Comments\")"))
    sel.type("css=textarea#id_comment_form_content", comment)
    sel.click("css=button:contains('Comment')")

def verify_comment_text(self,sel,comment,result="posted",reply_text=None):
    """After comment text is entered in enter_comment_text, verify correct post behavior

    Result options: 'posted' comment is posted
                    'stripped' commented is posted and html stripped
                    'too long' > 3000 char length warning
                    'login' user must be logged into post
                    'reply' reply post contains original and new comment
    
    """
    #give it 1 second to post
    time.sleep(1)
    if result == "posted":
        posted_text = sel.get_text("css=ul.comments.big_list li:nth-child(1) > div.info p")
        self.assertEqual(posted_text.strip(),comment.strip(),"found: "+posted_text+" expected: "+comment)
    elif result == "too long":
        self.failUnless(sel.is_element_present("css=p.error_list:contains('Ensure this value has at most 3000 characters')"))
    elif result == "login":
        self.failUnless(sel.is_element_present("css=.login-for-comment:contains('Login to post a comment')"))
        if sel.is_element_present("css=ul.comments.big_list li:nth-child(1) > div.info p"):
            self.failIf(sel.get_text("css=ul.comments.big_list li:nth-child(1) > div.info p") == comment)

        
      

    

    


def handle_error_page(self,sel,test_id):
    if sel.is_element_present("css=form h2:contains('Error')"):
        print sel.get_attribute("css=h2 + input@value")
        print sel.get_attribute("css=h2 + input@name")
        sel.type("feedback_email", testvars.gmail)
        feedback_math = sel.get_text("css=form#feedback_form p + p label")
        s = feeback_math[20:25]
        sel.type("feedback_math_captcha_field", eval(s))
        sel.type("feedback_message", "test_id: "+test_id+" sel-rc automated test encountered an error")
        sel.click("css=button[type='submit']")
        print "submitted error to feedback form"
    else:
        print "no site errors encountered"



