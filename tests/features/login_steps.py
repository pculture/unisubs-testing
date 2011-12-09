#!/usr/bin/env python
from lettuce import *



@step('I (am logged|am not logged|log) in as a "([^"]*)" user')
def log_in_or_out(self, login, user):
    user_types = ['normal', 'admin']
    
    if user not in user_types:
        raise Exception("user value must be one of %s" % user_types)
    if login == "am not logged":
        world.unisubs_pg.log_out()
    elif login == "am logged" or login == "log":
        world.unisubs_pg.log_in(user)
    else:
        raise Exception("I am not sure what to do here")


    
