Feature: Apply to team
	As a visitor
	I want to submit an application
	So that I can join the team

	Scenario: Unauthenticated user
		Given I am not logged into Universal Subtitles
		When I visit a team page
		Then I see a button that reads "Sign in to Join Team"

	## Not sure exactly how to break down more complex scenarios
	## like this, or if I'm getting too detailed or lumping too
	## many conditions together...
	Scenario: Authenticated user
		Given I am logged into Universal Subtitles
		And I visit a team page
		And the team's membership policy is "Application"
		Then I see a button that reads "Apply to Join"
		When I click the apply button
		And I enter "<message>" into the "About You" textarea
		And I click "Submit Application"
		Then I am added to the list of applicants