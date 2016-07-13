# -*- coding: utf-8 -*-
'''
Created on 2015-7-9

@author: zhengjin

Include non-monkeyrunner functions.

'''

import os
import time
import subprocess

# ----------------------------------------------------
# ADB functions
# ----------------------------------------------------
def verify_adb_devices_serialno():
    cmd = 'adb get-serialno'
    print cmd

    if 'unknown' in os.popen(cmd).read():
        return False
    else:
        return True

def adb_connect(device_ip):
    try_adb_connect_times = 3
    wait_time = 3
    cmd = 'adb connect %s' %(device_ip)

    for i in range(0,try_adb_connect_times):
        os.system(cmd)
        print 'try to connect to adb device, %d times.' %(i + 1)
        if verify_adb_devices_serialno():  # verify connect success
            return True
        time.sleep(wait_time)
    
    return False

def adb_connect_with_root(device_ip):
    if not adb_connect(device_ip):  # adb connect
        print 'Error, when adb connect to the device!'
        exit(1)
        
    if not run_cmd_adb_root_from_subprocess():
        print 'Error, when run adb as root!'
        exit(1)

    if not adb_connect(device_ip):   # adb connect as root
        print 'Error, when adb connect to the device with root!'
        exit(1)

def run_cmd_adb_root_from_subprocess():
    cmd = 'adb root'
    print cmd
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()

    lines_error = p.stderr.readlines()
    if len(lines_error) > 0:
        for line in lines_error:
            print line
        print 'Error, adb root failed!'
        return False

    for line in p.stdout.readlines():
        if 'already' in line:
            print 'adbd is already running as root.'
            return True
        elif 'adbd as root' in line:
            print 'adb root success.'
            return True
        else:
            print 'Error, adb root failed.'
            return False

def build_logcat_command(log_path, log_level):
    return 'adb logcat -c && adb logcat -f %s -v threadtime *:%s' %(log_path, log_level)

def pull_mr_logs(src_path, target_path):
    cmd = 'adb pull %s %s' %(src_path, target_path)
    print cmd
    os.system(cmd)


# ----------------------------------------------------
# IO functions
# ----------------------------------------------------
def mkdir_for_shell(path_dir):
    cmd = 'adb shell mkdir -p %s' %(path_dir)
    print cmd
    os.system(cmd)

def remove_dir_for_shell(path_dir):
    cmd = 'adb shell rm -rf %s' %(path_dir)
    print cmd
    os.system(cmd)

def create_log_dir_for_win(path_dir):
    if os.path.exists(path_dir):
        print 'Warning, the path (%s) is exist.' %(path_dir)
        return
    else:
        os.makedirs(path_dir)
        time.sleep(1)
        print 'create directory %s on local.' %(path_dir)


if __name__ == '__main__':

    pass