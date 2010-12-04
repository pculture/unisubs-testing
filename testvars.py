# -*- coding: utf-8 -*-
import os
import platform

preE=" --- ERROR: "


MSTestVariables = {"DataDirectory": os.path.join(os.getcwd(), "TestInput"), \
                   "TimeOut":"120000", \
                  }

# Mapping to the MiroSubs website UI navigations buttons and links

WebsiteUI = {"Home":"css=a:contains('Miro Subs Alpha')", \
             "Login_Button":"css=a[href*=/auth/login]", \
             "Logout_Button":"css=a[href*=/logout]", \
             "SiteLogoutUrl": "/logout/?next=/",\
             "Subtitle_Button":"css=a[href=/videos/create/]", \
             "All_Videos_Button":"css=a:contains('All Videos')", \
             "About_Button":"css=a:contains('About')", \
             "FAQ_Button":"css=a:contains('FAQ')", \
             "Search_Button":"css=a:contains('Search')", \
             "Video_Submit_Button":"//button[@value='Begin']", \
             #widget menu displayed on website
             "SubtitleMe_menu":"css=.mirosubs-tabTextchoose", \
             "SubMe_menuitems":"css=.mirosubs-langmenuitem-content", \
             "AddSubtitles_menuitem":"css=.mirosubs-improveSubtitles" ,\
             "Subhomepage_menuitem":"css=.mirosubs-subtitleHomepage" ,\
             "Login_menuitem":"css=.mirosubs-createAccount" ,\
             "Logout_menuitem":"css=.mirosubs-langmenuitem-content:contains('Logout')" , \
             "ChooseLanguage_menu":"css=.mirosubs-tabText:contains('Choose language')" ,
             
          }

# Website Videos page
videos_url_td = "td:nth-child(1)"
videos_trans_td = "td:nth-child(4)"
videos_subtitled_td = "td:nth-child(5)"
video_original = "css=ul.left_nav li:nth-child(2) > a"
video_metadata = "css=ul.left_nav li a[href:contains('meta-')]"
video_video_info = "css=li a:contains('Video Info')"
## action links
video_upload_subtitles = "css=a[id=upload-subtitles-link]"
video_edit_subtitles = "css=a[id=edit_subtitles]"
video_add_translation = "css=a[id=add_translation]"
video_compare_revisions = "css=button span:contains('Compare Revisions')"
rev_rollback = "css=a.roll_back"


history_tab = "css=span.inline_text:contains('History')"
comments_tab = "css=span.inline_text:contains('Comments')"
transcripts_tab = "css=.inline_text:contains('Subtitles')"


WidgetUI = {"Video_playPause":"css=.mirosubs-playPause", \
            "Video_play_button":"css=.mirosubs-playPause.play", \
            "Video_pause_button":"css=.mirosubs-playPause.pause", \
            "Video_elapsed_time":"css=.mirosubs-timeElapsed", \
            "Current_playing_sub":"css=.mirosubs-captionDiv", \
            "Next_step":"css=.mirosubs-done", \
            "Translate_now_button":"css=a#add_translation"
, \
            "Play_pause":"css=.mirosubs-tab:contains('tab')",\
            "Sync_sub":"css=span:contains('Tap when next subtitle')",\
            "Skip_back":"css=.mirosubs-control:contains('shift')",\
            "Active_subtime":"css=li.active span.mirosubs-timestamp-time",\
            "Active_subtext":"css=li.active span.mirosubs-title",\
            "Must_Login":"css=.mirosubs-needLogin a", \
            "Select_language":"css=h3:contains('Add subtitles')", \
            "Close_widget":"css=span[class=mirosubs-modal-widget-title-close]"    
        }
widget_steps = "css=.mirosubs-help-heading li a"
widget_step3 = "css=.mirosubs-help-heading li a:contains('3')"
widget_step2 = "css=.mirosubs-help-heading li a:contains('2')"
widget_step1 = "css=.mirosubs-help-heading li a:contains('1')"

# TestData

siteuser = "sub_writer"
twitteruser = "pcfsubwriter"
openiduser = "http://pcf-sub-writer.myopenid.com"
gmailuser = "pcf.subwriter"
passw = "sub.writer"
gmail = "pcf.subwriter@gmail.com"

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


