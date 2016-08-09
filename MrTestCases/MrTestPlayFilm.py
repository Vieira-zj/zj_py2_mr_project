# -*- coding: utf-8 -*-

'''
Created on 2016-7-27

@author: zhengjin
'''

import sys
import os
import random

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrUtils import MrBaseConstants, MrBaseMrUtils
from MrTestCases import MrTestTemplate


# ----------------------------------------------------------
# Variables
# ----------------------------------------------------------
g_device = None
g_hierarchy_viewer = None

g_film_title = ''


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_init():
    global g_device
    global g_hierarchy_viewer

    g_device = MrTestTemplate.g_device
    g_hierarchy_viewer = MrTestTemplate.g_hierarchy_viewer

def test_open_film_in_player():
    # on launcher home, open film tab
    MrTestTemplate.open_tab((250,750))
    
    # open film list page
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_LEFT, MrBaseConstants.g_long_wait_time)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_DOWN)

    # select film and open
    msg = 'test_setup_open_film_in_player, verify title of film details page'
    move_times = random.randint(2,11)
    for i in range(1,move_times):
        MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_RIGHT)
    MrBaseMrUtils.press_and_wait(g_device,MrBaseConstants.KEY_ENTER,MrBaseConstants.g_long_wait_time)
    
    film_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/detail_title')
    if MrTestTemplate.verify_null_or_empty(film_title):
        MrTestTemplate.failed_and_take_snapshot(msg)
        return False
    else:
        global g_film_title
        g_film_title = film_title
        print 'Film title: %s' %film_title
        print 'PASS, %s' %msg
    
    # play film
    msg = 'test_setup_open_film_in_player, verify video player is on top\n'
    wait_time_for_open_player = 10.0
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, wait_time_for_open_player)
    player = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/playerflipper')
    if player is not None:
        print 'Video player: %s' %type(player)
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
        return False
    
#     cur_activity = g_device.shell('dumpsys activity | grep mFocusedActivity')  # check video player is on top
#     if cur_activity.find(MrBaseConstants.g_component_video_player):
#         print 'Video player: %s' %cur_activity
#         print 'PASS, %s' %msg
#     else:
#         MrTestTemplate.failed_and_take_snapshot(msg)
#         return False

    return True
    
def test_pause_film_play():
    # pause player
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    
    msg = 'test_pause_film_play, verify film title when pause player'
    sub_film_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/video_player_title')
    if g_film_title.strip() == sub_film_title.strip():
        print 'Film title: %s' %sub_film_title
        print 'PASS, %s' %msg
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)
    
    msg = 'test_pause_film_play, verify pause button when pause player'
    pause_button = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/control_panel_pause_layout_btn')
    if pause_button is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    msg = 'test_pause_film_play, verify seek bar when pause player'
    seek_bar = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/media_progress')
    if seek_bar is not None:
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
    
    msg = 'test_pause_film_play, verify film time when pause player\n'
    film_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_total')
    if MrTestTemplate.verify_null_or_empty(film_time):
        print 'FAILED, %s' %msg
    else:
        print 'Film time: %s' %film_time
        print 'PASS, %s' %msg

def test_film_is_playing(play_time):
    cur_play_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_current')
    print 'Current play time %s' %cur_play_time
    time_start = MrTestTemplate.format_play_time(cur_play_time)
    
    # replay film
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    MrBaseMrUtils.mr_wait(play_time)

    # pause
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    cur_play_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_current')
    print 'Current play time %s' %cur_play_time
    time_end = MrTestTemplate.format_play_time(cur_play_time)
    
    msg = 'test_film_is_playing, verify playing film\n'
    during = time_end - time_start
    print 'Play film during time: %d' %during
    if during >= play_time:
        print 'PASS, %s' %msg
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)

def test_after_reset_film_process(reset_time):
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    MrBaseMrUtils.do_repeat_press_during_time(g_device, MrBaseConstants.KEY_LEFT, reset_time)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def test_main():
    # run as one test case 
    if not test_open_film_in_player():
        return
    
    test_pause_film_play()

    replay_times = 3  # default replay 3 times
    play_time = 3 * 60  # default is 3 minutes
    for i in range(1,(replay_times+1)):
        print 'Run test test_film_is_playing %d time' %i
        test_film_is_playing(play_time)

    reset_time = 60
    test_after_reset_film_process(reset_time)


MrTestTemplate.main(os.path.basename(__file__), test_init, test_main)
