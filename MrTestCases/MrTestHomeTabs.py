# -*- coding: utf-8 -*-
'''
Created on 2016-7-27

@author: zhengjin

Test the tabs on launcher home.

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


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_init():
    global g_device
    global g_hierarchy_viewer
 
    g_device = MrTestTemplate.g_device
    g_hierarchy_viewer = MrTestTemplate.g_hierarchy_viewer

def test_open_bottom_film_tab():
    MrTestTemplate.open_launcher_tab((250,750))

    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/maintitle')
    if MrTestTemplate.verify_null_or_empty(main_title):
        MrTestTemplate.failed_and_take_snapshot('test_open_bottom_film_tab')
    else:
        print 'Film tab main title: %s' %main_title
        print 'PASS, test_open_bottom_film_tab'
    
def test_open_bottom_tv_tab():
    MrTestTemplate.open_launcher_tab((450,750))
    
    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/maintitle')
    if MrTestTemplate.verify_null_or_empty(main_title):
        MrTestTemplate.failed_and_take_snapshot('test_open_bottom_tv_tab')
    else:
        print 'TV tab main title: %s' %main_title
        print 'PASS, test_open_bottom_tv_tab'
        
def test_open_bottom_children_tab():
    MrTestTemplate.open_launcher_tab((600,750))

    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/maintitle')
    if MrTestTemplate.verify_null_or_empty(main_title):
        MrTestTemplate.failed_and_take_snapshot('test_open_bottom_children_tab')
    else:
        print 'Children tab main title: %s' %main_title
        print 'PASS, test_open_bottom_children_tab'
    
def test_open_bottom_variety_tab():
    MrTestTemplate.open_launcher_tab((850,750))
    
    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/maintitle')
    if MrTestTemplate.verify_null_or_empty(main_title):
        MrTestTemplate.failed_and_take_snapshot('test_open_bottom_variety_tab')
    else:
        print 'Variety tab main title: %s' %main_title
        print 'PASS, test_open_bottom_variety_tab'


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
MrTestTemplate.main(os.path.basename(__file__), 
                    test_init,
                    test_open_bottom_film_tab, 
                    test_open_bottom_tv_tab, 
                    test_open_bottom_children_tab,
                    test_open_bottom_variety_tab)
