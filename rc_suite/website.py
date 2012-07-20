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
import base64


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
        auth_link = "css=a#twitter.provider"
    elif auth_type == "open-id":
        auth_link = "css=a#open-id.provider"
    elif auth_type == "google":
        auth_link = "css=a#google.provider"
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
    sel.open("/demo/")
#   Workaround if demo page breaks
##    if "iexplore" in selvars.set_browser():
##        submit_video(self,sel,"http://www.youtube.com/watch?v=Q1kAhWZ1hiA")
##    else:
##        submit_video(self,sel,"http://videos.mozilla.org/firefox/3.5/switch/switch.ogv")

def submit_video(self,sel,url,login=True):
    """Description: Submit a video using the site button.

    After the video is submitted, check if it is already in the db, and if so, delete and resubmit to assure
    a fresh state for testing.

    Pre-condition: site page is opened

    Post-condition: the widget is launched immediately.
    You'll need to deal with the help video, see widget.close_howto_video
    """
    print "* Submit Video"
    if "verify_age" in url:
        submitted = False
    else:
        sel.open("/")
        sel.click(testvars.WebsiteUI["Subtitle_Button"])
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,"css=form.main_video_form input#submit_video_field.main_video_form_field")
        sel.type("video_url", url)
        sel.click(testvars.WebsiteUI["Video_Submit_Button"])
        sel.wait_for_page_to_load(testvars.timeout)
        if sel.is_element_present("css=ul.errorlist"):
            submitted = False
        else:
            submitted = True
            if str(sel.get_text(testvars.WebsiteUI["SubtitleMe_menu"])) != "Subtitle Me":
                ## Delete and resubmit the video
                curr_url = sel.get_eval("window.location")
                admin_delete_video(self,sel,curr_url)
                if login == True:
                    SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
                sel.open("/videos/create")
                sel.type("video_url", url)
                sel.click(testvars.WebsiteUI["Video_Submit_Button"])
                sel.wait_for_page_to_load(testvars.timeout)
    return submitted      

    
def front_page_submit(self,sel,url):
    sel.open("/")
    sel.type("css=div#subtitle form input", url)
    sel.click("css=div#subtitle button.button:contains('Subtitle')")
    sel.wait_for_page_to_load(testvars.timeout)


def start_sub_widget(self,sel,skip="True",edit_type='orig',sec_lang=None,login=False):
    """Start the Subtitle Widget using the Subtitle Me menu.

    This will handle the language choice for demo or submitted videos.
    skip is set to true by default and gets passed to widget.close_howto_video
    to prevent further how-to video displays.

    Choice for edit_type: orig, trans_orig, trans_other (requires sec_lang), forkit.

    Pre-condition: On a page where the widget is present. Video with or without subs.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    sel.window_maximize()
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
    time.sleep(5)
    sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
    time.sleep(5)
    if sel.is_element_present(testvars.WidgetUI["Select_language"]) == False:
        if sel.is_element_present(testvars.WebsiteUI["AddSubtitles_menuitem"]):
            sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])
        elif sel.is_element_present(testvars.WebsiteUI['NewTranslation_menuitem']):
            sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])
        else:
            print "widget opened"
            widget.close_howto_video(self,sel)
            mslib.wait_for_element_present(self,sel,"css=.unisubs-help-heading")
    time.sleep(5)
    if sel.is_element_present(testvars.WidgetUI["Select_language"]):
        if edit_type == 'orig':
            widget.starter_dialog_edit_orig(self,sel)
        elif edit_type == 'trans_orig':
            widget.starter_dialog_translate_from_orig(self,sel)
        elif edit_type == 'trans_other':
            if sec_lang == None:
                self.fail("must provide from lang code in sec_lang")
            else:
                widget.starter_dialog_translate_from_not_orig(self,sel,from_lang=sec_lang)
        elif edit_type == 'forkit':
            widget.starter_dialog_fork(self,sel)
        else:
            print "not sure what I'm doing in started dialog"
    else:
        print "widget opened immediately"
        widget.close_howto_video(self,sel)
        mslib.wait_for_element_present(self,sel,"css=.unisubs-help-heading")



def verify_login(self,sel,username="sub_writer"):
    """
    Description: Verifies user is logged in by finding the logout button on the
    website and then starting the demo and looking for logout menu item on the
    Subtitle Me button.

    Pre-Condition: must be logged into site.

    """
    mslib.wait_for_element_present(self,sel,"css=li[id=me_menu]")
    self.failUnless(sel.is_element_present("css=div[id=menu_name]:contains('"+username+"')"),\
                    "user not logged in, user_panel not displayed")
## Commented this out - post 0.9.3 not showing name of logged in user
##    print "logged in as: " + sel.get_text("css=.user_panel a")
##    self.failUnless(sel.is_element_present("css=.user_panel a:contains("+username+")"),\
##                    "username: "+username+ " not found. Got "+ sel.get_text("css=.user_panel a"))





def verify_submitted_video(self,sel,vid_url,embed_type=None):
    """
    Description: Verifies the contents of the main video page of a submitted video.
    Require's the original url and expected type of embed.  Assumes html5 video if not specified.

    embed_type one of 'youtube', 'flow' 'html5' (default)

    Returns: url of the video on the universalsubtitles site.
    """
    print " * verify submitted video, embed type"
    vid_embed = None
    vid_span_css = "css=span.unisubs-videoplayer object"
    vid_div_css = "css=span.unisubs- div object"
    html5_el = "css=div[id=widget_div] video"
    mslib.wait_for_element_present(self,sel,"css=div[id=widget_div]")
    if embed_type == "flow":
        self.assertTrue(sel.is_element_present("css=object[data*='flowplayer']"))
    elif embed_type == "youtube":
        self.assertTrue((sel.is_element_present(vid_span_css+"[data*='youtube.com']")) or \
                        sel.is_element_present("css=div.unisubs-widget iframe[src*='youtube.com']"))
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
        
   
    self.assertTrue(sel.is_element_present("css=.unisubs-embed"),\
                    "no embed code present")
    unisubs_link = sel.get_text("css=.unisubs-permalink[href]")
    print sel.get_text("css=.unisubs-embed")
    return unisubs_link

def get_video_with_translations(self,sel):
    """Get the url of the video page for a video that has translations.

    Returns: video_url
    """
    sel.open("videos/")
    sort_videos_table(self,sel,"Subtitles and Translations","desc") 
    row_no = random.randint(1,3)
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
        upload_subtitles(self,sel,sub_file)
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
    submitted = False
    while submitted == False:
        vid_url = offsite.get_youtube_video_url(self)
        submitted = submit_video(self,sel,vid_url)
        aaa = testvars.video_original +"@href"
        local_url = sel.get_attribute(testvars.video_original +"@href")
    return local_url

def get_translated_lang(self,sel):
    """Locate a language (not metadata or original) tab for a video.

    Need to exclude Original, Video Info, and Metadata
    """
    #get the original language
    original_lang = sel.get_text(testvars.video_original)
    tab_no = 2
    tab_li = "css=ul#subtitles-menu li:nth-child("+str(tab_no)+") > a "
    skip_list = [original_lang, "Metadata: Twitter", "Metadata: Geo", "Metadata: Wikipedia"]
    while sel.is_element_present(tab_li):        
        if sel.get_text(tab_li) not in skip_list:
            test_lang = sel.get_text(tab_li).split('(') # Split off the number of lines
            break
        tab_no = tab_no + 1
        tab_li = "css=ul#subtitles-menu li:nth-child("+str(tab_no)+") > a"
    lang = test_lang[0].rstrip()
    print lang
    return lang

def upload_subtitles(self,sel,sub_file,lang="en"):
    """Uploads subtitles for the specified language."

    """
    view_video_link = "css=div.content div.grid_4 h2.main-title a"
#    if sel.is_element_present(view_video_link):    
#        sel.click(view_video_link)
#        time.sleep(15)
    if sel.is_element_present(testvars.video_back_to_main_page):    
        sel.click(testvars.video_back_to_main_page)
        time.sleep(15)
    mslib.wait_for_element_present(self,sel,testvars.video_upload_subtitles)
    sel.click(testvars.video_upload_subtitles)
    mslib.wait_for_element_present(self,sel,"css=form[id='upload-subtitles-form'] select")
    sel.select("css=form[id='upload-subtitles-form'] select[id='id_language']", "value="+lang)
    sel.type("css=div#upload-subtitles-div form#upload-subtitles-form div input#subtitles-file-field",sub_file)
    sel.click("css=div#upload-subtitles-div form#upload-subtitles-form div button.green_button")


def verify_sub_upload(self,sel,sub_file,lang=""):
    """Verifies the uploaded subtitle text matches the text of a corresponing test file.

    """
    mslib.wait_for_element_present(self,sel,"css=p.feedback-message")
    sel.click("css=div#upload_subs-div a.close")
    time.sleep(15)
    sel.refresh()
    time.sleep(3)
    mslib.wait_for_element_present(self,sel,testvars.video_original)
    sub_td = 1
    if lang == "":
        #assuming original lang if no lang specified.
        sel.click(testvars.video_original)
        sel.wait_for_page_to_load(testvars.timeout)
    else:
        sel.click(testvars.video_lang+":contains('"+lang+"')")
        sel.wait_for_page_to_load(testvars.timeout)
 
    for line in codecs.open(sub_file,encoding='utf-8'):
        subline = line.split(',')
        sub = subline[0].rstrip()
        self.assertTrue("css=tr:nth-child("+str(sub_td)+") > td.last:contains("+sub+")")
        sub_td = sub_td + 1
    
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
    while sel.is_element_present("css=tr:nth-child("+str(sub_td)+") > td div.sub_content"):
        subline = sel.get_text("css=tr:nth-child("+str(sub_td)+") > td div.sub_content")
        if modify==True:
            subline=subline.upper()
        f.write(subline+ "\n")
        sub_td = sub_td + 1
        if limit == True and sub_td == 10:
            break
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
    mslib.wait_for_element_present(self,sel,"css=th a:contains('"+column+"')")
    sel.click("css=th a:contains('"+column+"')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if sel.is_element_present("css=a."+order+":contains("+column+")"):
        print "already sorted: ",order
    else:
        sel.click("css=th a:contains('"+column+"')")
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if order == "desc":
        self.assertTrue(sel.is_element_present("css=a.desc:contains("+column+")"))
    if order == "asc":
        self.assertTrue(sel.is_element_present("css=a.asc:contains("+column+")"))


def click_lang_tab(self,sel,language):
    """Click on a lanugage tab.

    Assumes you are on the videos tab and know the lang you want.
    """
    mslib.wait_for_element_present(self,sel,testvars.video_lang+":contains('"+language+"')")
    sel.click(testvars.video_lang+":contains('"+language+"')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    self.failUnless(sel.is_element_present(testvars.video_lang_hd+":contains('"+language+"')"))


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
        time.sleep(10)
        sel.refresh()
        sel.wait_for_page_to_load(testvars.timeout)
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
    
    Assumes you have the video's page open, does not require history tab open.
    """
    myval = sel.get_text("css=div#languages-tab div.hd ul.inline_tabs li a[href=#revisions-tab] span.badgy_out span.badgy")
    revision = int(myval)-1
    return revision

def verify_latest_history(self,sel,rev=None,user=None,tm=None,text=None):
    print "verifying history tab contents"
    print rev
    time.sleep(10)
    sel.refresh()
    sel.wait_for_page_to_load(testvars.timeout)
    if sel.is_text_present("Most Recent") == False:
        sel.click(testvars.history_tab)
    mslib.wait_for_element_present(self,sel,"css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(1) > a")
    if rev:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(1) > a:contains('"+rev+"')"))
    if user:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(2) > a:contains('"+user+"')"))
    if time:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(4):contains('"+tm+"')"))
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
    print sel.get_eval("window.location")
    print "older_rev: "+str(older_rev)+" newer_rev: "+str(newer_rev)
    #Verify the heading
#    self.assertTrue(sel.is_text_present("#"+str(older_rev)))
#    self.assertTrue(sel.is_text_present("#"+str(newer_rev)))
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
    sel.type("id_description", "Team "+team+ " - for test purposes only.")
    sel.type("id_logo", team_logo)
    if "iexplore" in selvars.set_browser():
        vid_url = "http://blip.tv/file/1077145/"
    else:
        vid_url = "http://blip.tv/file/get/Miropcf-Miro20Introduction771.ogv"
    sel.type("id_video_url", vid_url )  
    sel.click("css=.green_button.big:contains('Create Team')")
    sel.wait_for_page_to_load(testvars.timeout)
    # Verify team creation parameters
    if team == "":
        self.assertTrue(sel.is_element_present("css=ul.errorlist li:contains('This field is required')"))
    else:
        self.assertEqual(str(team), str(sel.get_value("id_name")))
        self.assertEqual("Team "+str(team)+" - for test purposes only.", str(sel.get_value("id_description")))
        self.failUnless(sel.is_element_present("css=.avatar-container img[src*='png_100x100']")) 
        self.failUnless(sel.is_element_present("css=p:contains('Current video') > a:contains('blip')"))    

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

def teampage_lang_select(self,sel):
    time.sleep(3)
    if sel.is_text_present("What languages do you speak") == True:
        sel.click("css=div[id='language_picker'] + button")
        time.sleep(2)
        mslib.wait_for_text_not_present(self,sel,"Saving")

def handle_lang_select(self,sel):
    time.sleep(5)
    if sel.is_text_present("What languages do you speak") == True:
        sel.click("css=div[id='language_picker'] + button")
        time.sleep(2)
        mslib.wait_for_text_not_present(self,sel,"Saving")

def save_team_settings(self,sel):
    sel.click(testvars.teams_save)

def open_teams_page(self,sel):
    sel.open("teams")
    
def search_teams(self,sel,team):
    """Search for the given team name.

    Assumes using the url query string
    """
    sel.open("/teams/?q="+team)


def feature_video(self,sel,action='Feature'):
    """As an admin user, Feature or Unfeature a video.

    Assumes logged in as an admin user.
    Action can be 'Feature' or 'Unfeature'
    """
    mslib.wait_for_element_present(self,sel,"css=ul#admin-menu.left_nav li a:contains('eature')")
    if not sel.is_element_present("css=ul#admin-menu.left_nav li a:contains('"+action+"')"):
        print "video already",action
    else:
        sel.click("css=ul#admin-menu.left_nav li a:contains('eature')")
        mslib.wait_for_element_present(self,sel,"css=ul#admin-menu.left_nav li a:contains('eature')")
    vid_url = sel.get_attribute("css=ul#video-menu.left_nav li:nth-child(1) >  a@href")
    return vid_url


def admin_delete_video(self,sel,curr_url):
    """Completely delete a video from the site.

    """
    
    vid_id = curr_url.split('/videos/')[1]
    sel.open("/videos/"+vid_id+"staff/delete")
    if sel.is_element_present("id_username"):
        sel.type("id_username", base64.standard_b64decode(testvars.ad_usr))
        sel.type("id_password", base64.standard_b64decode(testvars.del_pw))
        sel.click("//input[@value='Log in']")
        sel.wait_for_page_to_load(testvars.timeout)
    sel.open("/admin/logout")
    time.sleep(5)
    sel.open("/")
    

def handle_error_page(self,sel,test_id):
    time.sleep(5)
    if sel.is_element_present("css=h2:contains('when you encountered this error.')") or sel.is_element_present("css=h2:contains('Sorry')"):
        sel.type("feedback_email", testvars.gmail)
        feedback_math = sel.get_text("css=form p + p label")
        s = feedback_math[20:25]
        sel.type("feedback_math_captcha_field", eval(s))
        sel.type("feedback_message", "test_id: "+test_id+" sel-rc automated test encountered an error \n Prove You are Human.")
        sel.click("css=button.green_button")
        self.verificationErrors.append("submitted error to feedback")
        print "submitted error to feedback form: "+ str(test_id)
        



