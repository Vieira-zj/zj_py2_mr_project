# -*- coding: utf-8 -*-
'''
@author: zhengjin
'''

import os
import sys
import time
import unittest
import logging

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrRunner import MrTestRunner
from MrUtils import MrBaseConstants
from MrUtils import MrBaseMrUtils

# ----------------------------------------------------------
# Demo test cases
# ----------------------------------------------------------
class mr_test_demos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'class setUp.'
        
    @classmethod
    def tearDownClass(cls):
        print 'class tearDown.'

    def setUp(self):
        print 'method setUp.'
        self.device = MrBaseMrUtils.get_easy_device(MrTestRunner.g_user_device_no)
        
    def tearDown(self):
        print 'method tearDown.'

    def test_mr_demo_21(self):
    # test get text of textview
        print 'Run test case -----> mr_test_demo_01' 
        MrBaseMrUtils.start_activity(self.device, MrBaseConstants.g_component_filemanager)
        time.sleep(3.0)
        view_title = MrBaseMrUtils.get_text_by_id(self.device, 'id/tab_title')
        
        logging.warn('Text of title ---> %s' %view_title)
        self.assertTrue(len(view_title) > 0)
        
    def ignore_test_mr_demo_22(self):
    # test get text of textview on dynamic page
        logging.debug('Run test case -----> run mr_test_demo_02')
        MrBaseMrUtils.start_activity(self.device, MrBaseConstants.g_component_video_news)
        time.sleep(3.0)
        view_title = MrBaseMrUtils.get_text_by_id(self.device, 'id/news_special_list_item_title')
        logging.debug('Text of title ---> %s' %view_title)
        
    # test different activity
    def ignore_test_mr_demo_23(self):
        logging.warn('TODO: test_mr_demo_23')


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def init_env():
    MrBaseConstants.init_g_path_vars(MrTestRunner.g_user_run_num)
    MrBaseMrUtils.init_log_config(MrBaseConstants.g_mr_prj_root_path)


if __name__ == '__main__':

    init_env()
    unittest.main()
    
    pass