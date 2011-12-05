Feature: Leave team
	As a team member
	I want to leave the team
	So that I am no longer a member

	Scenario: Team owner
		Given I am the owner of the team
		When I click the leave button
		Then I see an error message informing me that I cannot leave the team

	Scenario: Non-owner
		Given I am not the owner of the team
		When I click the leave button
		Then I see a message informing me that I have left the team