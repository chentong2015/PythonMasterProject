#!/usr/bin/python
# coding=utf-8

import getopt
import sys
import time


def usage():
    print(" description    : check packet validation")
    print(" --help         : Print usage and exit")
    print(" --verbose      : verbose mode")
    print(" --site         : site")


if __name__ == '__main__':
    # __name__是内置变量，可用于表示当前模块的名字
    # 如果一个.py文件(模块)被直接运行时，则其没有包结构，其__name__值为__main__，即模块名为__main__
    print(__name__)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:v", ["help", "site="])
    except getopt.GetoptError:
        print("Error....")
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-v", "--verbose"):
            bVERBOSE = True
            continue
        if o in ("-s", "--site"):
            print("in sample_test site=" + a)
            if a.find("LL") != -1:
                print("wait 5")
                time.sleep(5)
            mSit = a
            continue
        if o in ("-h", "--help"):
            gRESULT = "FAILURE"
            usage()
            sys.exit(0)
        gRESULT = "SUCCESS"
    print("SUCCESS for in sample_test :test executed !")

