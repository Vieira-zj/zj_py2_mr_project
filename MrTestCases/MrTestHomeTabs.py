# -*- coding: utf-8 -*-
'''
Created on 2016-7-27

@author: zhengjin
'''

import sys
import os

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrUtils import MrBaseConstants
from MrUtils import MrBaseMrUtils
from MrTestCases import MrTestTemplate

# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_open_bottom_film_tab(device, hierarchy_viewer, snapshot_dir):
    MrBaseMrUtils.touch_and_wait(device, (250,750))
    MrBaseMrUtils.press_and_wait(device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)
    
    main_title = MrBaseMrUtils.get_text_by_id(device, hierarchy_viewer, 'id/maintitle')
    if main_title is None or main_title == '':
        print 'FAILED, test_bottom_film_tab'
        MrBaseMrUtils.take_snapshot(device, snapshot_dir)
    else:
        print 'Film tab main title: %s' %main_title
        print 'PASS, test_bottom_film_tab'

def test_open_bottom_tv_tab(device, hierarchy_viewer, snapshot_dir):
    MrBaseMrUtils.touch_and_wait(device, (450,800))
    MrBaseMrUtils.press_and_wait(device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)
    
    main_title = MrBaseMrUtils.get_text_by_id(device, hierarchy_viewer, 'id/maintitle')
    if main_title is None or main_title == '':
        print 'FAILED, test_open_bottom_tv_tab'
        MrBaseMrUtils.take_snapshot(device, snapshot_dir)
    else:
        print 'TV tab main title: %s' %main_title
        print 'PASS, test_open_bottom_tv_tab'

def test_open_bottom_children_tab(device, hierarchy_viewer, snapshot_dir):
    MrBaseMrUtils.touch_and_wait(device, (600,750))
    MrBaseMrUtils.press_and_wait(device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)

    main_title = MrBaseMrUtils.get_text_by_id(device, hierarchy_viewer, 'id/maintitle')
    if main_title is None or main_title == '':
        print 'FAILED, test_open_bottom_children_tab'
        MrBaseMrUtils.take_snapshot(device, snapshot_dir)
    else:
        print 'Children tab main title: %s' %main_title
        print 'PASS, test_open_bottom_children_tab'

def test_open_bottom_variety_tab():
    print 'TODO:'

def test_open_bottom_video_category_tab():
    print 'TODO:'

def test_open_left_member_tab():
    print 'TODO:'


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
MrTestTemplate.main(test_open_bottom_film_tab, test_open_bottom_tv_tab, test_open_bottom_children_tab)

