# -*- coding: utf-8 -*-
'''
Created on 2016-8-8

@author: zhengjin
'''
import sys
import os

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrUtils import MrBaseMrUtils, MrBaseConstants
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

def test_open_news_tab_of_right_area():
    MrTestTemplate.open_launcher_tab((1350,300))
    
    msg = 'test_open_news_tab_of_right_area, verify main title of NEWS tab'
    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/news_special_list_item_title')
    if MrTestTemplate.verify_null_or_empty(main_title):
        MrTestTemplate.failed_and_take_snapshot(msg)
        return False
    else:
        print 'News tab main title: %s' %main_title
        print 'PASS, %s' %msg

    msg = 'test_open_news_tab_of_right_area, verify sub title of NEWS tab'    
    sub_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/news_play_title')
    if MrTestTemplate.verify_null_or_empty(main_title):
        MrTestTemplate.failed_and_take_snapshot(msg)
        return False
    else:
        print 'News tab sub title: %s' %sub_title.split(' ')[0]
        print 'PASS, %s' %msg

    msg = 'test_open_news_tab_of_right_area, verify NEWS player\n'
    player_view = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/news_player_view')
    if player_view is None:
        MrTestTemplate.failed_and_take_snapshot(msg)
        return False
    else:
        print 'Player view: %s' %type(player_view)
        print 'PASS, %s' %msg
    
    return True

def test_playing_news():
    # max new player windows
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_RIGHT)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_RIGHT)
    MrBaseMrUtils.press_and_wait(g_device,MrBaseConstants.KEY_ENTER,MrBaseConstants.g_short_wait_time)

    # pause player
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    cur_play_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_current')
    time_start = MrTestTemplate.format_play_time(cur_play_time)
    
    # replay news
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    play_time = 15.0
    MrBaseMrUtils.mr_wait(play_time)
    
    # pause player
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    cur_play_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_current')
    time_end = MrTestTemplate.format_play_time(cur_play_time)
    
    during = time_end - time_start
    print 'Play news during time: %d' %during

    msg = 'test_playing_news, verify news is playing\n'
    if during >= play_time:
        print 'PASS, %s' %msg
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def test_main():
    if not test_open_news_tab_of_right_area():
        return
    test_playing_news()

MrTestTemplate.main(os.path.basename(__file__), 
                    test_init,
                    test_main)
