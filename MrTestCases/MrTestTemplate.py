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
# Helper methods
# ----------------------------------------------------------
def open_tab(point):
    MrBaseMrUtils.touch_and_wait(g_device, point)
    MrBaseMrUtils.press_and_wait(g_device,MrBaseConstants.KEY_ENTER,MrBaseConstants.g_long_wait_time)

def failed_and_take_snapshot(msg):
    print 'FAILED, %s' %msg
    MrBaseMrUtils.take_snapshot(g_device, g_snapshot_dir)


# ----------------------------------------------------------
# Setup and clearup
# ----------------------------------------------------------
def test_suite_setup():
    MrBaseConstants.init_g_path_vars_for_win(MrTestRunner.g_user_run_num)

    global g_device
    g_device = MrBaseMrUtils.get_monkey_device(MrTestRunner.g_user_device_no)
    global g_hierarchy_viewer
    g_hierarchy_viewer = MrBaseMrUtils.get_hierarchy_viewer(g_device)
    global g_snapshot_dir
    g_snapshot_dir = MrBaseConstants.g_snapshot_dir_path_for_win

def test_case_setup():
    if not back_to_launcher(g_device):
        print 'Error back to the launcher home!'
        exit(1)

def test_case_clearup():
    print 'TODO:'

def back_to_launcher(device):
    MrBaseMrUtils.press_and_wait(device, MrBaseConstants.KEY_HOME, MrBaseConstants.g_wait_time)
    cur_activity = device.shell('dumpsys activity | grep mFocusedActivity')
    return cur_activity.find(MrBaseConstants.g_component_launcher_home)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def main(script_name, *arg):   # template
    print '%s: START ---> run test script: %s' %(MrBaseConstants.g_cur_time,script_name)
    
    test_suite_setup()
    for fn in arg:
        print '%s: start: run test case: %s' %(MrBaseConstants.g_cur_time,fn.__name__)
        test_case_setup()
        fn()
        print '%s: end: run test case: %s\n' %(MrBaseConstants.g_cur_time,fn.__name__)
    
    print '%s: END ---> run test script: %s\n\n' %(MrBaseConstants.g_cur_time,script_name)