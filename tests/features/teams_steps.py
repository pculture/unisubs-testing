#!/usr/bin/env python
from lettuce import *


@step('"(.*?)" user is not a member of any teams')
def delete_user_from_team_all_teams(self, user):
    world.dj_admin.delete_user_from_all_teams(user)
    

@step('I visit (?:a|an|the) "(.*?)" team')
def open_a_teams_page(self, team_type):
    """Open a/an/the 'open', 'private', 'application-only' or named team page.

    If the string is one of the generic types, then the default team of that type is used.  Alternatively
    a specify team name can be specified by either the stup or full-name (provided no funny characters).
    To be more accurate: use the stub, like "unisubs-test-team" 
    """
    world.a_team_pg.open_a_team_page(team_type)

@step('I (see|click) the join button')
def join_button(self, action):
    """Verify the presence or click the "Join" button.  

    Both 'click_join()' and 'join_exists()' verify the Button display the correct text based on when the user is 
    logged in or out of the site
    """ 
    if action == "see":
        assert world.a_team_pg.join_exists()
    elif action == "click":
        world.a_team_pg.click_join()
    else:
        raise Exception("Undefined action: %s" % action)

@step('I (am|am not) a member of the "(.*?)" team')
def is_a_team_member(self, action, team):
    """Check if the currently logged in user is a member of the designated team.

    Valid strings are: a/an/the 'open', 'private', 'application-only' or "named" team page.

    If the string is one of the generic types, then the default team of that type is used.  Alternatively
    a specify team name can be specified by either the stup or full-name (provided no funny characters).
    To be more accurate: use the stub, like "unisubs-test-team"
    """
    if action == "am":
        assert world.a_team_pg.is_member(team)
    else:
        assert not world.a_team_pg.is_member(team)
 
