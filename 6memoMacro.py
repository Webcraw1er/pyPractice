import os
import time
import pyautogui as pg

if print("yes"):
    print("yes2")
if pg.getWindowsWithTitle('제목 없음') == []:     # title이 '제목없음'인 창들 정보
    locateMemoIcon= pg.locateOnScreen("images/memoIcon.png", confidence='0.8')
    if locateMemoIcon== None:
        print("locatemomooiicon doesnt exist.")
    pg.moveTo(locateMemoIcon.left +5, locateMemoIcon.top + 5, 0.3)
    pg.click() 
time.sleep(1)
memoWin= pg.getWindowsWithTitle('제목 없음')[0]

if memoWin.isMinimized == True:
    locateMemoIcon= pg.locateOnScreen("images/memoIcon.png", confidence='0.8')
    if locateMemoIcon== None:
        print("locatemomooiicon doesnt exist.")
    pg.moveTo(locateMemoIcon.left +5, locateMemoIcon.top + 5, 0.3)
    pg.click() 

time.sleep(0.3)

if memoWin.isActive == False:
    print("activated")
    memoWin.activate()

time.sleep(1)
exitIcon= pg.locateOnScreen("images/exitIcon.png", confidence= '0.8')
pg.moveTo(exitIcon.left+5, exitIcon.top+5, 0.3)
pg.click()



"""
기능:

memoWin: finds a window of which its name is "제목 없음".
if there's none, open it.

if its minimized, click on the icon. 최소화: 최대화 하고 최소화 하든지, 그냥 아이콘 클릭해서 불러내야 한다. 
if its unactivated, activate it.    비활성화: 메모장 바깥을 클릭해서 가려졌을 떄를 칭함.


그리고 메모장을 킨 후에 다시 닫는다



"""
