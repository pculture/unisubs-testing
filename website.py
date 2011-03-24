from selenium import selenium

import unittest
import time
import re
import codecs
import os
import random
import mslib
import selvars
import testvars
import widget
import offsite


#Login as a user

def SiteLogIn(self,sel,user,passw):
    """
    Description: Login to site using the website login button and a site account
    
    Requires: valid site user name and password.
    
    Pre-condition: user is on the site page.


    
    Post-condition: user is still on the site page
    """
    sel.open("en/logout/?next=/")
    sel.window_maximize()
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
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
   

def Login(self,sel,auth_type):
    """
    Description: Log on using website button and select an external login option.
    auth_type can be either 'twitter', 'open-id', or 'google'

    Requires: valid account for selected login.  See testvars for existing accounts.

    Pre-condition: user is on the site page
    
    Post-condition: offsite login form displayed, see offsite
    
    
    """
    # auth_type can be either ".twitter", ".open-id", "google"
    if auth_type == "twitter":
        auth_link = "css=a[href*='twitter']"
    elif auth_type == "open-id":
        auth_link = "css=a[href*='openid']"
    elif auth_type == "google":
        auth_link = "css=a[href*='gmail']"
    else:
        self.fail("unrecognized auth type")
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    sel.click(testvars.WebsiteUI["Login_Button"])
    mslib.wait_for_element_present(self,sel,auth_link)
    sel.click(auth_link)
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    #After login, use offsite to do auth

def start_demo(self,sel):
    """
    Description: Starts the demo widget from the site

    Pre-condition: site page is opened

    Post-condition: /demo page is opened, usually next step is start_sub_widget
    """
#    sel.open("/demo/")
    sel.open("/")
#    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])

def submit_video(self,sel,url):
    """
    Description: Submit a video using the site button

    Pre-condition: site page is opened

    Post-condition: the widget is launched immediately.
    You'll need to deal with the help video, see widget.close_howto_video
    """
    print "* Submit Video"
    sel.open("/")
    sel.click(testvars.WebsiteUI["Subtitle_Button"])
    sel.window_maximize()
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    
def front_page_submit(self,sel,url):
    sel.open("/")
    sel.type("css=.submit_video", url)
    sel.click("css=.btn_submit_video")
    sel.wait_for_page_to_load(testvars.timeout)


def start_sub_widget(self,sel,wig_menu=testvars.WebsiteUI["SubtitleMe_menu"],skip="True",vid_lang="English",sub_lang="English"):
    """Start the Subtitle Widget using the Subtitle Me menu.

    This will handle the language choice for demo or submitted videos.
    skip is set to true by default and gets passed to widget.close_howto_video
    to prevent further how-to video displays.

    Pre-condition: On a page where Subtitle Me menu is present. Video with no subs.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    sel.window_maximize()
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
    sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
    time.sleep(5)
    if sel.is_element_present(testvars.WidgetUI["Select_language"]):
        widget.select_video_language(self,sel,vid_lang,sub_lang)
        time.sleep(15)
        widget.close_howto_video(self,sel)
    elif sel.is_element_present(testvars.WebsiteUI["AddSubtitles_menuitem"]):
        sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])
        widget.select_video_language(self,sel,vid_lang,sub_lang)    
        widget.close_howto_video(self,sel)
    else:
        self.fail("wtf - no widget, no sub menu")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")

def verify_login(self,sel,username="sub_writer"):
    """
    Description: Verifies user is logged in by finding the logout button on the
    website and then starting the demo and looking for logout menu item on the
    Subtitle Me button.

    Pre-Condition: must be logged into site.

    Post-Condition: will be on the /demo page
    """
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Logout_Button"])
    self.failUnless(sel.is_element_present("css=.user_panel"),\
                    "user not logged in, user_panel not displayed")
    print "logged in as: " + sel.get_text("css=.user_panel a")
    self.failUnless(sel.is_element_present("css=.user_panel a:contains("+username+")"),\
                    "username: "+username+ " not found. Got "+ sel.get_text("css=.user_panel a"))





def verify_submitted_video(self,sel,vid_url,embed_type=""):
    """
    Description: Verifies the contents of the main video page of a submitted video.
    Require's the original url and expected type of embed.  Assumes html5 video if not specified.

    embed_type one of 'youtube', 'flow' 'html5' (default)

    Returns: url of the video on the universalsubtitles site.
    """
    print " * verify submitted video, embed type"
    sel.wait_for_page_to_load(testvars.timeout)
    vid_embed = None
    vid_span_css = "css=div[id=widget_div] span object"
    vid_div_css = "css=div[id=widget_div] div object"
    html5_el = "css=div[id=widget_div] video"
    mslib.wait_for_element_present(self,sel,"css=div[id=widget_div]")
    if embed_type == "flow":
        self.assertTrue(sel.is_element_present("css=object[data*='flowplayer']"))
    elif embed_type == "youtube":
        self.assertTrue(sel.is_element_present(vid_span_css+"[data*='youtube.com']"))
    elif embed_type == 'vimeo':      
        self.assertTrue(sel.is_element_present(vid_span_css+"[data*='moogaloop.swf']"))
    elif embed_type == 'dailymotion':      
        self.assertTrue(sel.is_element_present(vid_span_css+"[id$='_dailymotionplayer']"))
    else:
        if sel.is_element_present("css=object[data*='flowplayer']"):
            vid_embed = 'flow'
        elif sel.is_element_present(html5_el):
            vid_embed = 'html5'
        self.assertTrue(vid_embed,"video not embedded in site: "+str(vid_url))
        
   
    self.assertTrue(sel.is_element_present("css=.mirosubs-embed"),\
                    "no embed code present")
    unisubs_link = sel.get_text("css=.mirosubs-permalink[href]")
    print sel.get_text("css=.mirosubs-embed")
    return unisubs_link

def get_video_with_translations(self,sel):
    """Get the url of the video page for a video that has translations.

    Returns: video_url
    """
    sel.open("videos/")
 #   sort_videos_table(self,sel,"Subtitles and Translations","desc") 
    row_no = random.randint(1,6)
    local_url = "none"    
    while sel.is_element_present("css=tr:nth-child("+str(row_no)+") > "+testvars.videos_trans_td):
        num_trans = sel.get_text("css=tr:nth-child("+str(row_no)+") > "+testvars.videos_trans_td)
        print num_trans
        if int(num_trans) > 1:
            local_url = sel.get_attribute("css=tr:nth-child("+str(row_no)+ ") > "+testvars.videos_url_td+" > a@href")
            break        
        row_no = row_no + 1        
    if local_url == "none":
        print "no translations - have to add one"
        vid_url = offsite.get_youtube_video_url(self)
        SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        submit_video(self,sel,vid_url)
        sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.ssa")
        website.upload_subtitles(self,sel,sub_file)
        local_url = sel.get_attribute(testvars.video_original +" > a@href")
        SiteLogout(self,sel)
    return local_url
def get_video_no_translations(self,sel):
    """Get the url of the video page for a video that has translations.

    Returns: video_url
    """
    sel.open("videos/")
    sort_videos_table(self,sel,"Subtitles and Translations","asc") 
    row_no = random.randint(1,6)
    local_url = "none"
    
    subtitled_cell="css=tr:nth-child("+str(row_no)+") > "+testvars.videos_trans_td
    while sel.is_element_present(subtitled_cell):
        if int(sel.get_text(subtitled_cell)) == 0:
            local_url = sel.get_attribute("css=tr:nth-child("+str(row_no)+ ") > "+testvars.videos_url_td+"href")
            break
        row_no = row_no + 1
        subtitled_cell=("css=tr:nth-child("+str(row_no)+") > "+testvars.videos_trans_td)
        
    if local_url == "none":
        print "no untranslated vidoes - must add one."
        local_url = submit_random_youtube(self,sel)
        
    return local_url

def submit_random_youtube(self,sel):
    vid_url = offsite.get_youtube_video_url(self)
    submit_video(self,sel,vid_url)
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    local_url = sel.get_attribute(testvars.video_original +"@href")
    return local_url

def get_translated_lang(self,sel):
    """Locate a language (not metadata or original) tab for a video.

    Need to exclude Original, Video Info, and Metadata
    """
    #get the original language
    original_lang = sel.get_text(testvars.video_original)
    tab_no = 1
    tab_li = "css=ul.left_nav li:nth-child("+str(tab_no)+") > a "
    skip_list = [original_lang, "Video Info", "Metadata: Twitter", "Metadata: Geo", "Metadata: Wikipedia"]
    while sel.is_element_present(tab_li):        
        if sel.get_text(tab_li) not in skip_list:
            test_lang = sel.get_text(tab_li).split('(') # Split off the number of lines
            break
        tab_no = tab_no + 1
        tab_li = "css=ul.left_nav li:nth-child("+str(tab_no)+") > a"
    lang = test_lang[0].rstrip()
    print lang
    return lang

def upload_subtitles(self,sel,sub_file,lang="en"):
    """Uploads subtitles for the specified language."

    """
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.video_upload_subtitles)
    sel.click(testvars.video_upload_subtitles)
    sel.select("css=form[id='upload-subtitles-form'] select", "value="+lang)
    sel.type("subtitles-file-field",sub_file)


def verify_sub_upload(self,sel,sub_file,lang=""):
    """Verifies the uploaded subtitle text matches the text of a corresponing test file.

    """
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sub_td = 1
    for line in codecs.open(sub_file,encoding='utf-8'):
        subline = line.split(',')
        sub = subline[0].rstrip()
        self.assertTrue("css=tr:nth-child("+str(sub_td)+") > td.last:contains("+sub+")")
        sub_td = sub_td + 1
    if lang == "":
        sublang = (sel.get_text("css=li.full.active a").split('(')) # split off the number of lines
        self.assertEqual(sublang[0].rstrip(),"English")
    else:
        sublang = (sel.get_text("css=li.full.active a").split('(')) # split off the number of lines
        self.assertEqual(sublang[0].rstrip(),lang)

def verify_subs(self,sel,sub_file):
    """Compares the displayed text for subtitles in the to the input file.

    """
    print " * verifying subtitle text"
    sub_td = 1
    for line in codecs.open(sub_file,encoding='utf-8'):
        subline = line.split(',')
        sub = subline[0].rstrip()
        self.assertTrue("css=tr:nth-child("+str(sub_td)+") > td div.sub_content:contains("+sub+")")
        sub_td = sub_td + 1

def store_subs(self,sel,modify=False,limit=True):
    """reads each line of subs and saves to a file for later use.

    """
    f = codecs.open("subs.txt", "w",encoding='utf-8')
    sub_td = 1
    while sel.is_element_present("css=tr:nth-child("+str(sub_td)+")"):
        subline = sel.get_text("css=tr:nth-child("+str(sub_td)+") > td div.sub_content")
        if modify==True:
            subline=subline.upper()
        f.write(subline+ "\n")
        sub_td = sub_td + 1
    f.close

def translate_video(self,sel,url=None,lang=None):
    """Given the local url of a video, adds a translation.
        
    """
    if url == None:
        print "adding translation from current page"
    else:
        print "opening video page to translate"
        sel.open(url)
    self.assertTrue(sel.is_element_present("css=a#add_translation"),"add translation button not found")
    sel.click(testvars.video_add_translation)

    

def sort_videos_table(self,sel,column,order):
    """Sort the videos table by the specified heading in the specified order

    Current column headings are: URL, Pageloads, Subtitles Fetched, Translations, Subtitled?
    Order can be 'asc' or 'desc'

    """
    sel.click("link="+column)
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if sel.is_element_present("css=a."+order+":contains("+column+")"):
        sel.click("link="+column)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if order == "asc":
        self.assertTrue(sel.is_element_present("css=a.desc:contains("+column+")"),"sort not correct")
    if order == "desc":
        self.assertTrue(sel.is_element_present("css=a.asc:contains("+column+")"),"sorted by desc")


def enter_comment_text(self,sel,comment):
    """Enter text in the Comments box and submit

    Assumes user is on the comments tab
    """
    self.assertTrue(sel.is_element_present("css=li.active a span:contains('Comments')"))
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
    #give it 3 seconds to post
    print "* Verify Comment"
    time.sleep(5)
    if result == "posted":
        posted_text = sel.get_text("css=ul.comments.big_list li:nth-child(1) > div.info p")
        self.assertEqual(posted_text.strip(),comment.strip(),"posted text doesn't match expected text")
    elif result == "too long":
        self.assertTrue(sel.is_element_present("css=p.error_list:contains('Ensure this value has at most 3000 characters')"), \
                        "too long message not found")
    elif result == "login":
        self.assertTrue(sel.is_element_present("css=.login-for-comment:contains('Login to post a comment')"), \
                        "login message not present")
        if sel.is_element_present("css=ul.comments.big_list li:nth-child(1) > div.info p"):
            self.assertNotEqual(sel.get_text("css=ul.comments.big_list li:nth-child(1) > div.info p"),"comment", \
                                "comment posted without login")

def check_the_box(self,sel,row_num):
    """Check or uncheck the box in the revision history table.

    returns the attribute in case we need it.

    """
    myval = sel.get_attribute("//div[@id='revisions-tab']/table/tbody/tr["+str(row_num)+"]/td[1]/input@value")
    sel.click("//input[@value="+myval+"]") #check the box
    return myval

def get_current_rev(self,sel):
    """Returns the most current revision number for a videos subtitles or translation.
    
    Assumes you have the video's page open and are on the history tab.
    """
    myval = sel.get_text("//div[@id='revisions-tab']/table/tbody/tr[1]/td[1]")
    
    revision = myval.split()[0]
    return revision

def verify_latest_history(self,sel,rev=None,user=None,time=None,text=None):
    print "verifying history tab contents"
    mslib.wait_for_element_present(self,sel,testvars.history_tab)
    sel.click(testvars.history_tab)
    mslib.wait_for_element_present(self,sel,"css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(1) > a")
    if rev:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(1) > a:contains('"+rev+"')"))
    if user:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(2) > a:contains('"+user+"')"))
    if time:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(4):contains('"+time+"')"))
    if text:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(5):contains('"+text+"')"))


def get_diff_url(self,sel,rev_link):
    """Gets the url id of a revision for comparing.

    """
    sel.click(rev_link)
    mslib.wait_for_element_present(self,sel,"css=ul.breadcrumb li a:contains('Revision History')")
    d = sel.get_eval("window.location")
    diff_id = d.split('/')[-1]
    sel.click("css=ul.breadcrumb li a:contains('Revision History')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    return diff_id

def verify_compare_revisions(self,sel,older_rev, newer_rev,rollback=False):
    """Verifies contents of page comparing 2 revisions.

    compares the older rev and newer rev numbers.

    """
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    print "older_rev: "+str(older_rev)+" newer_rev: "+str(newer_rev)
    #Verify the heading
    self.assertTrue(sel.is_element_present("css=h2.main-title:contains('#"+str(older_rev)+"')"))
    self.assertTrue(sel.is_element_present("css=h2.main-title:contains('#"+str(newer_rev)+"')"))
    #Verify left column - older
    self.assertTrue(sel.is_element_present("css=div.left_column h3.diff_title:contains('Revision #"+str(older_rev)+"')"))
    self.assertTrue(sel.is_element_present("css=div.left_column div.revision_buttons a.new_edit:contains('Submit a new edit based on this version (#"+str(older_rev)+")')"))
    #Verify right column - newer
    self.assertTrue(sel.is_element_present("css=div.right_column h3.diff_title:contains('Revision #"+str(newer_rev)+"')"))
    self.assertTrue(sel.is_element_present("css=div.right_column div.revision_buttons a.new_edit:contains('Submit a new edit based on this version (#"+str(newer_rev)+")')"))

    #Back to history tab, by clicking breadcrumb link
    if rollback==True:
        rollback_revision(self,sel)
    else:
        sel.click("css=ul.breadcrumb li a:contains('Revision History')")
        sel.wait_for_page_to_load(testvars.timeout)

def rollback_revision(self,sel):
    mslib.wait_for_element_present(self,sel,testvars.rev_rollback)
    sel.click(testvars.rev_rollback)
    self.assertEqual("Subtitles will be rolled back to a previous version", sel.get_confirmation())
    sel.wait_for_page_to_load(testvars.timeout)


def create_team(self,sel,team,team_logo):
    sel.type_keys("id_name", team+" ")
#    sel.type_keys("id_slug", team)
    sel.type("id_description", "Team "+team+ " - for test purposes only.")
#    sel.type("id_logo", team_logo)
    if "iexplore" in selvars.set_browser():
        vid_url = "http://blip.tv/file/1077145/"
    else:
        vid_url = "http://blip.tv/file/get/Miropcf-Miro20Introduction771.ogv"
    sel.type("id_video_url", vid_url )  
    sel.click("css=.green_button.big:contains('Create Team')")
    sel.wait_for_page_to_load(testvars.timeout)
    # Verify team creation parameters
    current_video = vid_url.split('/')[-1]
    try:
        if team == "":
            self.assertTrue(sel.is_element_present("css=ul.errorlist li:contains('This field is required')"))
        else:
            self.assertEqual(str(team), str(sel.get_value("id_name")))
            self.assertEqual("Team "+str(team)+" - for test purposes only.", str(sel.get_value("id_description")))
#            self.failUnless(sel.is_element_present("css=.avatar-container img[src*='png_100x100']")) comment out until png bug fixed
            self.failUnless(sel.is_element_present("css=p:contains(\"Current video:\") > a:contains("+current_video+")"))       
    except AssertionError, e: self.verificationErrors.append(str(e))

def get_own_team(self,sel):
    open_teams_page(self,sel)
    if sel.is_element_present("css=h4 a:contains('your team')"):
        print 'using existing team'
        t = sel.get_text("css=h4 a:contains('your team')")
        team = t.split('(')[0]
        team = team.rstrip()
        
    else:
        print "creating new team"
        team = "miro"+time.strftime("%m%d%H%M%S", time.gmtime())
        team_logo_path = os.path.join(testvars.MSTestVariables["DataDirectory"],"sheep.png")
        sel.click(testvars.start_team)
        sel.wait_for_page_to_load(testvars.timeout)
        create_team(self,sel,team,team_logo_path)
    return team

def save_team_settings(self,sel):
    sel.click("css=.green_button.small:contains('Save')")

def open_teams_page(self,sel):
    sel.open("teams")
    
def search_teams(self,sel,team):
    """Search for the given team name.

    Assumes using the url query string
    """
    sel.open("/teams/?q="+team)
    
    


def handle_error_page(self,sel,test_id):
    sel.select_frame("relative=top")
    if sel.is_element_present("css=h2:contains('when you encountered this error.')") or sel.is_element_present("css=h2:contains('Sorry')"):
        sel.type("feedback_email", testvars.gmail)
        feedback_math = sel.get_text("css=form p + p label")
        s = feedback_math[20:25]
        sel.type("feedback_math_captcha_field", eval(s))
        sel.type("feedback_message", "test_id: "+test_id+" sel-rc automated test encountered an error \n Prove You are Human.")
        sel.click("css=button.green_button")
        self.verificationErrors.append("submitted error to feedback")
        print "submitted error to feedback form: "+ str(test_id)
        



