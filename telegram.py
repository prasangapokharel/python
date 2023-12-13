import pyautogui as pg
import time

print("Starting in 5 seconds")
time.sleep(5)

for i in range(10):
    user_message = input("Enter your message: ")

    if user_message.lower() == "hi":
        response = "Hello"
    else:
        response = "I love you"

    pg.write(response)
    pg.press("Enter")
