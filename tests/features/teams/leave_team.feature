Feature: Leave team
	As a member of a team 
	I want to leave the team

    Scenario: Team owner want to leave their team and is the sole admin
        Given I am logged in as the "team-owning" user
        When I leave the team "open" 
        Then I see the error message: "You are the last admin of this team." 

    Scenario: Normal volunteer leaves the team
        Given I am logged in as the "normal" user
            And I have joined the team "<team>"
        When I leave the team "<team>"
        Then I am not a member of the "<team>" team
        Examples:
        | team |
        | open | 

