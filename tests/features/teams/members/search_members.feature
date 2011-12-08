Feature: Search members
	As a visitor or user
	I want to search through team members
	So that I can find the person I'm looking for

	Scenario: Perform search that returns results
		Given I am on the team members page
		When I enter search term "<username>"
		Then I see results for "<username>"

	# TODO: Populate with real user data
	Examples:
		| username |
		| admin |

	Scenario: Perform a search that returns no results
		Given I am on the team members page
		When I enter search term "<username>"
		Then I see a placeholder message in an element with class "empty"
	
	Examples:
		| username |
		| usernameisnotausername |
		| youcantbeseriousaboutthis |
		| nousershouldhavethisname |