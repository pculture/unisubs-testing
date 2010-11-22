from selenium import selenium

import unittest
import time
import re
import codecs
import mslib
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
    sel.open("/demo/")
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
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    
def front_page_submit(self,sel,url):
    sel.open("/")
    sel.type("css=input[name=video_url]", url)
    sel.click("css=button:contains('Go')")


def start_sub_widget(self,sel,wig_menu=testvars.WebsiteUI["SubtitleMe_menu"],skip="True",vid_lang="English",sub_lang="English"):
    """Start the Subtitle Widget using the Subtitle Me menu.

    This will handle the language choice for demo or submitted videos.
    skip is set to true by default and gets passed to widget.close_howto_video
    to prevent further how-to video displays.

    Pre-condition: On a page where Subtitle Me menu is present. Video with no subs.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
    sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
    time.sleep(5)
    if sel.is_element_present(testvars.WidgetUI["Select_language"]):
        widget.select_video_language(self,sel,vid_lang,sub_lang)
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
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    vid_embed = None
    vid_css = "css=div[id=widget_div] object"
    html5_el = "css=div[id=widget_div] video"
    mslib.wait_for_element_present(self,sel,vid_css)
    if embed_type == "flow":
        self.assertTrue(sel.is_element_present(vid_css+"[data*='flowplayer']"))
    elif embed_type == "youtube":       
        self.assertTrue(sel.is_element_present(vid_css+"[data*='youtube.com']"))
    elif embed_type == 'vimeo':      
        self.assertTrue(sel.is_element_present(vid_css+"[data*='moogaloop.swf']"))
    elif embed_type == 'dailymotion':      
        self.assertTrue(sel.is_element_present(vid_css+"[id$='_dailymotionplayer']"))
    else:
        if sel.is_element_present(vid_css+"[data*='flowplayer']"):
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
    row_no = 1
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
    row_no = 1
    local_url = "none"
    
    subtitled_cell="css=tr:nth-child("+str(row_no)+") > "+testvars.videos_trans_td
    while sel.is_element_present(subtitled_cell):
        if int(sel.get_text(subtitled_cell)) == 0:
            local_url = sel.get_attribute("css=tr:nth-child("+str(row_no)+ ") > "+testvars.videos_url_td+" > a@href")
            break
        row_no = row_no + 1
        subtitled_cell=("css=tr:nth-child("+str(row_no)+") > "+testvars.videos_trans_td)
        
    if local_url == "none":
        print "no untranslated vidoes - must add one."
        vid_url = offsite.get_youtube_video_url(self)
        submit_video(self,sel,vid_url)
 #       widget.select_video_language(self,sel)
 #       widget.close_howto_video(self,sel)
 #       widget.close_widget(self,sel)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        local_url = sel.get_attribute(testvars.video_original +" > a@href")
        
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
    return test_lang[0].rstrip()

def upload_subtitles(self,sel,sub_file,lang="English"):
    """Uploads subtitles for the specified language."

    """
    mslib.wait_for_element_present(self,sel,testvars.video_upload_subtitles)
    sel.click(testvars.video_upload_subtitles)
    sel.select("css=form[id='upload-subtitles-form'] select", "label="+lang)
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
    """Compares the displayed text for subtitles in the history table to the input file.

    """
    sub_td = 1
    for line in codecs.open(sub_file,encoding='utf-8'):
        subline = line.split(',')
        sub = subline[0].rstrip()
        self.assertTrue("css=tr:nth-child("+str(sub_td)+") > td div.sub_content:contains("+sub+")")
        sub_td = sub_td + 1

def store_subs(self,sel):
    """reads each line of subs and saves to a file for later use.

    """
    f = open("subs.txt", "w")
    sub_td = 1
    while sel.is_element_present("css=tr:nth-child("+str(sub_td)+") > td div.sub_content"):
        subline = sel.get_text("css=tr:nth-child("+str(sub_td)+") > td div.sub_content")
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


def get_current_rev(self,sel):
    """Returns the most current revision number for a videos subtitles or translation.
    
    Assumes you have the video's page open and are on the history tab.
    """
    revision = sel.get_text("css=tr td:nth-child(1) > a")
    return revision

def verify_latest_history(self,sel,rev=None,user=None,time=None,text=None):
    print "verifying history tab contents"
    mslib.wait_for_element_present(self,sel,testvars.history_tab)
    sel.click(testvars.history_tab)
    if rev:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(1) > a:contains('"+rev+"')"))
    if user:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(2) > a:contains('"+user+"')"))
    if time:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(4):contains('"+time+"')"))
    if text:
        self.assertTrue(sel.is_element_present("css=div[id=revisions-tab] tr:nth-child(1) > td:nth-child(5):contains('"+text+"')"))


def handle_error_page(self,sel,test_id):
    sel.select_window("null") #just making sure I'm really here, if I am.
    sel.select_frame("relative=top")
    if sel.is_element_present("css=h2:contains('when you encountered this error.')"):
        sel.type("feedback_email", testvars.gmail)
        feedback_math = sel.get_text("css=form p + p label")
        s = feedback_math[20:25]
        sel.type("feedback_math_captcha_field", eval(s))
        sel.type("feedback_message", "test_id: "+test_id+" sel-rc automated test encountered an error \n Prove You are Human.")
        sel.click("css=button[type='submit']")
        print "submitted error to feedback form: "+ str(test_id)
        



