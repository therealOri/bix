#CTRL + C will stop this from running.

import pynput
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
text = input('Text?: ')
time.sleep(5) #This is how long it waits before starting/running the code below.

while True:
    
    keyboard.type(text)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)
    print('Server Has been bumped!')
    time.sleep(7260) #7260 is 2hrs and 1 min in seconds. It's set up like this because disboard sometimes throws a fit if you are exactly on time.
