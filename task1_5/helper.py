#!/usr/bin/python
import datetime
import subprocess
import sys
import argparse

helper = argparse.ArgumentParser()
helper.add_argument('-t', '--time', help='displays the current time', action="store_true")
helper.add_argument('-d', '--date', help='displays the current date', action="store_true")
helper.add_argument('-u', '--uname', help='displays the current user', action="store_true")
helper.add_argument('-v', '--version', help='displays the current version of python', action="store_true")
helper.add_argument('-T', '--tree', help='displays files in the current directory', action="store_true")
args = helper.parse_args()
if args.time:
    print datetime.datetime.now().time().strftime('%H:%M:%S')
if args.date:
    print datetime.datetime.now().date().strftime('%d.%m.%Y')
if args.uname:
    print os.getlogin()
if args.version:
    print sys.version
if args.tree:
    print os.listdir(os.getcwd())
if len(sys.argv) == 1:
    helper.print_help()