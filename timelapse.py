#!/usr/bin/python

import time 
import os 
import datetime

while True: 
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    os.system('fswebcam -r 1920x1080 -S 20 --no-banner --save /home/pi/timelapse/img/' + now + '.png') 
    time.sleep(10) #
