Feature: Apply to team
	As a visitor
	I want to submit an application
	So that I can join the team

	Scenario: Unauthenticated user
		Given I am not logged into Universal Subtitles
		When I visit a team page
		Then I see a button that reads "Sign in to Join Team"

	Scenario: Authenticated user
		Given I am logged into Universal Subtitles
		And I visit a team page
		And the team's membership policy is "Application"
		Then I see a button that reads "Apply to Join"
		When I click the apply button
		Then I see the application modal
		When I click "Submit Application"
		Then I am added to the list of applicants