from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

time.sleep(3)  # wait 3 seconds and then simulate 'a'
keyboard.press('a')
keyboard.release('a')

# To simulate pressing 'shift + a' (which will result in 'A')
keyboard.press(Key.shift)
keyboard.press('a')
keyboard.release('a')
keyboard.release(Key.shift)
