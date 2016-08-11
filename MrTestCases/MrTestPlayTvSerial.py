# -*- coding: utf-8 -*-
'''
Created on 2016-8-9

@author: zhengjin
'''
import sys
import os
import re

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

def test_select_tv_serial_from_list():
    MrTestTemplate.open_launcher_tab((450,750))
    
    MrBaseMrUtils.press_and_wait(g_device,MrBaseConstants.KEY_LEFT,MrBaseConstants.g_long_wait_time)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_DOWN)

    # select tv serial contains more than 20 tv shows
    move_times = 5
    min_tv_show_num = 20
    while True:
        MrBaseMrUtils.do_repeat_press_by_times(g_device, MrBaseConstants.KEY_RIGHT, move_times)
        container = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/info_container')
        node_title = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/title', container)
        tv_desc = MrBaseMrUtils.get_text_of_viewnode(g_hierarchy_viewer, node_title)

        if  get_number_from_tv_desc(tv_desc) > min_tv_show_num:
            print 'select tv serial: %s' %tv_desc
            return True
    
    return False

def test_open_tv_serial_details():    
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
    # play tv
    wait_time_for_open_player = 10.0
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER, wait_time_for_open_player)
    
    msg = 'test_open_tv_player, verify video player is on top\n'
    player = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/playerflipper')
    if player is not None:
        print 'Video player: %s' %type(player)
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg
        return False
    
    return True

def test_pause_tv_player():
    # pause player
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    
    msg = 'test_pause_tv_player, verify tv serial title when pause player'
    sub_tv_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/video_player_title')
    if g_tv_title.strip() == sub_tv_title.split(' ')[0].strip():
        print 'TV serial title: %s' %sub_tv_title
        print 'PASS, %s' %msg
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)
    
    msg = 'test_pause_tv_player, verify tv serial total time when pause player\n'
    tv_total_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_total')
    if MrTestTemplate.verify_null_or_empty(tv_total_time):
        print 'FAILED, %s' %msg
    else:
        print 'TV serial total time: %s' %tv_total_time
        print 'PASS, %s' %msg

    # replay tv
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)

def test_playing_tv_serial(play_time):
    # wait tv playing
    MrBaseMrUtils.mr_wait(play_time)

    msg = 'test_playing_tv_serial, verify video player is on top\n'
    player = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/playerflipper')
    if player is not None:
        print 'Video player: %s' %type(player)
        print 'PASS, %s' %msg
    else:
        print 'FAILED, %s' %msg

    # play next
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_DOWN)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_RIGHT)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)


# ----------------------------------------------------------
# Helper functions
# ----------------------------------------------------------
def get_number_from_tv_desc(fv_desc):
    if '全' in fv_desc:
        res = re.search('全(\d+)集', fv_desc)
        return int(res.group(1))
    return 0


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def test_main():
    if not test_select_tv_serial_from_list():
        return
    if not test_open_tv_serial_details():
        return
    if not test_open_tv_player():
        return

    test_pause_tv_player()
    
    play_time = 15 * 60
    test_times = 10
    for i in range(0,test_times):
        print 'play tv serial number: %d' %(i+1)
        test_playing_tv_serial(play_time)
    # when run 3 or 4 iterators, there are errors in adb or hierarchy viewer


MrTestTemplate.main(os.path.basename(__file__), test_init, test_main)
