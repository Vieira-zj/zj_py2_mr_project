# -*- coding: utf-8 -*-
'''
@author: zhengjin
'''

import os
import sys

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrRunner import MrTestRunner
from MrUtils import MrBaseConstants
from MrUtils import MrBaseMrUtils

# ----------------------------------------------------------
# Demo test cases
# ----------------------------------------------------------
def mr_test_demo_21(device):
# test get text of textview
    
    print 'run mr_test_demo_01'
    MrBaseMrUtils.start_activity(device, MrBaseConstants.g_component_filemanager)
    MrBaseMrUtils.mr_sleep(3.0)
    view_title = MrBaseMrUtils.get_text_by_id(device, 'id/tab_title')
    print view_title
    
def mr_test_demo_22(device):
# test get text of textview on dynamic page
    
    print 'run mr_test_demo_02'
    MrBaseMrUtils.start_activity(device, MrBaseConstants.g_component_video_news)
    MrBaseMrUtils.mr_sleep(3.0)
    view_title = MrBaseMrUtils.get_text_by_id(device, 'id/news_special_list_item_title')
    print view_title
    
# test different activity
def mr_test_demo_23(device):

    print 'TODO'


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def mr_test_setup():
    MrBaseConstants.init_g_path_vars(MrTestRunner.g_user_run_num)

def mr_test_main():

    mr_test_setup()
        
    device = MrBaseMrUtils.get_easy_device(MrTestRunner.g_user_device_no)
    mr_test_demo_23(device)
    

if __name__ == '__main__':

    reload(sys)
    sys.setdefaultencoding('utf-8')

    mr_test_main()
    
    pass