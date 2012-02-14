#!/usr/bin/env python
import time
from lettuce import *
from nose.tools import assert_false
from nose.tools import assert_true


@step('I login')
def login(self):
    world.unisubs_pg.log_in('normal')
 
@step('(accept|reject) the confirmation alert')
def confirmation_alert(self, action):
    if action == "accept":
        world.html.handle_js_alert("accept")
    elif action == "reject":
        world.html.handle_js_alert("reject")

@step('I (see|do not see) the (error|success) message: "(.*?)"')
def message_display(self, action, message_type, message):
    message_check = message_type+"_message_present"
    if action == "see": assert_true(getattr(world.unisubs_pg, message_check)(message))
    if action == "do not see": assert_false(getattr(world.unisubs_pg, message_check)(message))


