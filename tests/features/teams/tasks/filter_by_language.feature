Feature: Filter tasks by language
	As a visitor or user
	I want to view tasks for a specific language
	So that I can find ways to contribute given my skills

	Scenario: 
		Given I am on the team tasks page
		And the language filter list contains all languages with active tasks
		When I select a language in the list
		Then I see only the tasks for that language