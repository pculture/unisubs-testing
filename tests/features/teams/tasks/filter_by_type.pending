Feature: Filter tasks by type
	As a visitor or user
	I want to view tasks of a specific type
	So that I can find a way to contribute

	Scenario: Filter on a type that shows results
		Given I am on the team tasks page
		When I click the name of a type with a count greater than zero
		Then I see the list of tasks of that type

	Scenario: Filter on a type that shows no results
		Given I am on the team tasks page
		When I click the name of a type with a count equal to zero
		Then I see placeholder text in an element with class "empty"