import pyautogui as pg
import time


time.sleep(2)
if pg.locateOnScreen('images/deviceAd.png', grayscale='True', confidence='0.8') is None:
    deviceAdIconLocation= pg.locateOnScreen('images/deviceAdIcon.png', confidence="0.8")
    if deviceAdIconLocation != None:
        pg.moveTo(deviceAdIconLocation.left, deviceAdIconLocation.top, 0.5)
        pg.moveRel(10, 10, 0.3)
        pg.click()

deviceAdLocation= pg.locateOnScreen('images/deviceAd.png', grayscale='True', confidence='0.8')
time.sleep(1)
if deviceAdLocation != None:
    print("found!")
    print(deviceAdLocation.left, deviceAdLocation.top)
    pg.moveTo(deviceAdLocation.left, deviceAdLocation.top, 0.3)
else:
    print("not found!")
print("done")

