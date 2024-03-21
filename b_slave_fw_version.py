"""
Test ID: 
  2
Test Description: |-
  This is to check slave firmware version.
Test Steps: |-
  1. Check slave firmware version.
"""
from itor3_pyapp.master.whoami import *
wai = WAI()
slave = wai.get_version()

report(2, slave)