# -*- coding: utf-8 -*-

'''
Created on 2016-7-27

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

g_film_title = ''
g_play_time = 20.0


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_init():
    global g_device
    global g_hierarchy_viewer

    g_device = MrTestTemplate.g_device
    g_hierarchy_viewer = MrTestTemplate.g_hierarchy_viewer

def test_open_a_film_in_player():
    # on launcher home, open film tab
    MrTestTemplate.open_tab((250,750))
    
    # on film recommend page, open film details
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_DOWN)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_long_wait_time)
    
    msg = 'test_open_a_film_in_player, verify title of film details page'
    film_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/detail_title')
    if MrTestTemplate.verify_null_or_empty(film_title):
        MrTestTemplate.failed_and_take_snapshot(msg)
        return
    else:
        print 'Film title: %s' %film_title
        print 'PASS, %s' %msg

        global g_film_title
        g_film_title = film_title

    # on film details page, click play to open player
    msg = 'test_open_a_film_in_player, verify video player is on top'
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, MrBaseConstants.g_time_out)
#     player = MrBaseMrUtils.find_view_by_id(device, hierarchy_viewer, 'id/playerflipper')
#     if player is not None:
#         print 'PASS, %s' %msg
#     else:
#         print 'FAILED, %s' %msg
#         return
    
    cur_activity = g_device.shell('dumpsys activity | grep mFocusedActivity')  # check video player is on top
    if cur_activity.find(MrBaseConstants.g_component_video_player):
        print 'Video player: %s' %cur_activity.strip('\n')
        print 'PASS, %s' %msg
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)
        return
    
def test_play_film_and_pause():
    # play film
    MrBaseMrUtils.mr_wait(g_play_time)
    # pause player
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    
    msg = 'play_film_and_pause, verify film title when pause player'
    sub_film_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/video_player_title')
    if g_film_title.strip() == sub_film_title.strip():
        print 'PASS, %s' %msg
        print 'Film title: %s' %sub_film_title
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)
    
    msg = 'play_film_and_pause, verify pause button when pause player'
    pause_button = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/control_panel_pause_layout_btn')
    if pause_button is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    msg = 'play_film_and_pause, verify seek bar when pause player'
    seek_bar = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/media_progress')
    if seek_bar is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    msg = 'play_film_and_pause, verify film time when pause player\n'
    film_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_total')
    if MrTestTemplate.verify_null_or_empty(film_time):
        print 'FAILED, %s' %msg
    else:
        print 'PASS, %s' %msg
        print 'Film time: %s' %film_time

def test_film_is_playing():
    cur_play_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_current')
    time_start = MrTestTemplate.format_play_time(cur_play_time)
    
    # replay film
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    MrBaseMrUtils.mr_wait(g_play_time)

    # pause
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    cur_play_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_current')
    time_end = MrTestTemplate.format_play_time(cur_play_time)
    
    msg = 'test_film_is_playing, verify playing film\n'
    during = time_end - time_start
    print 'Play film during time: %d' %during
    if during >= g_play_time:
        print 'PASS, %s' %msg
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)

    # reset film process bar
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    MrBaseMrUtils.do_repeat_press_during_time(g_device,MrBaseConstants.KEY_LEFT,MrBaseConstants.g_long_wait_time)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def test_main():
    test_open_a_film_in_player()
    test_play_film_and_pause()
    test_film_is_playing()

MrTestTemplate.main(os.path.basename(__file__), test_init, test_main)