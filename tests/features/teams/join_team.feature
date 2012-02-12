Feature: Join a team
    As a user 
    I want to join a team
    So that I can contribute subtitles

    @team
    Scenario: An anonymous user tries to join an open team, and must login first
        Given "normal" user is not a member of any teams
            And I am not logged in as a "normal" user
        When I visit an "open" team
            And I click the signin button
            And I log in as a "normal" user
            And I click the join button
            And accept the confirmation alert
        Then I am a member of the "open" team 

    Scenario: A logged in, 'normal' (non-admin) user joins an open team
        Given "normal" user is not a member of any teams
            And I am logged in as a "normal" user
            And I visit an "open" team
        When I click the join button
            And accept the confirmation alert
        Then I am a member of the "open" team

    Scenario: A logged in 'normal' user tries to join an application-only team
        Given "normal" user is not a member of any teams
            And I am logged in as a "normal" user
            And I visit an "application-only" team
        When I click the apply button
            Then the application form is displayed

