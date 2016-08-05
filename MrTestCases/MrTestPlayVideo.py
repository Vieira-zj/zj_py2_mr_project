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
# Variables
# ----------------------------------------------------------
g_device = None
g_hierarchy_viewer = None
g_snapshot_dir = ''


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_setup():
    global g_device
    global g_hierarchy_viewer
    global g_snapshot_dir

    g_device = MrTestTemplate.g_device
    g_hierarchy_viewer = MrTestTemplate.g_hierarchy_viewer
    g_snapshot_dir = MrTestTemplate.g_snapshot_dir

def test_play_film():
    # on launcher home, open film tab
    MrTestTemplate.open_tab((250,750))
    
    # on film recommend page, open film details
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_DOWN)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)
    
    msg = 'test_play_film, verify title of film details page'
    film_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/detail_title')
    if film_title is None or film_title == '':
        MrTestTemplate.failed_and_take_snapshot(msg)
        return
    else:
        print 'Film title: %s' %film_title
        print 'PASS, %s' %msg

    # on film details page, click play to open player
    msg = 'test_bottom_film_tab, verify open video player'
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_time_out)
#     player = MrBaseMrUtils.find_view_by_id(device, hierarchy_viewer, 'id/playerflipper')
#     if player is not None:
#         print 'PASS, %s' %msg
#     else:
#         print 'FAILED, %s' %msg
#         return
    
    cur_activity = g_device.shell('dumpsys activity | grep mFocusedActivity')  # check video player is on top
    if cur_activity.find(MrBaseConstants.g_component_video_player):
        print 'Video player: %s' %cur_activity
        print 'PASS, %s' %msg
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)
        return
    
    # pause player
    MrBaseMrUtils.mr_wait(MrBaseConstants.g_time_out)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    
    msg = 'test_bottom_film_tab, verify film title when pause player'
    sub_film_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/video_player_title')
    if film_title.strip() == sub_film_title.strip():
        print 'PASS, %s' %msg
        print 'Film title: %s' %sub_film_title
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)
    
    msg = 'test_bottom_film_tab, verify pause button when pause player'
    pause_button = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/control_panel_pause_layout_btn')
    if pause_button is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    msg = 'test_bottom_film_tab, verify seek bar when pause player'
    seek_bar = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/media_progress')
    if seek_bar is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    msg = 'test_bottom_film_tab, verify film time when pause player'
    film_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_total')
    if film_time is None or film_time == '':
        print 'FAILED, %s' %msg
    else:
        print 'PASS, %s' %msg
        print 'Film time: %s' %film_time
    MrBaseMrUtils.take_snapshot(g_device, g_snapshot_dir)

    # clear up, reset the film process to start
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    MrBaseMrUtils.do_repeat_press_during_time(g_device,MrBaseConstants.KEY_LEFT,MrBaseConstants.g_time_out)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
MrTestTemplate.main(os.path.basename(__file__), 
                    test_setup, 
                    test_play_film)

