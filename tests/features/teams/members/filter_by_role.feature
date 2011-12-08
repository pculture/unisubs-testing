Feature: Filter members by role
	As a visitor or user
	I want to view members with a specific role
	So that I know who they are

	Scenario: Filter on a role that shows results
		Given I am on the team members page
		When I click the name of a role with a count greater than zero
		Then I see the list of members with that role

	Scenario: Filter on a role that shows no results
		Given I am on the team members page
		When I click the name of a role with a count equal to zero
		Then I see placeholder text in an element with class "empty"