from selenium import selenium
import unittest
import time
import sys
import os
import mslib
import website
import widget
import offsite
import testvars
import selvars

class subgroup_78_playback(unittest.TestCase):
    """offsite widget on MC site.
    Litmus Subgroup 78 - offsite subwidget embedded in mc:
        Tests designed to exercise the subtitle widget embedded
        in sites external to universalsubtitles.org (live, dev or staging)  
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), selvars.set_site()))
        self.selenium.start()
        self.session = self.selenium.sessionId
        self.selenium.set_timeout(testvars.timeout)
        
   
# The test cases of the subgroup.

    def test_684(self):
        """Pagedemo New York Times video 1 - sub position on playback.
        Open the testpage
        Start Playback
        Verify subs are in the correct position on the video.
        
        http://litmus.pculture.org/show_test.cgi?id=684
        """
        sel = self.selenium

        #test 1st video on the page
        testpage = "/pagedemo/nytimes_youtube_embed"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        print "testing playback on 1st video on page"
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=span.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=span.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)
        
        

        #test 2nd video on the page
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        print "testing playback on second video on page"
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].play()')
        mslib.wait_for_element_present(self,sel,"css=span.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[1].pause()')
        caption_position =  sel.get_element_height("css=span.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)

    def test_688(self):
        """Pagedemo New York Times video 1 - translation playback
        
        http://litmus.pculture.org/show_test.cgi?id=688
        """
        test_id = 688
        sel = self.selenium
        testpage = "/pagedemo/nytimes_youtube_embed"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].openMenu()') 
        sel.click("css=div.mirosubs-dropdown div ul li:contains('100%')")
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(10)
        print "testing playback on translated lang"
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')       
        mslib.wait_for_element_present(self,sel,"css=span.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=span.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)
        
        

    def test_685(self):
        """Pagedemo Blog Youtube Embed - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=685
        """
        test_id = 685
        sel = self.selenium
        testpage = "/pagedemo/blog_youtube_embed"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)



    def test_686(self):
        """Pagedemo Gapminder - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=686
        """
        test_id = 686
        sel = self.selenium
        testpage = "/pagedemo/gapminder"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)

    def test_687(self):
        """Pagedemo Khan Widgetizer - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=687
        """
        test_id = 687
        sel = self.selenium
        testpage = "/pagedemo/khan_widgetizer"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)

    def test_701(self):
        """Pagedemo Khan Widgetizer async - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=687
        """
        test_id = 701
        sel = self.selenium
        testpage = "/pagedemo/async_widgetizer"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        sel.click("link=Widgetize it!")
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)

    
    def test_702(self):
        """Pagedemo JW Player - sub position on playback.
        
        http://litmus.pculture.org/show_test.cgi?id=687b
        """
        test_id = 702
        sel = self.selenium
        testpage = "/widget/widgetize_demo/jwplayer"
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(5)
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)

        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Check for an error page, then close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)







class subgroup_78_subtesting_playback(unittest.TestCase):
    """
    Litmus Subgroup 78 - offsite subwidget:
        Tests designed to exercise the subtitle widget embedded
        in sites external to universalsubtitles.org (live, dev or staging)  
    """


    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://subtesting.com/"))
        self.selenium.start()
        self.session = self.selenium.sessionId
        self.selenium.set_timeout(testvars.timeout)
        




    def test_696(self):
        """Subtesting widget - sub position on playback.
        Open the testpage
        Start Playback
        Verify subs are in the correct position on the video.
        
        http://litmus.pculture.org/show_test.cgi?id=696
        """
        sel = self.selenium

        #test 1st video on the page
        testpage = (selvars.set_subtesting_wordpress_page(self,601)) #same subtesting page as test test_601
        sel.open(testpage)
        sel.wait_for_page_to_load(testvars.timeout)
        sel.window_maximize()
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        time.sleep(3)
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].play()')
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionSpan")
        sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].pause()')
        caption_position =  sel.get_element_height("css=.mirosubs-captionSpan")
        verify_caption_position(self,sel,caption_position)
        verify_submenu_present(self,sel)


# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Check for an error page, then close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)



def verify_submenu_present(self,sel):
    sel.get_eval('this.browserbot.getUserWindow().mirosubs.widget.Widget.getAllWidgets()[0].openMenu()')
    time.sleep(2)
    self.failUnless(sel.is_element_present(testvars.WebsiteUI["Subhomepage_menuitem"]))


def verify_caption_position(self,sel,caption_position):
    if int(caption_position) > 80:
            self.fail("captions are too high on the video")
    if int(caption_position) < 10:
            self.fail("captions are too lown on the video")

      

if __name__ == "__main__":
    unittest.main()

 
