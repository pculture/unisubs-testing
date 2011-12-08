Feature: Filter members by language
	As a visitor or user
	I want to view members that know a specific language
	So that I know who they are ;)

	Scenario: 
		Given I am on the team members page
		And the language filter list contains all languages known by members
		When I select a language in the list
		Then I see only the members who know that language