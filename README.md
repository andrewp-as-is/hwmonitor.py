<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/hwmonitor.svg?maxAge=3600)](https://pypi.org/project/hwmonitor/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/hwmonitor.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/hwmonitor.py/actions)

### Installation
```bash
$ [sudo] pip install hwmonitor
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
