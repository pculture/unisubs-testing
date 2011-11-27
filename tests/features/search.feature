Feature: Watch Page Search
    As a user
    I want to be able to find videos based on the title, subtitle text, url...
    So that I can view them on the site.


    Scenario: Perform a search that returns results
        Given I am on the watch page
        When I enter a search for "<search>"
        Then search results are displayed for "<search>"
        And the search term is displayed for the "<search>"

    Examples:
        | search |
        | monkey |
        | I'd like to be under the sea |
        | Selbst wenn du das letzte Herbstblatt bist, das vom Baum hängt |
        | 我们开始通用字幕，因为我们相信 |
 
    Scenario: Perform a search that returns no results
        Given I am on the watch page
        When I enter a search for "<search>"
        Then search results are not displayed for "<search>"
        And the search term is displayed for the "<search>"

    Examples:
        | search |
        | asd0asd9f as0d9f8asd asd0f98asd |




