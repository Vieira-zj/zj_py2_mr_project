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


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_init():
    global g_device
    global g_hierarchy_viewer
 
    g_device = MrTestTemplate.g_device
    g_hierarchy_viewer = MrTestTemplate.g_hierarchy_viewer

def test_move_to_right_area_and_open_p11_tab():
    MrBaseMrUtils.touch_and_wait(g_device, (1700,350),MrBaseConstants.g_wait_time)
    MrBaseMrUtils.press_and_wait(g_device,MrBaseConstants.KEY_ENTER,MrBaseConstants.g_long_wait_time)
    
    msg = 'test_move_to_right_area_and_open_first_tab, verify film title'
    film_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/detail_title')
    if MrTestTemplate.verify_null_or_empty(film_title):
        MrTestTemplate.failed_and_take_snapshot(msg)
    else:
        print 'Film title: %s' %film_title
        print 'PASS, %s' %msg
    
def open_p21_tab():
    print 'TODO:'

def open_p31_tab():
    print 'TODO:'



# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
MrTestTemplate.main(os.path.basename(__file__), 
                    test_init, 
                    test_move_to_right_area_and_open_p11_tab)
