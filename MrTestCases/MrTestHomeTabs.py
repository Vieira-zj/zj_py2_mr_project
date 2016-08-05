# -*- coding: utf-8 -*-
'''
Created on 2016-7-27

@author: zhengjin
'''

import sys
import os

sys.path.append(os.environ['MR_PROJECT_PATH'])
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

def test_open_bottom_film_tab():
    MrTestTemplate.open_tab((250,750))

    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/maintitle')
    if main_title is None or main_title == '':
        MrTestTemplate.failed_and_take_snapshot('test_open_bottom_film_tab')
    else:
        print 'Film tab main title: %s' %main_title
        print 'PASS, test_open_bottom_film_tab'
    
def test_open_bottom_tv_tab():
    MrTestTemplate.open_tab((450,750))
    
    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/maintitle')
    if main_title is None or main_title == '':
        MrTestTemplate.failed_and_take_snapshot('test_open_bottom_tv_tab')
    else:
        print 'TV tab main title: %s' %main_title
        print 'PASS, test_open_bottom_tv_tab'
        
def test_open_bottom_children_tab():
    MrTestTemplate.open_tab((600,750))

    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/maintitle')
    if main_title is None or main_title == '':
        MrTestTemplate.failed_and_take_snapshot('test_open_bottom_children_tab')
    else:
        print 'Children tab main title: %s' %main_title
        print 'PASS, test_open_bottom_children_tab'
    
def test_open_bottom_variety_tab():
    MrTestTemplate.open_tab((850,750))
    
    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/maintitle')
    if main_title is None or main_title == '':
        MrTestTemplate.failed_and_take_snapshot('test_open_bottom_variety_tab')
    else:
        print 'Variety tab main title: %s' %main_title
        print 'PASS, test_open_bottom_variety_tab'

def test_open_news_tab_of_right_area():
    MrTestTemplate.open_tab((1350,300))
    
    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/news_special_list_item_title')
    if main_title is None or main_title == '':
        MrTestTemplate.failed_and_take_snapshot('verify main title text of news tab')
        return
    else:
        print 'News tab main title: %s' %main_title
        print 'PASS, verify main title text of news tab'
    
    sub_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/news_play_title')
    if sub_title is None or sub_title == '':
        MrTestTemplate.failed_and_take_snapshot('verify sub title text of news tab')
        return
    else:
        print 'News tab sub title: %s' %sub_title.split(' ')[0]
        print 'PASS, verify sub title text of news tab'

    player_view = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/news_player_view')
    if player_view is None:
        MrTestTemplate.failed_and_take_snapshot('verify video player of news tab')
    else:
        print 'Player view: %s' %type(player_view)
        print 'PASS, verify player of news tab'
        MrBaseMrUtils.take_snapshot(g_device, g_snapshot_dir)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
MrTestTemplate.main(os.path.basename(__file__), 
                    test_setup,
                    test_open_bottom_film_tab, 
                    test_open_bottom_tv_tab, 
                    test_open_bottom_children_tab,
                    test_open_bottom_variety_tab,
                    test_open_news_tab_of_right_area)
