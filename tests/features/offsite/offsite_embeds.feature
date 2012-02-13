Feature: Playback of Videos with subtitles on pages with the univesal subtitles widget embedded.
    In order to share videos with subtitles around the world
    As a website owner
    I want display videos on my site and have my users be able to create, edit and playback subtitles
    There are a few sites that we want to check to make sure subs here are never broken and to accomplish this we have set up some demo pages on the unisubs site.  We want to be sure certain pages are never broken:
    1. New York Times http://dev.universalsubtitles.org/en/pagedemo/nytimes_youtube_embed
    2. Youtube embed on a wordpress blog, http://dev.universalsubtitles.org/en/pagedemo/blog_youtube_embed
    3. Gapminder http://dev.universalsubtitles.org/en/pagedemo/gapminder 

    Scenario Outline: Display subtitles on the embedded video
        Given I am on the site "<site>"
        When I start playback on the "<nth>" embedded video
        Then I see the subtitles for the "<nth>" embedded video
        And the subititles are correctly positioned on the video

    Examples:
        | site | nth |
        | pagedemo/nytimes_youtube_embed | 0 |
        | pagedemo/blog_youtube_embed | 0 |
        | pagedemo/gapminder | 0 |
