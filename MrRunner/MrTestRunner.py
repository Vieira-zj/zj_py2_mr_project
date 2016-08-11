# -*- coding: utf-8 -*-
'''
@author: zhengjin

Executor to run the monkeyrunner test scripts.

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
g_user_run_during = 0  # seconds. if = 0, run only once

# g_user_run_scripts = ('MrTestHomeTabs.py','MrTestPlayFilm.py','MrTestNewsTab.py',
#                       'MrTestTabsOfRightArea.py', 'MrTestPlayTvSerial.py')
g_user_run_scripts = ['MrTestPlayTvSerial.py']  # run single script

g_user_flag_write_report = False
g_user_flag_create_adb_connect = False


# ----------------------------------------------------------
# Helper functions
# ----------------------------------------------------------
def get_all_tests_from_dir(dir_path):
    run_scripts = []
    tc_prefix = MrBaseConstants.g_mr_tcs_prefix
    
    f_names = os.listdir(dir_path)
    for f_name in f_names:
        if f_name.startswith(tc_prefix):
            run_scripts.append(os.path.join(dir_path, f_name))

    if len(run_scripts) > 0:
        return run_scripts
    else:
        print 'Error, no test case found at %s!' %dir_path
        exit(1)

def run_mr_script(script_path):
    cmd = '%s %s' %(MrBaseConstants.get_mr_run_bat_path(), script_path)
    if g_user_flag_write_report:
        cmd = '%s >> %s' %(cmd, MrBaseConstants.g_mr_log_file_path_for_win)

    print 'Run script: %s' %cmd
    ret = os.system(cmd)
    if ret != 0:
        print 'Error, when run the monkeyrunner command!'

def run_setup():
    os.environ['MR_PROJECT_PATH'] = os.path.dirname(os.getcwd())
    MrBaseConstants.init_g_path_vars_for_win(g_user_run_num)

    if not os.path.exists(MrBaseConstants.g_snapshot_dir_path_for_win):
        os.makedirs(MrBaseConstants.g_snapshot_dir_path_for_win)

    if g_user_flag_create_adb_connect:
        MrBaseUtils.adb_connect_with_root(g_user_device_ip)

def run_clearup():
    print 'TODO: logs'


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def mr_process():
    test_scripts = []
    for run_script in g_user_run_scripts:
        test_scripts.append(os.path.join(MrBaseConstants.g_mr_tcs_dir_path, run_script))
    if len(test_scripts) == 0:
        print 'Error, no test case added!'
        exit(1)
    
    for test_script in test_scripts:
        print '%s: START ---> run TEST SCRIPT: %s' %(MrBaseConstants.g_cur_time,test_script)
        run_mr_script(test_script)
        print '%s: END ---> run TEST SCRIPT: %s\n' %(MrBaseConstants.g_cur_time,test_script)
        
def main(fn, during=0):
    start = int(time.clock())
    run_setup()

    run_times = 1
    if during > 0:
        while ((time.clock() - start) < during):
            print '-------- Run test script suite %d times --------' %run_times
            fn()
            run_times += 1
    else:   # run test only 1 time
        fn()

    run_clearup()
    end = int(time.clock())
    print "MonkeyRunner finished and cost %d minutes and %s seconds!" %((end-start)/60, (end-start)%60)


if __name__ == '__main__':

    main(mr_process, g_user_run_during)
    pass
