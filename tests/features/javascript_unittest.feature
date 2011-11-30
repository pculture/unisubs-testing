Feature: Execute javascript unittests in the browser
    In order to verify javascript functions
    As a developer
    I want execute the javascript unittests 

    Scenario Outline: Display subtitles on the embedded video
        Given I am on the javascript test page
        When I start the tests
        Then they complete with no failures
        
