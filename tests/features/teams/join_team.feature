Feature: Join a team
	As a visitor
	I want to join a team
	So that I can contribute subtitles

	Scenario: Unauthenticated user
		Given I am not logged into Universal Subtitles
		When I visit a team page
		Then I see a button that reads "Sign in to Join Team"

	Scenario: Authenticated user
		Given I am logged into Universal Subtitles
		And I visit a team page
		And the team's membership policy is "Open"
		Then I see a button that reads "Join Team"
		When I click the join button
		Then I am a member of the team