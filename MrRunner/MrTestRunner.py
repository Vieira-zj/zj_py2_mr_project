# -*- coding: utf-8 -*-
'''
@author: zhengjin

Executor to run the monkeyrunner scripts.

'''
import os
import time

from MrUtils import MrBaseConstants
from MrUtils import MrBaseUtils

# ----------------------------------------------------------
# User defined variables
# ----------------------------------------------------------
g_user_device_ip = '172.17.5.106'
g_user_device_port = '5555'
g_user_device_no = '%s:%s' %(g_user_device_ip, g_user_device_port)

g_user_run_num = '01'
g_user_run_script = 'MrTestLauncher.py'

g_user_logcate_log_level = 'I'
g_user_flag_create_adb_connect = False


# ----------------------------------------------------------
# Build tests
# ----------------------------------------------------------
def get_all_tests_from_dir(dir_path):
    tests = []
    tc_prefix = MrBaseConstants.g_mr_tcs_prefix
    
    f_names = os.listdir(dir_path)
    for f_name in f_names:
        if f_name.startswith(tc_prefix):
            tests.append(os.path.join(dir_path, f_name))

    if len(tests) > 0:
        return tests
    else:
        print 'Error, no test case found!'
        exit(1)

def run_setup():
    os.environ['MR_PROJECT_PATH'] = os.path.dirname(os.getcwd())
    MrBaseConstants.init_g_path_vars_for_win(g_user_run_num)

    if g_user_flag_create_adb_connect:
        MrBaseUtils.adb_connect_with_root(g_user_device_ip)

#     MrBaseUtils.mkdir_for_shell(MrBaseConstants.g_captures_dir_path_for_shell)
#     MrBaseUtils.create_log_dir_for_win(MrBaseConstants.g_captures_dir_path_for_win)

def run_clearup():
    print 'TODO:'
#     MrBaseUtils.pull_mr_logs(MrBaseConstants.g_mr_log_sub_dir_path_for_shell, 
#                              MrBaseConstants.g_mr_log_sub_dir_path_for_win)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def run_mr_script(script_path):
    cmd = '%s %s' %(MrBaseConstants.get_mr_run_bat_path(), script_path)
    print 'Run script: %s' %(cmd)
    ret = os.system(cmd)
    
    if ret != 0:
        print 'Error, when run the monkeyrunner command.'

def mr_process():
    test_scripts = []
    test_scripts.append(os.path.join(MrBaseConstants.g_mr_tcs_dir_path, g_user_run_script))
    
    if len(test_scripts) == 0:
        print 'Error, no test case added!'
        exit(1)
    
    for test_script in test_scripts:
        print 'START ---> run test script: %s' %(test_script)
        run_mr_script(test_script)
        print 'END ---> run test script: %s' %(test_script)
        
def main(fn):
    run_setup()
    start = int(time.clock())
    fn()
    end = int(time.clock())
    run_clearup()
    
    print "MonkeyRunner finished and cost %d minutes and %s seconds!" %((end-start)/60, (end-start)%60)


if __name__ == '__main__':

    main(mr_process)
    pass
