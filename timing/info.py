#!/usr/bin/env python
import os
from colors import *

# get cpuinfo to check rtm (supporting Intel TSX)
print(BOLD)
print(f"{BLACK}Get processor info from {BLUE}/proc/cpuinfo{BLACK}")
os.system("cat /proc/cpuinfo | grep 'model name' | head -n 1")
try:
    f = open("/proc/cpuinfo", "rb")
    data = f.read()
    if 'rtm' not in data:
        print(f"{RED}Error, your processor does not support Intel TSX")
        quit()
    else:
        print(f"{GREEN}This processor supports Intel TSX")
except:
    print(f"{RED}Error: cannot open /proc/cpuinfo")
    quit()


# Run uname -a to check the version of Linux Kernel
print(BLACK + "\nRun " + BLUE + "uname -a" + BLACK + " to check OS version" + BLACK)
os.system("uname -a")

# get cmdline to check if kaslr is enabled as bootargs
print(BLACK + "\nRun " + BLUE + "cat /proc/cmdline" + BLACK + " to see bootargs" + BLACK)
os.system("cat /proc/cmdline")
try:
    f = open("/proc/cmdline", "rb")
    data = f.read()
    if 'kaslr' not in data:
        print(f"{RED}Error, the kernel is not set with kaslr flag")
        quit()
    else:
        print(f"{GREEN}The kernel is set with kaslr flag")
except:
    print(f"{RED}Error: cannot open /proc/cmdline")
    quit()


