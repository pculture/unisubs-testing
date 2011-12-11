Feature: Edit a member's role and restrictions
	As a team admin
	I want to edit a member's role
	So that I can determine the privileges they have

	# TODO: Populate with real user data?
	Scenario: Assign another admin with no restrictions
		Given I am an admin and have no restrictions
		And I am on the members page
		Then I see an edit button for managers and contributors
		When I click the edit button for a manager or contributor
		Then I see the edit member modal
		When I select "admin" from the role dropdown
		And I click "save changes"
		Then the member is now an admin

	# TODO: Populate with real user and project data
	Scenario: Assign an admin with project restrictions
		Given I am an admin and have no restrictions
		And I am on the members page
		Then I see an edit button for managers and contributors
		When I click the edit button for a manager or contributor
		Then I see the edit member modal
		When I select "admin" from the role dropdown
		And I select "<project>" from the project restrictions dropdown
		And I click "save changes"
		Then the member is now an admin for the "<project>" project
	
	Examples:
		| project |
		| blah |

	Scenario: Asign a manager with no restrictions

	Scenario: Assign a manager with project restrictions

	Scenario: Assign a manager with language restrictions

	Scenario: Assign a manager with project and language restrictions