#!/usr/bin/env python
import os
import public
import subprocess


PATHS = [
    os.path.expanduser("~/Applications/HardwareMonitor.app/Contents/MacOS/hwmonitor"),
    "/Applications/HardwareMonitor.app/Contents/MacOS/hwmonitor",
]
for PATH in PATHS:
    if os.path.exists(PATH):
        break


@public.add
def read():
    """return string with `hwmonitor` output"""
    return subprocess.check_output([PATH], stderr=subprocess.PIPE).decode("utf-8")


@public.add
def sensors():
    """return dict with sensor names as keys and temperature as values"""
    result = dict()
    for l in read().splitlines():
        if ":" in l:
            k, v = l.split(":")
            result[k] = int(v.split(' ')[1])
    return result


@public.add
def sensor(name):
    """return sensor value by sensor name"""
    for k, v in sensors().items():
        if name.lower() in k.lower():
            return v
