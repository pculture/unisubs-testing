@submit
Feature:  Add videos for subtitling.
 - A single url may be submitted from one of the supported sites:
   - Youtube
   - Blip 
   - Vimeo
   - Daily Motion
 - A single url can be submitted of one of the supported formats:
  - ogg, ogv
  - flv
  - webm
  - mp4
 - Multiple videos in the form of an rss feed can also be submitted from the supported sites:
   - Vimeo
   - Blip 
   - Daily Motion
   - Youtube User feed
   - Youtube User page 

Scenario Outline: Submit an individual video from one of the supported sites:
 - youtube
 - blip
 - dailymotion, vimeo.
 When I submit a unique video "<url>"
 Then I see the embedded video
Examples:
    | url |
    | http://www.youtube.com/watch?v=WqJineyEszo |
    | http://www.dailymotion.com/video/xlh9h1_fim-syndicat-des-apiculteurs-de-metz-environs_news |
    | http://vimeo.com/26487510 |


Scenario Outline: Submit an individual video of one of the supported formats
        When I submit a unique video "<url>"
        Then I see the embedded video
Examples:
    | url |
    | http://blip.tv/file/get/Pycon-PyCon2011PythonTheSecretSauceInTheOpenCloud878.ogv |
    | http://blip.tv/file/get/Linuxconfau-LightningTalks606.flv |
    | http://pculture.org/feeds_test/conversions/webm/waiting_for_the_sun.webmvp8.webm |

Scenario Outline: Bulk Submit a video feed from a supported source.

 When I submit a unique feed "<url>"
 Then I see the submit successful message

Examples:
    | url |
    | http://vimeo.com/jeroenhouben/videos/rss |
    | http://www.dailymotion.com/rss/user/WildFilmsIndia/1 |
    | http://blip.tv/weird-america/rss/flash |
    | http://blip.tv/cord-cutters/cord-cutters-sync-mobile-media-with-miro-4-5280931?skin=rss |
    | http://gdata.youtube.com/feeds/api/users/katyperrymusic/uploads |
    | http://www.dailymotion.com/rss/user/LocalNews-GrabNetworks/1 |

Scenario Outline: Submit youtube user page videos
   When I submit a youtube user page "<url>"
   Then I see the submit successful message

Examples:
    | db_url | url |
    | https://gdata.youtube.com/feeds/api/users/SeveFanClub/uploads | http://www.youtube.com/user/SeveFanClub |

Scenario Outline: Submit youtube user feed videos
    When I submit a unique youtube user feed "<username>"
    Then I see the submit successful message

Examples:
    | db_url | username |
    | https://gdata.youtube.com/feeds/api/users/croatiadivers/uploads | croatiadivers |



