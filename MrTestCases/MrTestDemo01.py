# -*- coding: utf-8 -*-
'''
@author: zhengjin

A demo to test the APIs for MonkeyRunner, MonkeyDevice and Hierarchyviewer.

'''

import sys

from com.android.monkeyrunner import MonkeyRunner as mr  
from com.android.monkeyrunner.easy import EasyMonkeyDevice,By
from com.android.monkeyrunner import MonkeyDevice

# ----------------------------------------------------------
# Demo scripts
# ----------------------------------------------------------
def mr_test_demo_for_device():
    print 'test apis for mr and device.'
    
#     device = get_monkey_device()

#     device.startActivity(component='tv.fun.settings/.general.GeneralSettingsActivity')
#     mr.sleep(3.0)
    
#     device.type('helloworld')
    
#     device.press('KEYCODE_ENTER')  
#     device.press('KEYCODE_BACK')  
    
    # takeSnapshot
#     mr.sleep(10.0)
#     result = device.takeSnapshot()  
#     result.writeToFile('d:\shot1.png','png');
    
    # run shell commands
#     ret = device.shell('dumpsys activity | grep mFocusedActivity')
#     print ret
#     print ret.find(MrBaseConstants.g_component_settings)

    # get UI objects, failed
#     root = device.getRootView()
#     print root.getViewClass()

#     list_views = device.getViewsByText('通用设置')
#     print len(list_views)

def mr_test_demo_for_hierarchyviewer():
    print 'test the apis for hierarchyviewer.'
    
#     device = get_monkey_device()
#     hierarchy = device.getHierarchyViewer()

    # setting home page
#     title = hierarchy.findViewById('id/setting_title')
#     point =  hierarchy.getAbsoluteCenterOfView(title)  # Point {960, 171}
#     print 'position x -> %d, y -> %d' %(point.x, point.y)

    # launcher home page
#     title = hierarchy.findViewById('id/title')  # get the 1st match view
#     point = hierarchy.getAbsoluteCenterOfView(title)
#     print 'touch at (%d,%d)' %(point.x, point.y)
#     device.touch(point.x, point.y, 'DOWN_AND_UP')
#     mr.sleep(1)
#     device.press('KEYCODE_ENTER')
#     mr.sleep(5)
    
    # film list page
#     tab_title = hierarchy.findViewById('id/tab_title')
#     print hierarchy.getText(tab_title).encode('utf8')
#     card_title = hierarchy.findViewById('id/title')
#     print hierarchy.getText(card_title).encode('utf8')
    
    # news page
#     title = hierarchy.findViewById('id/news_special_list_item_title')
#     print hierarchy.getText(title).encode('utf8')
#     sub_title = hierarchy.findViewById('id/news_play_title')
#     print hierarchy.getText(sub_title).encode('utf8')
    
def mr_test_demo_for_easydevice():
    print 'test apis for easydevice.'
    
    device = get_monkey_device()
    easy_device = EasyMonkeyDevice(device)
    
    # launcher home page
#     device.press('KEYCODE_HOME')
#     mr.sleep(1)
#     easy_device.touch(By.id('id/title'), MonkeyDevice.DOWN_AND_UP)
#     mr.sleep(1)
#     device.press('KEYCODE_ENTER')
#     mr.sleep(5)
    
    # film list page
#     tab_title_text = easy_device.getText(By.id('id/tab_title'))
#     print tab_title_text.encode('utf8')

    # touch on card of right area
    easy_device.touch(By.id('id/subtitle'), MonkeyDevice.DOWN_AND_UP)
    mr.sleep(1)

def get_monkey_device():
    # create monkey device
    device = mr.waitForConnection(3.0, '172.17.5.134:5555')
    if not device:
        print >> sys.stderr,"fail"  
        sys.exit(1)

    return device


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
# mr_test_demo_for_device()
# mr_test_demo_for_hierarchyviewer()
mr_test_demo_for_easydevice()
