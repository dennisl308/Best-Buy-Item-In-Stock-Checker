# Best Buy Item Stock Checker
# Created by Dennis Luong

# Description:
#   This program will check if a given item by URL is in stock.
#   When a item is in stock, a window will pop up and two beeps will be played.
#   The user can set how often the program will perform its stock checking.

# Imported libraries
from bs4 import BeautifulSoup   # for HTML parsing
from datetime import datetime   # for getting current time
import requests # for HTML scraping
import pyautogui # for pop-up window
import winsound # for beep sounds
import time # for setting how frequent checks are made

# Sound properties
duration = 100  # milliseconds
frequency = 500 # Hz

# gives permission to access HTML contents
agent = {
    'User-Agent': 'Jimmy'  # put your name here
}

# -------------------------------------------------------------------

print('What is the name of your product?')
product_Name = input()

print("What is this product's URL? (Note, Make sure the URL is correct)")
URL = input()

# storing and error checking user input for time
loop_Flag = True
while loop_Flag:
    print("How frequently, in seconds, do you want the program to check for your item? Put '0' to check as often as possible.")
    delay = input()

    if delay.isdigit():
        loop_Flag = False   # stop while loop
        delay = int(delay)  # convert string to int
    else:
        print("Sorry, that is not a number. Try again.")

print("Checking will now begin...")

# keep checking/looping until item is in stock
loop_Flag = True
while loop_Flag:
    page = requests.get(URL, headers=agent) # get HTML contents
    soup = BeautifulSoup(page.content, 'html.parser')   # parse HTML contents
    stock_Status = str(soup.find('div', class_='fulfillment-add-to-cart-button')) # look for div that contains the item's stock status

    # item is in stock, "Add to Cart" was found, returning -1 means the string could not be found
    if (stock_Status.find('Add to Cart') != -1):
        loop_Flag = False       # stop while loop
        date = datetime.now()   # datetime object
        formatted_Date = date.strftime('%d/%m/%Y %H:%M:%S') # format date

        # beep two times
        for i in range(0, 2):
            winsound.Beep(frequency, duration)
        
        # pop-up message
        pyautogui.alert(text=product_Name + "\nYour item is in stock." + "\nTime when detected: " + formatted_Date, title="In-Stock Checker Notification", button="OK")

    time.sleep(delay)   # suspend execution for a given amount of time

print("Check has ended. This program will now exit.")