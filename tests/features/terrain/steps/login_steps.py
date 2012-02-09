#!/usr/bin/env python
from lettuce import *

@step('I (am logged|am not logged|log) in as (?:a|the) "([^"]*)" user')
def log_in_or_out(self, login, user):
    _VALID_USERS = world.unisubs_pg.USER_NAMES.iterkeys()
    if user not in _VALID_USERS:
        raise Exception("user value must be one of %s" % _VALID_USERS)
    if login == "am not logged":
        world.unisubs_pg.log_out()
    elif login == "am logged" or login == "log":
        world.unisubs_pg.log_in(user)
    else:
        raise Exception("I am not sure what to do here")


    
