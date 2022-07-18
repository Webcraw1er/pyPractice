import pyautogui as pg
import time
pg.Pause=0.2
pg.FAIL_SAFE = True

time.sleep(1)
pg.moveTo(267, 1050, 0.3)
pg.click()
time.sleep(1)
pg.moveTo(265, 551, 0.3)
pg.click()
time.sleep(2)
locateDeviceMa= pg.locateOnScreen("images/deviceMa.png", confidence='0.8')    
print("locateDeviceMa found: ", locateDeviceMa)
time.sleep(1)
pg.moveTo(locateDeviceMa.left, locateDeviceMa.top, 1)
print("why tha faq is it not working/")
