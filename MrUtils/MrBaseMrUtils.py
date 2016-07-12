# -*- coding: utf-8 -*-
'''
Created on 2015-7-9

@author: zhengjin

Include the functions called from monkeyrunner test case.

'''

import os
import sys
import time
import logging

from MrUtils import MrBaseConstants

from com.android.monkeyrunner import MonkeyRunner as mr
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
def get_easy_device(device_no):
    
    device = device_connect_and_return(device_no)
    easy_device = EasyMonkeyDevice(device)
    
    if easy_device == None:
        print 'Error when get the mr device object!'
        exit(1)

    return easy_device

def device_connect_and_return(device_no):

    print 'connect to device %s' %(device_no)
    device = mr.waitForConnection(MrBaseConstants.g_wait_time, device_no)
    if not device:
        print >> sys.stderr,"fail"
        sys.exit(1)

    return device

def start_activity(device, component_name):
    
    print 'start activity %s' %(component_name)
    device.startActivity(component=component_name) 
    wait_for_activity_started(device, component_name)
    
def wait_for_activity_started(device, component_name):
    
    for i in range(0,int(MrBaseConstants.g_time_out)):
        ret = device.shell('dumpsys activity | grep mFocusedActivity')
        if ret.find(component_name) >= 0:
            return
        else:
            mr.sleep(MrBaseConstants.g_short_wait_time)
            print 'Wait for activity start %s second.' %(i + 1)
    
def take_snapshot(device, dir_path):
    
    file_name = 'mr_snapshot_%s.%s' %(time.strftime('%y-%m-%d %H_%M_%S'), MrBaseConstants.g_capture_suffix)
    file_path = os.path.join(dir_path, file_name)
    print 'snapshot save to %s' %(file_path)
    
    result = device.takeSnapshot()
    result.writeToFile(file_path, MrBaseConstants.g_capture_suffix);

def adb_screen_capture(dir_path):
    
    file_name = 'capture_%s.%s' %(time.strftime('%y-%m-%d %H_%M_%S'), MrBaseConstants.g_capture_suffix)
    path = '%s/%s' %(dir_path, file_name)
    cmd = 'adb shell screencap -p %s' %(path)
    print cmd
    os.system(cmd)


# ----------------------------------------------------
# Hierarchy functions
# ----------------------------------------------------
def get_hierarchy_viewer(device):
    return device.getHierarchyViewer()

def find_view_by_id(device, view_id):

    print 'get view by id -> %s' %(view_id)
    hierarchy_viewer = get_hierarchy_viewer(device)
    view_node = hierarchy_viewer.findViewById(view_id)
    
    return view_node

def get_text_by_id(device, view_id):

    print 'get text view by id -> %s' %(view_id)
    hierarchy_viewer = get_hierarchy_viewer(device)
    view_node = hierarchy_viewer.findViewById(view_id)

    return hierarchy_viewer.getText(view_node).encode('utf8')

def wait_for_view_existance(device, view_id, timeout=3):

    for i in range(timeout):
        view_node = find_view_by_id(device, view_id)
        if view_node is None:
            print 'try to find object %d times, and wait 1 sec' %(i + 1)
            time.sleep(1)
        else:
            print 'True, wait for view %s existance'
            return
            
    print 'False, wait for view %s existance. Test exit'
    exit(1)
    
    
# ----------------------------------------------------
# Device actions
# ----------------------------------------------------
def press_and_wait(device, key, wait_time=MrBaseConstants.g_short_wait_time):

    device.press(key)
    mr.sleep(wait_time)

def input_and_wait(device, text, wait_time=MrBaseConstants.g_short_wait_time):

    device.type(text)
    mr.sleep(wait_time)


# ----------------------------------------------------
# Log functions
# ----------------------------------------------------
def init_log_config(prj_path):

    long_format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    short_format = '%(filename)-12s: %(levelname)-8s %(message)s'
    
    long_date_format = '%a, %d %b %Y %H:%M:%S'
    short_date_format = '%d %b %H:%M:%S'

    # define console log
    logging.basicConfig(level=logging.DEBUG, format=short_format, datefmt=short_date_format)
    
    # define file log
    file_name = 'mr_test_log_%s.log' %(time.strftime('%y-%m-%d %H_%M_%S'))
    file_path = os.path.join(prj_path,'mr_test_log',file_name)
    print 'log file path ---> %s' %file_path
    log_file = logging.FileHandler(filename=file_path, mode='w')
    log_file.setLevel(logging.WARN)
    log_file.setFormatter(logging.Formatter(fmt=long_format, datefmt=long_date_format))
    logging.getLogger('').addHandler(log_file)


# ----------------------------------------------------
# Main
# ----------------------------------------------------
if __name__ == '__main__':

    pass
