Feature: Remove a video from a team
	As a team member with permission to manage videos
	I want to remove a video from the team
	So that it is no longer shown as part of the team

	Scenario: Remove a video
		Given i am on the team videos page
		When I click the remove button on a video
		Then that video is removed from the team and I don't see it listed