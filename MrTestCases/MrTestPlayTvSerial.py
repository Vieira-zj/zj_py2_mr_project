# -*- coding: utf-8 -*-
'''
Created on 2016-8-9

@author: zhengjin
'''
import sys
import os

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrUtils import MrBaseConstants, MrBaseMrUtils
from MrTestCases import MrTestTemplate


# ----------------------------------------------------------
# Variables
# ----------------------------------------------------------
g_device = None
g_hierarchy_viewer = None

g_tv_title = ''


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_init():
    global g_device
    global g_hierarchy_viewer

    g_device = MrTestTemplate.g_device
    g_hierarchy_viewer = MrTestTemplate.g_hierarchy_viewer

def test_open_tv_serial_details():
    MrTestTemplate.open_launcher_tab((450,750))
    
    # select tv serial
    MrBaseMrUtils.press_and_wait(g_device,MrBaseConstants.KEY_LEFT,MrBaseConstants.g_long_wait_time)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_DOWN)
    
    # open tv details
    MrBaseMrUtils.press_and_wait(g_device,MrBaseConstants.KEY_ENTER,MrBaseConstants.g_time_out)
    
    msg = 'test_open_tv_serial_details, verify tv title of details page'
    tv_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/detail_title')
    if MrTestTemplate.verify_null_or_empty(tv_title):
        MrTestTemplate.failed_and_take_snapshot(msg)
        return False
    else:
        global g_tv_title
        g_tv_title = tv_title
        print 'TV serial title: %s' %tv_title
        print 'PASS, %s' %msg

    return True

def test_open_tv_player():
    print 'TODO:'
    

# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
MrTestTemplate.main(os.path.basename(__file__), test_init)
