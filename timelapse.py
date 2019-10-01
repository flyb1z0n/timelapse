#!/usr/bin/python

import time 
import os 
import datetime

while True: 
    day = datetime.datetime.now().strftime("%Y-%m-%d");
    directory = '/home/pi/timelapse/img/' + day +'/';
    if not os.path.exists(directory):
        os.makedirs(directory)

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S");
    os.system('fswebcam -r 1920x1080 -S 20 --no-banner --save ' + directory + now + '.png') 
    time.sleep(10) 
