# -*- coding: utf-8 -*-
'''
@author: zhengjin
'''

import sys

from com.android.monkeyrunner import MonkeyRunner as mr  


# ----------------------------------------------------------
# Demo script
# ----------------------------------------------------------
def mr_test_demo():
    
    #connect device
    device = mr.waitForConnection(3.0, '172.17.5.134:5555')
    if not device:
        print >> sys.stderr,"fail"  
        sys.exit(1)

    # start activity
#     device.startActivity(component='tv.fun.settings/.general.GeneralSettingsActivity')
#     mr.sleep(3.0)
    
    #input helloworld  
#     device.type('helloworld')
    
#     device.press('KEYCODE_ENTER')  
#     device.press('KEYCODE_BACK')  
    
    #takeSnapshot
#     mr.sleep(10.0)
#     result = device.takeSnapshot()  
#     result.writeToFile('d:\shot1.png','png');
    
    #run shell commands
#     ret = device.shell('dumpsys activity | grep mFocusedActivity')
#     print ret
#     print ret.find(MrBaseConstants.g_component_settings)

#     nodes = device.getViewsByText('少儿')
#     for node in nodes:
#         print node.getViewClass();


if __name__ == '__main__':

    mr_test_demo()
    pass