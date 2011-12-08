Feature: Filter videos by language
	As a visitor or user
	I want to view videos with subtitles in a specific language
	So that I can watch videos in my preferred language

	Scenario: 
		Given I am on the team videos page
		And the language filter list contains all languages for which there are completed subtitles
		When I select a language in the list
		Then I see only the videos with subtitles available in that language