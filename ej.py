import keyboard
import time

key = False
while True:
    if keyboard.is_pressed('space') and not key:
        key = True
        print("Holi :D")
    elif not keyboard.is_pressed('space'):
        key = False
    time.sleep(0.5)
    print(key)