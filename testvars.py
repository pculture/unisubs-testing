preE=" --- ERROR: "

vlocalhost = "localhost"
vbrowser = "*chrome"

MSTestVariables = {"Site":"http://staging.universalsubtitles.org/", \
                   "ResultOutputDirectory":r"Results/", \
                   "DataDirectory":r"TestInput/", \
                   "TimeOut":"90000", \
                  }

# Mapping to the MiroSubs website UI navigations buttons and links

WebsiteUI = {"Home":"css=a:contains('Miro Subs Alpha')", \
             "Login_Button":"css=.login_link span:contains('Login')", \
             "Logout_Button":"css=.login_link span:contains('Logout')", \
             "Subtitle_Button":"css=a:contains('Subtitle a Video')", \
             "All_Videos_Button":"css=a:contains('All Videos')", \
             "About_Button":"css=a:contains('About')", \
             "FAQ_Button":"css=a:contains('FAQ')", \
             "Search_Button":"css=a:contains('Search')", \
             "Video_Submit_Button":"//button[@value='Begin']", \
             "SubtitleMe_menu":"css=.mirosubs-tabText", \
             "SubMe_menuitems":"css=.mirosubs-langmenuitem-content", \
             "AddSubtitles_menuitem":"css=.mirosubs-langmenuitem-content:contains('Add Subtitles')" ,\
             "Login_menuitem":"css=.mirosubs-langmenuitem-content:contains('Login')" ,\
             "Logout_menuitem":"css=.mirosubs-langmenuitem-content:contains('Logout')" , \
             "ChooseLanguage_menu":"css=.mirosubs-tabText:contains('Choose language')" , \
             
          }

WidgetUI = {"Video_playPause":"css=.mirosubs-playPause", \
            "Video_play_button":"css=.mirosubs-videoControls .play", \
            "Video_pause_button":"css=.mirosubs-videoControls .pause", \
            "Video_elapsed_time":"css=.mirosubs-timeElapsed", \
            "Transcribe_current_sub":"css=.mirosubs-captionDiv", \
            "Next_step":"css=.mirosubs-done", \
            "Play_pause":"css=.mirosubs-tab:contains('tab')",\
            "Sync_sub":"css=.mirosubs-down:contains('down')",\
            "Skip_back":"css=.mirosubs-control:contains('ctrl')",\
            "Active_subtime":"css=li.active span.mirosubs-timestamp-time",\
            "Active_subtext":"css=li.active span.mirosubs-title",\
            "Must_Login":"css=.mirosubs-needLogin", \
    
        }

# TestData

siteuser = "sub_writer"
twitteruser = "pcfsubwriter"
openiduser = "http://pcf-sub-writer.myopenid.com"
gmailuser = "pcf.subwriter"
passw = "sub.writer"

eels_fr = u'Mon a\u00E9roglisseur est plein d\'anguilles'
eels_jp = u'\u79C1\u306E\u30DB\u30D0\u30FC\u30AF\u30E9\u30D5\u30C8\u306F\u9C3B\u3067'


