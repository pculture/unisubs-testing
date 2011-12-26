
from lettuce import *

@step('Subtitles are present for each language in the dir "(.*?)"')
def verify_team_video_subs(self, sub_dir):
    print 'checking the subs for this dir: % s' % sub_dir
    world.video_pg.open_original_lang()
    langs = world.data.list_of_translations(sub_dir)
    for sub_file, lang in langs:
        world.video_pg.open_translation(lang)
        print 'checking this lang %s' % lang
        subtitles = world.data.pull_sub_strings_from_data(sub_file)
        world.video_pg.verify_sub_content(subtitles)
        world.browser.back()
        world.video_pg.page_up_to_orig_lang()    

@step('I search a team for the "(.*?)"')
def team_search(self, search_term):
    search = search_term.split('_')[0]
    print 'search for the team video: %s' % search
    world.team_search_pg.team_search(search)

