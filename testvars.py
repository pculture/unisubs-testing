preE=" --- ERROR: "

MSTestVariables = {"Browser":"*chrome", \
                   "Site":"http://mirosubsdev.8planes.com/", \
                   "ResultOutputDirectory":r"Results/", \
                   "DataDirectory":r"TestInput/", \
                   "TimeOut":"60000", \
                  }

# Mapping to the MiroSubs website UI navigations buttons and links

WebsiteUI = {"Home":"css=a:contains('Miro Subs Alpha')", \
             "Subtitle_Button":"css=a:contains('Subtitle Video')", \
             "All_Videos_Button":"css=a:contains('All Videos')", \
             "About_Button":"css=a:contains('About')", \
             "FAQ_Button":"css=a:contains('FAQ')", \
             "Search_Button":"css=a:contains('Search')", \
             "Video_Submit_Button":"//button[@value='Begin']"
             
             
          }

WidgetUI = {"Transcribe_current_sub":"css=.mirosubs-captionDiv", \
            "Next_step":"css=.mirosubs-done", \
            "Transcribe_play_pause":"css=.mirosubs-tab",\
            "Sync_Review_play_pause":"css=.mirosubs-spacebar", \
            "Sync_sub":"css=.mirosubs-down",\
            "Skip_back":"css=.mirosubs-control",\
            "Active_subtime":"css=li.active span.mirosubs-timestamp-time",\
            "Active_subtext":"css=li.active span.mirosubs-title",\

        }

# TestData

testuser = "sub_writer"
testpass = "sub.writer"
