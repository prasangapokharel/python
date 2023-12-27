import pyautogui as pg 
import time

time= int(input("Enter a starting second: "))

print("Starting in 5sec")
time.sleep(5)
#range is known as no.of times here
for i in range(10):
    pg.write("You are hacked")
    pg.press("Enter")