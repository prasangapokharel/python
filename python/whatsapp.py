import pyautogui as pg
import time
print("Starting in 1 second")
time.sleep(5)

for i in range(5):
    pg.write("I am abijeet")
    pg.press("Enter")