##right click when the mouse starts spinning
import pyautogui
import math
import time

time.sleep(1)


# Radius
R = 200
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen
(X,Y) = pyautogui.position(x/2,y/2)
# offsetting by radius
pyautogui.moveTo(X+R,Y)

for i in range(500):
    # setting pace with a modulus
    if i%12==0:
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))