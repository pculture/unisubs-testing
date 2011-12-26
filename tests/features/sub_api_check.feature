
Feature: Upload subs via the unisubs api
    In order to quickly upload videos and subtitles
    As a partner 
    I want to be sure that the videos and sub content is properly uploaded

    Scenario:  Subs are present for the given json files
        Given I am logged in as a "team" user
        When I search a team for the "<searchterm>"    
          And I open the first returned result
        Then Subtitles are present for each language in the dir "<directory>"

    Examples:
        | searchterm  | directory |
        | PeterGabriel | 23 |


