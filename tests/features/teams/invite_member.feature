Feature: Invite a member
	As a team member authorized to invite members
	I want to invite a user to the team
	So that the user can become a member

	# TODO: Should we specify the team as well? To test across multiple
	# teams?
	Scenario: Invite a single user
		Given I am on the team members page
		And I am an admin
		When I click the send invite button
		Then I go to the send invite page
		Given I enter a single valid "<username>"
		And the role selected is "<role>"
		When I click "Send Invites"
		Then the user "<username>" is invited
		When the user "<username>" accepts the invitation
		Then the user "<username>" joins the team with role "<role>"

	# TODO: Set up with real user data
	Examples:
		| username | role |
		| blah | admin |
		| blah | manager |
		| blah | contributor |

	
	Scenario: Invite multiple users
		Given I am on the team members page
		And I am an admin
		When I click the send invite button
		Then I go to the send invite page
		Given I enter a multiple valid "<usernames>"
		And the role selected is "<role>"
		When I click "Send Invites"
		Then the users "<usernames>" are invited
		When any of the users "<usernames>" accept the invitation
		Then the users "<usernames>" join the team with role "<role>"
	
	# TODO: Set up with real user data
	Examples:
		| usernames | role |
		| one, two | admin |
		| one, two, three | manager |
		| one, two, three, four | contributor |