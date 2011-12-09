Feature: Join a team
    As a visitor
    I want to join a team
    So that I can contribute subtitles

    Scenario: Unauthenticated user
        Given "normal" user is not a member of any teams
            And I am not logged in as a "normal" user
        When I visit an "open" team
            And I click the join button
            And I log in as a "normal" user
            And I click the join button
            And accept the confirmation alert
        Then I am a member of the "open" team 

    Scenario: Authenticated user
        Given "normal" user is not a member of any teams
            And I am logged in as a "normal" user
            And I visit an "open" team
        When I click the join button
            And accept the confirmation alert
        Then I am a member of the "open" team
