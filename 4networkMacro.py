import pyautogui as pg
import os
import time
import pyperclip
import random

if "deviceMa.png":
    print("there is deviceMa.png")
if "deviceMaIcon.png":
    print("there is deviceMaIcon.png")
locateDeviceMa= pg.locateOnScreen("images/deviceMa.png", confidence='0.8')
if locateDeviceMa is None:
    locateDeviceMaIcon= pg.locateOnScreen("images/deviceMaIcon.png", region=(720, 1000, 580, 79), confidence='0.8')
    if locateDeviceMaIcon is None:
        print("locateDeviceMaIcon not found")
    else:
        pg.moveTo(locateDeviceMaIcon.left + 10, locateDeviceMaIcon.top + 10, .3)
        pg.click()
    time.sleep(1)
    locateDeviceMa= pg.locateOnScreen("images/deviceMa.png", confidence='0.8')
    
if locateDeviceMa is not None:
    print("locateDeviceMa found: ", locateDeviceMa)
else:
    print("locateDeviceMa not found: quit program")
    quit()

pg.moveTo(locateDeviceMa.left + 157, locateDeviceMa.top + 303, .3)
print("finished")
pg.doubleClick()
time.sleep(1)
pg.moveRel(126, 53)
pg.doubleClick()

time.sleep(1)
locateAttributes= pg.locateOnScreen("images/attributes.png", confidence="0.9")
if locateAttributes == None:
    print("locateAttributes not found!")
    quit()
pg.moveTo(locateAttributes.left + 116, locateAttributes.top + 76, .2)
pg.click()
time.sleep(1)
pg.moveRel(-2, 308, .2)
pg.click()
time.sleep(1)
pg.moveRel(328, -118, .2)
pg.doubleClick()
time.sleep(1)
pg.press("backspace")

ranarr=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
ranstr= ''
i=12
while i>0:
    ran= random.choice(ranarr)
    print(ran)
    ranstr+= ran
    print(ranstr)
    i-=1
i=12
pyperclip.copy(ranstr)
pg.hotkey('ctrl', 'v')

pg.moveRel(32, 523, .2)
pg.click()

time.sleep(5)
locateDeviceMa= pg.locateOnScreen("images/deviceMa.png", confidence='0.8')
pg.moveTo(locateDeviceMa.left + 157, locateDeviceMa.top + 303, .3)
pg.doubleClick()

print("finished")


"""
 이 모든걸 userfunc 안에 집어넣어서 시간마다 무한 루프 돌린다.
 그리고 각 에러가 뜰때마다 해당되는 창을 닫고 quit()하는 걸 추가.

"""