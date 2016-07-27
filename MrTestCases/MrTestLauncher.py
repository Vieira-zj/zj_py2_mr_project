# -*- coding: utf-8 -*-
'''
Created on 2016-7-27

@author: zhengjin
'''

import sys
import os

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrRunner import MrTestRunner
from MrUtils import MrBaseConstants
from MrUtils import MrBaseMrUtils

# ----------------------------------------------------------
# Variables
# ----------------------------------------------------------
g_device = None


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_set_up():
    global g_device
    g_device = MrBaseMrUtils.get_easy_device(MrTestRunner.g_user_device_no)

    if not back_to_launcher(g_device):
        print 'Error back to the launcher home!'
        exit(1)

def back_to_launcher(device):
    MrBaseMrUtils.press_and_wait(device, MrBaseConstants.KEY_HOME)
    cur_activity = g_device.shell('dumpsys activity | grep mFocusedActivity')
    return cur_activity.find(MrBaseConstants.g_component_launcher_home)
    

def test_bottom_film_tab():
    print ''
    

# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
test_set_up()
