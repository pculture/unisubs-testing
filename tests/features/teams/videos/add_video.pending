Feature: Add a video
	As a user who has permission to manage team videos
	I want to add a video
	So that team contributors can add subtitles for it

	Scenario: Submit valid URLs
		Given I enter "<Video URL>" into the url field
		And I select "English" in the language field
		When I click the save button
		Then the video is saved and added to the team

	Examples:
		| Video URL |
		| 