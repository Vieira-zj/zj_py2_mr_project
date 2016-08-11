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


# ----------------------------------------------------------
# Helper methods
# ----------------------------------------------------------
def back_to_launcher():
    MrBaseMrUtils.press_and_wait(g_device,MrBaseConstants.KEY_HOME,MrBaseConstants.g_wait_time)
    cur_activity = g_device.shell('dumpsys activity | grep mFocusedActivity')
    return cur_activity.find(MrBaseConstants.g_component_launcher_home)

def open_launcher_tab(point, wait_time=MrBaseConstants.g_long_wait_time):
    MrBaseMrUtils.touch_and_wait(g_device, point)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, wait_time)

def verify_null_or_empty(obj):
    if obj is None or obj == '':
        return True
    else:
        return False

def failed_and_take_snapshot(msg):
    print 'FAILED, %s' %msg
    MrBaseMrUtils.take_snapshot(g_device, MrBaseConstants.g_snapshot_dir_path_for_win)

def format_play_time(play_time):
    hours = ''
    mins = ''
    secs = ''
    
    items = play_time.split(':')
    if len(items) == 2:
        mins = items[0]
        secs = items[1]
        return (convert_str_to_time(mins) * 60 + convert_str_to_time(secs))
    elif len(items) == 3:
        hours = items[0]
        mins = items[1]
        secs = items[2]
        return (convert_str_to_time(hours) * 60 * 60 + convert_str_to_time(mins) * 60 + 
                convert_str_to_time(secs))
    else:
        print 'The play time(%s) is invalid.' %play_time
        return 0
    
def convert_str_to_time(cur_time):
    if cur_time == '00':
        return 0
    if cur_time[0] == '0':
        return int(cur_time[1])    
    return int(cur_time)


# ----------------------------------------------------------
# Setup and clearup
# ----------------------------------------------------------
def test_suite_setup():
    MrBaseConstants.init_g_path_vars_for_win(MrTestRunner.g_user_run_num)

    global g_device
    g_device = MrBaseMrUtils.get_monkey_device(MrTestRunner.g_user_device_no)
    global g_hierarchy_viewer
    g_hierarchy_viewer = MrBaseMrUtils.get_hierarchy_viewer(g_device)

def test_suite_clearup():
    print 'TODO: logs'

def test_case_setup():
    if not back_to_launcher():
        print 'Error back to the launcher home!'
        exit(1)

def test_case_clearup():
    back_to_launcher()


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def main(script_name, *arg):   # test case template
    print '%s: START ---> run TEST SCRIPT: %s' %(MrBaseConstants.g_cur_time,script_name)
    
    test_suite_setup()
    for fn in arg:
        if fn.__name__ == 'test_init':
            fn()
            continue
        
        print '%s: START: run TEST CASE: %s' %(MrBaseConstants.g_cur_time,fn.__name__)
        test_case_setup()
        fn()
        test_case_clearup()
        print '%s: END: run TEST CASE: %s\n' %(MrBaseConstants.g_cur_time,fn.__name__)
    
    print '%s: END ---> run TEST SCRIPT: %s\n\n' %(MrBaseConstants.g_cur_time,script_name)
    