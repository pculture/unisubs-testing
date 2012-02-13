Feature: Leave team
	As a team member
	I want to leave the team
	So that I am no longer a member

##    Scenario: Team owner
##        Given I am logged in as the "team-owning" user
##            And I visit a team owned by "me"
##            When I click the leave button
##                And accept the confirmation alert
##            Then I see the error message: "You are the last member of this team." 

    Scenario: Non-owner
        Given I am logged in as the "normal" user
            And I have joined the team "<team>"
        When I click the leave button for the team "<team>"
            And accept the confirmation alert
        Then I am not a member of the "<team>" team
        Examples:
        | team |
        | open | 

