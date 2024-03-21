"""
Test ID: 
  4
Test Description: |-
  This is to test stirrer and cup alignment. 
  Load cell feedback is read. 
Test Steps: |-
  1. Move VT to flour dispense position
  2. Run KN 
  3. Check load cell reading feedback
"""
async def runtest():
  vt.move(0, 21, 10)
  await vt.wait()
  timeout = 10
  pos = 0
  await uasyncio.sleep(2)
  kn.run(20)

  max_weight = 0
  tol = 2
  for _ in range(30): 
    w = ds.get_status(0).weight
    if max_weight < w:
      max_weight = w
    info(w)
    await uasyncio.sleep(0.5)

  info(max_weight)
  kn.stop()

  if max_weight > (max_weight + tol):
    report(4, 'FAILED')
    must_stop()
  else:
    report(4, 'PASSED')

uasyncio.run(runtest())

