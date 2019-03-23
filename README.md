<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/hwmonitor.svg?longCache=True)](https://pypi.org/project/hwmonitor/)
[![](https://img.shields.io/pypi/v/hwmonitor.svg?maxAge=3600)](https://pypi.org/project/hwmonitor/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/hwmonitor.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/hwmonitor.py/)

#### Installation
```bash
$ [sudo] pip install hwmonitor
```

#### Functions
function|`__doc__`
-|-
`hwmonitor.read()` |return string with `hwmonitor` output
`hwmonitor.sensor(name)` |return sensor value by sensor name
`hwmonitor.sensors()` |return dict with sensor names as keys and temperature as values

#### Examples
```python
>>> import hwmonitor
>>> hwmonitor.read()
SMART Disk XXX (ZZZ): 55 C
...

>>> hwmonitor.sensors()
{'SMART Disk XXX (ZZZ)': 55, ...}

>>> hwmonitor.sensor("air")
25
```

#### Links
[Hardware Monitor.app](https://www.bresink.com/osx/HardwareMonitor.html)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>