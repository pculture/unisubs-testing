#!/usr/bin/env python
import time
from lettuce import *


@step('I login')
def login(self):
    world.unisubs_pg.log_in('normal')
 
@step('(accept|reject) the confirmation alert')
def confirmation_alert(self, action):
    time.sleep(2)
    a = world.browser.switch_to_alert()
    if action == "accept":
        a.accept()
    elif action == "reject":
        a.dismiss()

    
