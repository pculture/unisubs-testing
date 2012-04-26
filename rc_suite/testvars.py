# -*- coding: utf-8 -*-
import os
import platform


timeout = 60000
MSTestVariables = {"DataDirectory": os.path.join(os.getcwd(), "TestInput"), \
                   "TimeOut":timeout, \
                  }

# Mapping to the MiroSubs website UI navigations buttons and links

WebsiteUI = {"Home":"css=a:contains('Miro Subs Alpha')", \
             "Login_Button":"css=li a:contains('Sign In')", \
             "Logout_Button":"css=li a[href*=logout]", \
             "SiteLogoutUrl": "en/logout/?next=/",\
             "Subtitle_Button":"css=li[id='nav_submit'] a", \
             "All_Videos_Button":"css=a:contains('All Videos')", \
             "About_Button":"css=a:contains('About')", \
             "FAQ_Button":"css=a:contains('FAQ')", \
             "Search_Button":"css=a:contains('Search')", \
             "Video_Submit_Button":"//button[@value='Begin']", \
             #widget menu displayed on website
             "SubtitleMe_menu":"css=.unisubs-tabTextchoose", \
             "SubMe_menuitems":"css=.unisubs-langmenuitem-content", \
             "AddSubtitles_menuitem":"css=a:contains('Improve These Subtitles')", \
             "NewTranslation_menuitem":"css=a:contains('Add New Translation')" ,\
             "Subhomepage_menuitem":"css=a:contains('Subtitle Homepage')" ,\
             "Login_menuitem":"css=.unisubs-createAccount" ,\
             "Logout_menuitem":"css=.unisubs-langmenuitem-content:contains('Logout')" , \
             "ChooseLanguage_menu":"css=.unisubs-tabText:contains('Choose language')" ,
             "FeedBack_button": "css=.feedback_tab"
             
          }

# Website Videos page
vid_title = "css=.main-title"
videos_url_td = "td:nth-child(1)"
videos_trans_td = "td:nth-child(4)"
videos_subtitled_td = "td:nth-child(5)"
#video_original = "css=ul#subtitles-menu li:nth-child(1) > a"
video_original = "css=body#video_profile.v1 > div.content > div.grid_4 > h2.main-title > a"
video_back_to_main_page = "css=body#video.v1 > div.content > div.grid_4 > h2.main-title > a"
video_lang = "css=ul#subtitles-menu li a"
video_lang_hd = "css=div#languages-tab div.hd h2"
video_metadata = "css=ul.#video-menu.left_nav li a[href:contains('meta-')]"
video_video_info = "css=ul#video-menu.left_nav li a:contains('Info')"
## action links
#video_upload_subtitles = "css=ul#video-menu.left_nav li.contribute a#upload-subtitles-link"
video_upload_subtitles = "css=div#video-tab.tab > div.clearboth > div.video-tools > p > a#upload-subtitles-link"
video_add_to_team = "css=ul#moderation-menu li div.sort_button span.sort_label:contains('Add video to team')"
video_edit_subtitles = "css=div#transcripts-tab div.actions a#edit_subtitles_button"
video_add_translation = "css=ul#video-menu.left_nav li.contribute a#add_translation"
video_compare_revisions = "css=div#revisions-tab.action_buttons button.compare_versions_button"
rev_rollback = "css=a.roll_back"


teams_link = "css=a span:contains('Teams')"
start_team = "css=a.green_button.big.start_team"
manage_team = "css=a:contains('Settings')"
## teams page
teams_video_tab ="css=ul.inline_tabs li a[href*='videos']"


history_tab = "css=a[href='#revisions-tab']"
comments_tab = "css=a[href='#comments-tab']"
info_comments_tab = "css=div.hd ul.inline_tabs li a span.inline_text:contains('Comments')"
transcripts_tab = "div#languages-tab css=.inline_text:contains('Subtitles')"

#teams pages
vid_add_subs_button = "css=ul.big_list li:nth-child(1) > div.info div.team-video-buttons-container a.blue_button"
teams_save = "css=button span:contains('Save')"

# Widget Vars

WidgetUI = {"Video_playPause":"css=.unisubs-playPause", \
            "Video_play_button":"css=.unisubs-playPause.play", \
            "Video_pause_button":"css=.unisubs-playPause.pause", \
            "Video_elapsed_time":"css=.unisubs-timeElapsed", \
            "Current_playing_sub":"css=div.unisubs-subtext", \
            "Transcribed_text":"css=div span.unisubs-captionSpan", \
            "Current_playing_offsite":"css=span.unisubs-captionSpan", \
            "Next_step":"css=.unisubs-done span", \
            "Translate_now_button":"css=a#add_translation"
, \
            "Play_pause":"css=div.unisubs-play span.unisubs-tab",\
            "Sync_sub":"css=div.unisubs-begin span.unisubs-down",\
          #  "Sync_sub":"css=span:contains('Tap when next subtitle')",\
            "Skip_back":"css=.unisubs-control:contains('shift')",\
            "Active_subtime":"css=li.active span.unisubs-timestamp-time",\
            "Active_subtext":"css=li.active span.unisubs-title",\
            "Must_Login":"css=.unisubs-needLogin a", \
            "Select_language":"css=h3:contains('Create')", \
            "Close_widget":"css=span[class=unisubs-modal-widget-title-close]"    
        }
widget_steps = "css=.unisubs-help-heading li a"
widget_step3 = "css=.unisubs-help-heading li a:contains('3')"
widget_step2 = "css=.unisubs-help-heading li a:contains('2')"
widget_step1 = "css=.unisubs-help-heading li a:contains('1')"

create_lang_unknown = "css=select.original-language"
create_lang_known = "css=div p:contains('This video is in ')"
create_subtitle_into = "css=select.to-language"
create_translate_from = "css=select.from-language"

#offsite option
offsite_goto_subs = "css=.unisubs-goBack"
offsite_goto_site = "css=.unisubs-otherClose"

# TestData

siteuser = "sub_writer"
twitteruser = "pcfsubwriter"
openiduser = "http://pcf-sub-writer.myopenid.com"
openid_username = "Subwriter"
gmailuser = "pcf.subwriter"
passw = "sub.writer"
gmail = "pcf.subwriter@gmail.com"
ad_usr = "amFuZXRQQ0Y="
del_pw = "bG92ZXMudW5pc3Vicw=="
eels_fr = u'Mon a\u00E9roglisseur est plein d\'anguilles'
eels_jp = u'\u79C1\u306E\u30DB\u30D0\u30FC\u30AF\u30E9\u30D5\u30C8\u306F\u9C3B\u3067'


one_char_comment_text = "d"
normal_comment_text = """Charles Robert Darwin FRS (12 February 1809 – 19 April 1882)
                      was an English naturalist[I] who established that all species
                      of life have descended over time from common ancestors, and proposed
                      the scientific theory that this branching pattern of evolution
                      resulted from a process that he called natural selection.
                      He published his theory with compelling evidence for evolution
                      in his 1859 book On the Origin of Species"""
html_comment_text = """<td colspan="2" style="text-align:center; padding-bottom:0.5em;">
    <a href="/wiki/File:Charles_Darwin_seated_crop.jpg" class="image" title="Charles Robert
    Darwin, aged 45 in 1854, by then working towards publication of On the Origin of Species.">
    <img alt="Three quarter length studio photo showing Darwin's characteristic large forehead
    and bushy eyebrows with deep set eyes, pug nose and mouth set in a determined look. He is
    bald on top, with dark hair and long side whiskers but no beard or moustache. His jacket is dark,
    with very wide lapels, and his trousers are a light check pattern. His shirt has an upright wing
    collar, and his cravat is tucked into his waistcoat which is a light fine checked pattern."
    src="http://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Charles_Darwin_seated_crop.jpg/250px-Charles_Darwin_seated_crop.jpg" width="250" height="329" />
    </a><br />
    <div style="padding-top:0.3em; line-height:1.2em;"><span style="">Charles Robert Darwin, aged 45 in 1854, by then working towards publication of
    <i><a href="/wiki/On_the_Origin_of_Species" title="On the Origin of Species"><span style="white-space:nowrap;">On the Origin of Species</span></a></i>.
    </span></div>
    </td> """


