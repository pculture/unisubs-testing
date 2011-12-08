Feature: Search videos
	As a visitor or user
	I want to search through team videos
	So that I can find the video I'm looking for

	Scenario: Perform search that returns results
		Given I am on the team videos page
		When I enter the search term "<term>"
		Then I see results for "<term>"

	## TODO: To what extent whould I be targeting real data, and if so,
	## on dev or on staging?
	Examples:
		| term |
		| blah |

	Scenario: Perform a search that returns no results
		Given I am on the team videos page
		When I enter the search term "<term>"
		Then I see a no results message in an element with class "empty" 

	## TODO: To what extent whould I be targeting real data, and if so,
	## on dev or on staging?
	Examples:
		| term |
		| blah |