#!/usr/bin/env python
from unisubs_page import UnisubsPage
from create_page import CreatePage
from search_results_page import SearchResultsPage
from video_page import VideoPage

class SharedActions(UnisubsPage):
    """Sequences the require objects from multiple pages.
    """

    _ADMIN_DELETE_VID_URL = "/videos/%s/staff/delete"
    

    def delete_video(self, video_id):
        unisubs_pg = UnisubsPage()
        unisubs_pg.open_page(self._ADMIN_DELETE_VID_URL % video_id)
        unisubs_pg.django_admin_login()
        unisubs_pg.django_admin_logout()
        del unisubs_pg

    def find_and_delete_existing_video(self, url):
        """Search for a video by url and delete via django admin ui.

        url - refers to the videos original url, not local site url.
        """
        result_pg = SearchResultsPage()
        result_pg.open_search_page()
        result_pg.basic_search(url)
        if result_pg.search_has_results():
            self.click_by_css(result_pg.FIRST_SEARCH_RESULT)
            del result_pg
            vid_pg = VideoPage()
            vid_id = vid_pg.video_id()
            del vid_pg
            self.delete_video(vid_id)
            
           
           
        


        
            
        
        
        
        
        
    

        
        
        

        
    

        
        



    
            
        
        
    
