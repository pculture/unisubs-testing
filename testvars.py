preE=" --- ERROR: "

MSTestVariables = {"Browser":"*chrome", \
                   "Site":"http://dev.universalsubtitles.org/", \
                   "ResultOutputDirectory":r"Results/", \
                   "DataDirectory":r"TestInput/", \
                   "TimeOut":"60000", \
                  }

# Mapping to the MiroSubs website UI navigations buttons and links

WebsiteUI = {"Home":"css=a:contains('Miro Subs Alpha')", \
             "Login_Button":"css=a:contains('Login')", \
             "Logout_Button":"css=a:contains('Logout')", \
             "Subtitle_Button":"css=a:contains('Subtitle Video')", \
             "All_Videos_Button":"css=a:contains('All Videos')", \
             "About_Button":"css=a:contains('About')", \
             "FAQ_Button":"css=a:contains('FAQ')", \
             "Search_Button":"css=a:contains('Search')", \
             "Video_Submit_Button":"//button[@value='Begin']", \
             
          }

WidgetUI = {"Video_playPause":"css=.mirosubs-playPause", \
            "Transcribe_current_sub":"css=.mirosubs-captionDiv", \
            "Next_step":"css=.mirosubs-done", \
            "Transcribe_play_pause":"css=.mirosubs-tab:contains('tab')",\
            "Sync_Review_play_pause":"css=.mirosubs-spacebar:contains('spacebar')", \
            "Sync_sub":"css=.mirosubs-down:contains('down')",\
            "Skip_back":"css=.mirosubs-control:contains('control')",\
            "Active_subtime":"css=li.active span.mirosubs-timestamp-time",\
            "Active_subtext":"css=li.active span.mirosubs-title",\
            "SubtitleMe_menu":"css=.mirosubs-tabText",\
            "AddSubtitles_menuitem":"css=.mirosubs-langmenuitem-content:contains(\"Add Subtitles\")",\
            "Login_menuitem":"css=.mirosubs-langmenuitem-content:contains(\"Login\")",\
            "Must_Login":"css=.mirosubs-needLogin", \
            "Must_Login_Message":"To save your subtitling work, you need to LOGIN", \
            


        }

# TestData

siteuser = "sub_writer"
twitteruser = "pcfsubwriter"
openiduser = "http://pcf-sub-writer.myopenid.com"
gmailuser = "pcf.subwriter"
passw = "sub.writer"
