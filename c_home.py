"""
Test ID:
  3
Test Description: |-
  This is to test automatic calibration of assemblies. 
Test Steps: |-
  1. Calibrate VT, KR, and Press.
  2. Check VT, KR, and Press after calibration.
  

"""
calib = uasyncio.run(calibrate_vt_kr())

if calib == True:
  vt_pos = vt.get_status()
  time.sleep(0.05)
  info('VT Position:', vt_pos.pos)
  wp_pos = wp.get_status()
  time.sleep(0.05)
  info('WP Position:', wp_pos.press_gap)
  kr_pos = kr.get_status()
  info('KR Position:', kr_pos.pos) 
  time.sleep(0.05) 
  #rep = "PASSED" + ',' + " VT Position " + str(vt_pos.pos) + ',' + " WP Position " + str(wp_pos.press_gap) + ',' + " KR Position " + str(kr_pos.pos)
  rep = "PASSED" + '[nl]' + "VT Position:" + str(vt_pos.pos) + '[nl]' + "KR Position:" + str(kr_pos.pos) + '[nl]' + "WP Position:" + str(wp_pos.press_gap)
  report(3, rep)
else:
  report(3, "FAILED")
  must_stop()


