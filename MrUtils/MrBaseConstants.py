# -*- coding: utf-8 -*-

'''
@author: zhengjin

Include all the global constant variables.

'''

import time
import os

# ----------------------------------------------------
# Constant global variables
# ----------------------------------------------------
g_component_settings = 'tv.fun.settings/.general.GeneralSettingsActivity'
g_component_filemanager = 'tv.fun.filemanager/.FunFileManagerActivity'
g_component_launcher_home = 'com.bestv.ott/.home.HomeActivity'
g_component_video_news = 'com.besttv.ott/.NewsHomeActivity'

g_cur_date = time.strftime('%Y%m%d')
g_cur_time = time.strftime('%y-%m-%d %H_%M_%S')

g_short_wait_time = 1.0  # seconds
g_wait_time = 3.0  # seconds
g_long_wait_time = 5.0  # seconds
g_time_out = 8.0

g_mr_tcs_prefix = 'MrTest'
g_capture_suffix = 'png'


# ----------------------------------------------------
# Global paths
# ----------------------------------------------------
g_mr_prj_root_path = ''
g_mr_tcs_dir_path = ''

g_mr_log_root_dir_path_for_win = ''
g_mr_log_sub_dir_path_for_win = ''
g_mr_log_file_path_for_win = ''
g_captures_dir_path_for_win = ''

g_mr_log_root_dir_path_for_shell = ''
g_mr_log_sub_dir_path_for_shell = ''
g_captures_dir_path_for_shell = ''
g_logcat_file_path_for_shell = ''

def init_g_path_vars_for_win(run_num):
    global g_mr_prj_root_path
    global g_mr_tcs_dir_path
    
    global g_mr_log_root_dir_path_for_win
    global g_mr_log_sub_dir_path_for_win
    global g_mr_log_file_path_for_win
    global g_captures_dir_path_for_win
    
    g_mr_prj_root_path = os.environ['MR_PROJECT_PATH']
    g_mr_tcs_dir_path = os.path.join(g_mr_prj_root_path, 'MrTestCases')
    
    g_mr_log_root_dir_path_for_win = r'%s\mr_logs' %(g_mr_prj_root_path)
    g_mr_log_sub_dir_path_for_win = r'%s\mr_logs_%s_%s' %(g_mr_log_root_dir_path_for_win, g_cur_date, run_num)
    g_mr_log_file_path_for_win = os.path.join(g_mr_log_sub_dir_path_for_win, ('mr_log_%s_%s.log' %(g_cur_date, run_num)))
    g_captures_dir_path_for_win = r'%s\captures' %(g_mr_log_sub_dir_path_for_win)

def init_g_path_vars_for_shell(run_num):
    global g_mr_log_root_dir_path_for_shell
    global g_mr_log_sub_dir_path_for_shell
    global g_captures_dir_path_for_shell
    global g_logcat_file_path_for_shell
    
    g_mr_log_root_dir_path_for_shell = '/sdcard/testlogs/mr_logs'
    g_mr_log_sub_dir_path_for_shell = '%s/mr_logs_%s_%s' %(g_mr_log_root_dir_path_for_shell, g_cur_date, run_num)
    g_captures_dir_path_for_shell = '%s/captures' %(g_mr_log_sub_dir_path_for_shell)
    g_logcat_file_path_for_shell = '%s/mr_logcat_%s_%s.log' %(g_mr_log_sub_dir_path_for_shell, run_num, g_cur_date)


# ----------------------------------------------------
# Android key codes
# ----------------------------------------------------
KEY_ENTER = 'KEYCODE_ENTER'
KEY_HOME = 'KEYCODE_HOME'
KEY_BACK = 'KEYCODE_BACK'
KEY_UP = 'KEYCODE_DPAD_UP'
KEY_DOWN = 'KEYCODE_DPAD_DOWN'
KEY_LEFT = 'KEYCODE_DPAD_LEFT'
KEY_RIGHT = 'KEYCODE_DPAD_RIGHT'
KEY_CENTER = 'KEYCODE_DPAD_CENTER'
KEY_CHANNEL_PLUS = 'KEYCODE_CHANNEL_UP'  # 166
KEY_CHANNEL_MIN = 'KEYCODE_CHANNEL_DOWN'  # 167
KEY_TV = 'unknown'


# ----------------------------------------------------
# TouchPressType
# ----------------------------------------------------
PRESS_TYPE_UP = 'UP'
PRESS_TYPE_DOWN = 'DOWN'
PRESS_TYPE_DU = 'DOWN_AND_UP'


# ----------------------------------------------------
# Functions
# ----------------------------------------------------
def get_mr_run_bat_path():
    paths = os.environ['ANDROID_HOME'].split(';')
    for path in paths:
        if path.endswith('tools'):
            return os.path.join(path, 'monkeyrunner.bat')

    print 'Error, when get the path for android sdk tools.'
    exit(1)
