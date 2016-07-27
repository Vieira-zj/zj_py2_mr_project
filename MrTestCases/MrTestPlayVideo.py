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
g_hierarchy_viewer = None


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def suite_set_up():
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
    cur_activity = g_device.shell('dumpsys activity | grep mFocusedActivity')
    return cur_activity.find(MrBaseConstants.g_component_launcher_home)

def test_play_film():
    # on launcher home, open film tab
    g_device.touch(250, 750, MrBaseConstants.PRESS_TYPE_DU)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_time_out)
    
    # on film recommend page, open film details
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_DOWN)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)
    
    film_title = MrBaseMrUtils.get_text_by_id(g_device, g_hierarchy_viewer, 'id/detail_title')
    msg = 'test_play_film, verify open film details page'
    if film_title is None or film_title == '':
        print 'FAILED, %s' %msg
        # capture
        return
    else:
        print 'Film title: %s' %film_title
        print 'PASS, %s' %msg

    # on film details page, click play to open player
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_time_out)
    player = MrBaseMrUtils.find_view_by_id(g_device, g_hierarchy_viewer, 'id/playerflipper')
    msg = 'test_bottom_film_tab, verify open player'
    if player is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    # pause player
    MrBaseMrUtils.mr_wait(MrBaseConstants.g_time_out)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    
    sub_film_title = MrBaseMrUtils.get_text_by_id(g_device, g_hierarchy_viewer, 'id/video_player_title')
    msg = 'test_bottom_film_tab, verify film title when pause player'
    if film_title.strip() == sub_film_title.strip():
        print 'PASS, %s' %msg
        print 'Film title: %s' %sub_film_title
    else:
        print 'FAILED, %s' %msg
    
    pause_button = MrBaseMrUtils.find_view_by_id(g_device, g_hierarchy_viewer, 'id/control_panel_pause_layout_btn')
    msg = 'test_bottom_film_tab, verify pause button when pause player'
    if pause_button is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    seek_bar = MrBaseMrUtils.find_view_by_id(g_device, g_hierarchy_viewer, 'id/media_progress')
    msg = 'test_bottom_film_tab, verify seek bar when pause player'
    if seek_bar is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    film_time = MrBaseMrUtils.get_text_by_id(g_device, g_hierarchy_viewer, 'id/time_total')
    msg = 'test_bottom_film_tab, verify film time when pause player'
    if film_time is None or film_time == '':
        print 'FAILED, %s' %msg
    else:
        print 'PASS, %s' %msg
        print 'Film time: %s' %film_time


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def main(*arg):
    suite_set_up()
    for fn in arg:
        test_set_up()
        fn()
    
main(test_play_film)
