Feature: Remove a task from a team
	As a team member with permission to assign tasks
	I want to remove a task from the team
	So that it is no longer shown for the team

	Scenario: Remove a task
		Given I am on the team tasks page
		When I click the remove button on a task
		Then that task is removed from the team and I don't see it listed