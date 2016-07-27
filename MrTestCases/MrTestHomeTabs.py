# -*- coding: utf-8 -*-
'''
Created on 2016-7-27

@author: zhengjin
'''

import sys
import os
from sys import argv

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
def suite_set_up():
    global g_device
    g_device = MrBaseMrUtils.device_connect_and_return(MrTestRunner.g_user_device_no)

def test_set_up():
    if not back_to_launcher(g_device):
        print 'Error back to the launcher home!'
        exit(1)

def back_to_launcher(device):
    MrBaseMrUtils.press_and_wait(device, MrBaseConstants.KEY_HOME)
    cur_activity = g_device.shell('dumpsys activity | grep mFocusedActivity')
    return cur_activity.find(MrBaseConstants.g_component_launcher_home)

def test_open_bottom_film_tab():
    g_device.touch(250, 750, MrBaseConstants.PRESS_TYPE_DU)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)
    
    main_title = MrBaseMrUtils.get_text_by_id(g_device, 'id/maintitle')
    if main_title == None or main_title == '':
        print 'FAILED, test_bottom_film_tab'
        # capture
    else:
        print 'Film tab main title: %s' %main_title
        print 'PASS, test_bottom_film_tab'

def test_open_bottom_tv_tab():
    g_device.touch(450, 800, MrBaseConstants.PRESS_TYPE_DU)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)
    
    main_title = MrBaseMrUtils.get_text_by_id(g_device, 'id/maintitle')
    if main_title == None or main_title == '':
        print 'FAILED, test_open_bottom_tv_tab'
    else:
        print 'TV tab main title: %s' %main_title
        print 'PASS, test_open_bottom_tv_tab'

def test_open_bottom_children_tab():
    g_device.touch(600, 750, MrBaseConstants.PRESS_TYPE_DU)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)

    main_title = MrBaseMrUtils.get_text_by_id(g_device, 'id/maintitle')
    if main_title == None or main_title == '':
        print 'FAILED, test_open_bottom_children_tab'
    else:
        print 'Children tab main title: %s' %main_title
        print 'PASS, test_open_bottom_children_tab'

def test_open_bottom_variety_tab():
    print 'TODO:'


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def main(*arg):
    suite_set_up()
    for fn in arg:
        test_set_up()
        fn()
    
main(test_open_bottom_film_tab,test_open_bottom_tv_tab,test_open_bottom_children_tab)

