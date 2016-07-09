# -*- coding: utf-8 -*-
'''
@author: zhengjin
'''

import sys

from com.android.monkeyrunner import MonkeyRunner as mr  

# ----------------------------------------------------------
# Demo scripts
# ----------------------------------------------------------
def mr_test_demo_for_device():
    
    device = get_connected_device()

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

def mr_test_demo_for_easydevice():
    
    print 'TODO'

def mr_test_demo_for_hierarchyviewer():
    
    device = get_connected_device()

#     h = device.getHierarchyViewer()
#     node = h.findViewById('id/setting_title')
#     print node


def get_connected_device():

    #connect device
    device = mr.waitForConnection(3.0, '172.17.5.134:5555')
    if not device:
        print >> sys.stderr,"fail"  
        sys.exit(1)

    return device


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
if __name__ == '__main__':

    mr_test_demo_for_device()

    pass