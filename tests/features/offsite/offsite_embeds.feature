Feature: Playback of Videos with subtitles on pages with the univesal subtitles widget embedded.
    In order to share videos with subtitles around the world
    As a website owner
    I want display videos on my site and have my users be able to create, edit and playback subtitles 

    Scenario: Display subtitles on the embedded video
        Given I am on the site "<site>"
        When I start playback on the "<nth>" embedded video
        Then I see the subtitles for the "<nth>" embedded video
        And the subititles are correctly positioned on the video

    Examples:
        | site | nth |
        | pagedemo/nytimes_youtube_embed | 0 |
        | pagedemo/blog_youtube_embed | 0 |
        | pagedemo/gapminder | 0 |
