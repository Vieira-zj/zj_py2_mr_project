# -*- coding: utf-8 -*-
'''
Created on 2015-7-9

@author: zhengjin

Include the wrapped functions which use the monkeyrunner APIs.

'''

import os
import sys
import time
# import logging

from MrUtils import MrBaseConstants

from com.android.monkeyrunner import MonkeyRunner as mr, MonkeyDevice
# from com.android.monkeyrunner import MonkeyDevice as md
# from com.android.monkeyrunner import MonkeyImage as mi
# from com.android.monkeyrunner import MonkeyView
from com.android.monkeyrunner.easy import EasyMonkeyDevice
# from com.android.monkeyrunner.easy import By

# from com.android.chimpchat.hierarchyviewer import HierarchyViewer
# from com.android.hierarchyviewerlib.models import ViewNode


# ----------------------------------------------------
# Device functions
# ----------------------------------------------------
def get_monkey_device(device_no):
    device = mr.waitForConnection(MrBaseConstants.g_wait_time, device_no)
    if not device:
        print >> sys.stderr,"fail"
        sys.exit(1)

    return device

def get_easy_device(device_no):
    device = get_monkey_device(device_no)
    easy_device = EasyMonkeyDevice(device)
    if easy_device is None:
        print 'Error, when get the mr easy device object!'
        exit(1)

    return easy_device

def start_activity(device, component_name):
    print 'start activity %s' %(component_name)
    device.startActivity(component=component_name) 
    wait_for_activity_started(device, component_name)
    
def wait_for_activity_started(device, component_name):
    for i in range(0, int(MrBaseConstants.g_time_out)):
        ret = device.shell('dumpsys activity | grep mFocusedActivity')
        if ret.find(component_name) >= 0:
            return True
        mr.sleep(MrBaseConstants.g_short_wait_time)
    
    return False
    
def take_snapshot(device, dir_path):
    file_name = 'mr_snapshot_%s.%s' %(time.strftime('%y-%m-%d_%H%M%S'),MrBaseConstants.g_pic_suffix)
    file_path = os.path.join(dir_path, file_name)
    
    print 'save snapshot to %s' %(file_path)
    result = device.takeSnapshot()
    result.writeToFile(file_path, MrBaseConstants.g_pic_suffix)

def adb_screen_capture(dir_path):
    file_name = 'capture_%s.%s' %(time.strftime('%y-%m-%d_%H%M%S'),MrBaseConstants.g_pic_suffix)
    path = '%s/%s' %(dir_path, file_name)
    cmd = 'adb shell screencap -p %s' %path
    
    print cmd
    os.system(cmd)


# ----------------------------------------------------
# Hierarchy viewer functions
# ----------------------------------------------------
def get_hierarchy_viewer(device):
    viewer = None
    try:
        viewer = device.getHierarchyViewer()
    except Exception, e:
        print 'Exception, get the hierarchy viewer!'
        print 'Exception %s' %e
        exit(1)
        
    if viewer is None:
        print 'Error, get the hierarchy viewer!'
        exit(1)
    
    return viewer

def find_view_by_id(hierarchy_viewer, view_id, root_node=None):
    print 'get view by id: %s' %view_id
    
    view_node = None
    try:
        if root_node is None:
            view_node = hierarchy_viewer.findViewById(view_id)
        else:
            view_node = hierarchy_viewer.findViewById(view_id, root_node)
    except Exception, e:
        print 'Exception, find the view by id(%s)' %view_id
        print 'Exception %s' %e
    
    return view_node

def get_text_by_id(hierarchy_viewer, view_id):
    print 'get text of view: %s' %view_id

    ret_text = ''
    view_node = find_view_by_id(hierarchy_viewer, view_id)
    if view_node is not None:
        try:
            ret_text = hierarchy_viewer.getText(view_node).encode('utf-8')
        except Exception, e:
            print 'Exception when get the text of view(%s)' %view_id
            print 'Exception %s' %e

    return ret_text

def get_text_of_viewnode(hierarchy_viewer, view_node):
    ret_text = ''
    try:
        ret_text = hierarchy_viewer.getText(view_node).encode('utf-8')
    except Exception, e:
        print 'Exception %s' %e

    return ret_text

def wait_for_view_existance(hierarchy_viewer,view_id,timeout=MrBaseConstants.g_wait_time):
    for i in range(1,(timeout+1)):
        print 'try to find object %d times, and wait 1 sec' %i
        view_node = find_view_by_id(hierarchy_viewer, view_id)
        if view_node is not None:
            return True
        time.sleep(1)

    return False


# ----------------------------------------------------
# Device actions
# ----------------------------------------------------
def mr_wait(wait_time):
    mr.sleep(wait_time)  # seconds

def press_and_wait(device, key, wait_time=MrBaseConstants.g_short_wait_time):
    device.press(key, MonkeyDevice.DOWN_AND_UP)
    mr.sleep(wait_time)

def input_and_wait(device, text, wait_time=MrBaseConstants.g_short_wait_time):
    device.type(text)
    mr.sleep(wait_time)

def touch_and_wait(device, point, wait_time=MrBaseConstants.g_short_wait_time):
    device.touch(point[0], point[1], MonkeyDevice.DOWN_AND_UP)
    mr_wait(wait_time)

def do_repeat_press_by_times(device, key, press_times):
    sleep_time = 0.5
    for i in range(0,press_times):
        press_and_wait(device, key, sleep_time)
    
def do_repeat_press_during_time(device, key, during):
    sleep_time = 0.5
    start = time.clock()
    while ((time.clock() - start) < during):
        press_and_wait(device, key, sleep_time)
