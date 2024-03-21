"""
Test ID: 
  5
Test Description: |-
  This is to test roti making.
Test Steps: |-
  1. Run roti making. 
"""

async def rm():
  r = await roti.start_roti_making(2)
  info("Warmup Time(ms)", roti.report['WarmTime'])
  info("Total Time(ms)", roti.report['TotalTime'])

  a = " "
  for i in range (2):
    info("DB:", roti.report['DBWeight'][i])
    info("Flour:", roti.report['FlourWeight'][i])
    info("Water:", roti.report['WaterWeight'][i])
    info("Oil:", roti.report['OilWeight'][i])

    a = "PASSED" + '[nl]' + "Warmup:" + str(roti.report['WarmTime']) + '[nl]' + "Cycle Time:" +  str(roti.report['TotalTime']) + '[nl]' + "DB:" + str(roti.report['DBWeight']) + '[nl]' + "Flour:" + str(roti.report['FlourWeight']) + '[nl]' + "Water:" + str(roti.report['WaterWeight']) + '[nl]' + "Oil:" + str(roti.report['OilWeight'])

  report(5, a)
  
uasyncio.run(rm())

