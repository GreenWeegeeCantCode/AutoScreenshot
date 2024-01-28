import pyautogui
import time

running = True

print("Screenshotting will start in 7 seconds, make sure PFA has a midi opened and paused, make sure you have sharex open with the capture entine screen hotkey set to shift alt s, press ctrl + c in terminal to stop if using vscode")
time.sleep(7)
while True:
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.hotkey('shift', 'alt', 's')