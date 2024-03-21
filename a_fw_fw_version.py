"""
Test ID: 
  1
Test Description: |-
  This is to check master firmware version.
Test Steps: |-
  1. Check master firmware version.
"""
from itor3_pyapp import get_master_version
master = get_master_version()

report(1, master)