import pyautogui as pg
import time

time.sleep(0.2)
if pg.locateOnScreen('images/deviceAd.png', grayscale='True', confidence='0.8') is None:
    deviceAdIconLocation= pg.locateOnScreen('images/deviceAdIcon.png', confidence="0.8")
    if deviceAdIconLocation != None:
        pg.moveTo(deviceAdIconLocation.left, deviceAdIconLocation.top, 0.5)
        pg.moveRel(10, 10, 0.3)
        pg.click()
    else:
        quit()
else:
    quit()
print("hi")
time.sleep(1)
pg.moveRel(-200, -500, 0.3)
dal= pg.locateOnScreen('images/deviceAd.png', confidence='0.7')
if dal != None:
    print("found!")
    print(dal.left, dal.top)
    pg.mouseUp()
    pg.click()
    pg.click()
    pg.click()

pg.moveTo(dal.left, dal.top, 0.3)
pg.moveRel(100, 100, 1)