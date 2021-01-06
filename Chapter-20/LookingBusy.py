import pyautogui, time

def moveMouse():
    while True:
        try:
            pyautogui.moveRel(3, 0, 0.5)
            time.sleep(10)
        except KeyboardInterrupt:
            print('Program Ended!')

print('--->Program Start: Now the mouse will move every 10 seconds.')
moveMouse()