from selenium import webdriver
import time

# Path to the WebDriver executable (Update it according to your setup)
# Using a raw string to prevent escape character issues
driver_path = r"C:\Users\godsu\Desktop\Python\chromedriver.exe"

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome(executable_path=driver_path)

    # Navigate to YouTube
    driver.get("https://www.youtube.com/")

    # Optional: Close the browser window after some time (here, 5 seconds)
    time.sleep(5)
    driver.quit()

except Exception as e:
    print(f"An error occurred: {e}")
