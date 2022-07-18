import pyautogui as pg
import time

pg.PAUSE = 1
pg.FAILSAFE = True


deviceMa = pg.locateOnScreen("images/deviceMa.png", confidence='0.8')
if deviceMa is not None:
    print("deviceMa found!", deviceMa.left, deviceMa.top)
pg.moveTo(deviceMa.left + 150, deviceMa.top + 300, 1)
pg.click()
pg.doubleClick()
pg.doubleClick()
#pg.moveRel(50, 0, 0.2)
