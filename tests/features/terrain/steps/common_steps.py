#!/usr/bin/env python
import time
from lettuce import *


@step('I login')
def login(self):
    world.unisubs_pg.log_in('normal')
 
@step('(accept|reject) the confirmation alert')
def confirmation_alert(self, action):
    if action == "accept":
        world.html.handle_js_alert("accept")
    elif action == "reject":
        world.html.handle_js_alert("reject")

@step('I (see|do not see) the error message: "(.*?)"')
def error_message(self, action, message):
    if action == "see": assert world.unisubs_pg.error_message_present(message)
    if action == "do not see": assert not world.unisubs_pg.error_message_present(message)


