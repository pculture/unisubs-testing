import os
import platform

preE=" --- ERROR: "

vlocalhost = "localhost"
vbrowser = "*chrome"
down_arrow_key = u'\u2193'

MSTestVariables = {"Site":"http://dev.universalsubtitles.org/", \
                   "ResultOutputDirectory":os.path.join(os.getcwd(), "Results"), \
                   "DataDirectory": os.path.join(os.getcwd(), "TestInput"), \
                   "TimeOut":"190000", \
                  }

# Mapping to the MiroSubs website UI navigations buttons and links

WebsiteUI = {"Home":"css=a:contains('Miro Subs Alpha')", \
             "Login_Button":"css=.login_link span:contains(\"Login\")", \
             "Logout_Button":"css=.login_link span:contains('Logout')", \
             "SiteLogoutUrl": MSTestVariables["Site"]+"""logout/?next=/""",\
             "Subtitle_Button":"css=a:contains('Subtitle a Video')", \
             "All_Videos_Button":"css=a:contains('All Videos')", \
             "About_Button":"css=a:contains('About')", \
             "FAQ_Button":"css=a:contains('FAQ')", \
             "Search_Button":"css=a:contains('Search')", \
             "Video_Submit_Button":"//button[@value='Begin']", \
             "SubtitleMe_menu":"css=.mirosubs-tabTextchoose", \
             "SubMe_menuitems":"css=.mirosubs-langmenuitem-content", \
             "AddSubtitles_menuitem":"css=.mirosubs-improveSubtitles" ,\
             "Login_menuitem":"css=.mirosubs-createAccount" ,\
             "Logout_menuitem":"css=.mirosubs-langmenuitem-content:contains('Logout')" , \
             "ChooseLanguage_menu":"css=.mirosubs-tabText:contains('Choose language')" , \
             
          }

WidgetUI = {"Video_playPause":"css=.mirosubs-playPause", \
            "Video_play_button":"css=.mirosubs-videoControls .play", \
            "Video_pause_button":"css=.mirosubs-videoControls .pause", \
            "Video_elapsed_time":"css=.mirosubs-timeElapsed", \
            "Current_playing_sub":"css=.mirosubs-captionDiv", \
            "Next_step":"css=.mirosubs-done", \
            "Translate_now_button":"css=.mirosubs-done:contains(\"Add a Translation Now\")", \
            "Play_pause":"css=.mirosubs-tab:contains('tab')",\
            "Sync_sub":"css=.mirosubs-down:contains('down')",\
            "Skip_back":"css=.mirosubs-control:contains('shift')",\
            "Active_subtime":"css=li.active span.mirosubs-timestamp-time",\
            "Active_subtext":"css=li.active span.mirosubs-title",\
            "Must_Login":"css=.mirosubs-needLogin:contains('LOGIN')", \
            "Close_widget":"css=.mirosubs-modal-widget-title-close", \
    
        }

# TestData

siteuser = "sub_writer"
twitteruser = "pcfsubwriter"
openiduser = "http://pcf-sub-writer.myopenid.com"
gmailuser = "pcf.subwriter"
passw = "sub.writer"

eels_fr = u'Mon a\u00E9roglisseur est plein d\'anguilles'
eels_jp = u'\u79C1\u306E\u30DB\u30D0\u30FC\u30AF\u30E9\u30D5\u30C8\u306F\u9C3B\u3067'




