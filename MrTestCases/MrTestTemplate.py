# -*- coding: utf-8 -*-

'''
Created on 2016-7-28

@author: zhengjin

This is a template for monkey runner test cases.

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
g_hierarchy_viewer = None
g_snapshot_dir = ''

# ----------------------------------------------------------
# Helper functions
# ----------------------------------------------------------
def suite_set_up():
    MrBaseConstants.init_g_path_vars_for_win(MrTestRunner.g_user_run_num)

    global g_snapshot_dir
    g_snapshot_dir=MrBaseConstants.g_snapshot_dir_path_for_win
    global g_device
    g_device = MrBaseMrUtils.device_connect_and_return(MrTestRunner.g_user_device_no)

def test_set_up():
    global g_hierarchy_viewer
    g_hierarchy_viewer = MrBaseMrUtils.get_hierarchy_viewer(g_device)
    
    if not back_to_launcher(g_device):
        print 'Error back to the launcher home!'
        exit(1)

def back_to_launcher(device):
    MrBaseMrUtils.press_and_wait(device, MrBaseConstants.KEY_HOME, MrBaseConstants.g_wait_time)
    cur_activity = device.shell('dumpsys activity | grep mFocusedActivity')
    return cur_activity.find(MrBaseConstants.g_component_launcher_home)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def main(*arg):   # template
    suite_set_up()
    for fn in arg:
        test_set_up()
        fn(g_device, g_hierarchy_viewer, g_snapshot_dir)

