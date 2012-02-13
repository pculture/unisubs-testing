Feature: Submit videos via the create page
    In order to get a video subtitles
    As a user
    I want to add it to the site
    
    Scenario: Submit an individual video from the create page
        Given the video is not in the unisubs db "<url>"
        When I submit a video "<url>"
        Then I see the embedded video

    Examples:
        | url |
	    | http://www.youtube.com/watch?v=WqJineyEszo |
	    | http://blip.tv/file/get/Pycon-PyCon2011PythonTheSecretSauceInTheOpenCloud878.ogv |
	    | http://blip.tv/file/get/Linuxconfau-LightningTalks606.flv |
	    | http://www.dailymotion.com/video/xlh9h1_fim-syndicat-des-apiculteurs-de-metz-environs_news |
	    | http://vimeo.com/26487510 |


    Scenario: Bulk Submit a video feed
        Given the feed is not in the unisubs db "<url>"
        When I submit a feed "<url>"
        Then I see the submit successful message

    Examples:
        | url |
	    | http://vimeo.com/jeroenhouben/videos/rss |
	    | http://www.dailymotion.com/rss/user/WildFilmsIndia/1 |
	    | http://blip.tv/weird-america/rss/flash |
            | http://blip.tv/cord-cutters/cord-cutters-sync-mobile-media-with-miro-4-5280931?skin=rss |
            | http://gdata.youtube.com/feeds/api/users/katyperrymusic/uploads |
            | http://www.dailymotion.com/rss/user/LocalNews-GrabNetworks/1 |

    Scenario: Submit youtube user page videos
        Given the feed is not in the unisubs db "<db_url>"
        When I submit a youtube user page "<url>"
        Then I see the submit successful message

    Examples:
        | db_url | url |
        | https://gdata.youtube.com/feeds/api/users/SeveFanClub/uploads | http://www.youtube.com/user/SeveFanClub |

    Scenario: Submit youtube user feed videos
        Given the feed is not in the unisubs db "<db_url>"
        When I submit a youtube user feed "<username>"
        Then I see the submit successful message

    Examples:
        | db_url | username |
	| https://gdata.youtube.com/feeds/api/users/croatiadivers/uploads | croatiadivers |



