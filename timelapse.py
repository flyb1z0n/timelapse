#!/usr/bin/python

import time 
import os 

while True: 
    os.system('fswebcam -r 1920x1080 -S 20 --no-banner --save /home/pi/%H%M%S.png') 
    time.sleep(10) #
