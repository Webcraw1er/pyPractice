import pyautogui as pg
import time
import os

pg.FAIL_SAFE = True
pg.PAUSE = 0.2

for win in pg.getAllWindows():
    print(win)

os.system('taskmgr')
screenWidth, screenHeight = pg.size()
pg.moveTo(screenWidth/2, screenHeight/2)
pg.moveRel(10, 10, 1)


