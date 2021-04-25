#CTRL + C will stop this from running.

import pynput
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
time.sleep(5)

while True:
    
    keyboard.type('!d bump')
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)
    print('Server Has been bumped!')
    time.sleep(7260)
