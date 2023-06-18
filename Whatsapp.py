from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os
from time import sleep
import pandas as pd
from Body.Speak import Speak
import pathlib
from Body.Listen import Listen

# scriptDirectory = pathlib.Path().absolute()

# os.system("")
# os.environ["WDM_LOG_LEVEL"] = "0"
# PathofDriver = "DataBase/msedgedriver.exe"

# service = Service(PathofDriver)
# driver = webdriver.Edge(service=service)
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
# sleep(5)
# Speak("Initializing The Whatsapp Software.")

ListWeb = {'Name': "+Number"}

# def WhatsappSender(Name):
#     Speak(f"Preparing To Send a Message To {Name}")
#     Speak("What's The Message By The Way?")
#     Message = Listen()
#     Number = ListWeb[Name]
#     Link = f'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
#     #LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
#     #driver.get(LinkWeb)
#     sleep(5)
#     try:
#         driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
#         Speak("Message Sent")
        
#     except:
#         print("Invalid Number")

import time
import pyautogui

def WhatsappSender(Name):
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = Listen()
    Number = ListWeb[Name]
    Speak(f"{Number}")

    # Open WhatsApp
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write(r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2322.2.0_x64__cv1g1gvanyjgm\WhatsApp.exe")
    pyautogui.press("enter")
    time.sleep(20)  # Increase the delay if needed

    # Activate WhatsApp window
    whatsapp_window = pyautogui.getWindowsWithTitle("WhatsApp")[0]
    whatsapp_window.activate()

    # Wait for the chats list to load
    time.sleep(3)

    # Search for contact
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)
    pyautogui.write(Number)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("Tab")
    pyautogui.press("enter")
    time.sleep(2)  # Add a delay to allow the chat to open

    # Type the message
    pyautogui.write(Message)

    # Confirmation step
    Speak("Are you sure you want to send this message?")
    Speak("Please say 'yes' or 'no'")
    response = Listen().lower()
    if response == "yes":
        # Send the message
        pyautogui.press("enter")
        Speak("Message Sent")
        time.sleep(2)
    else:
        # Cancel sending the message
        pyautogui.hotkey("ctrl", "a")  # Select the typed message
        pyautogui.press("backspace")  # Delete the message
        Speak("Message sending canceled")
        
    time.sleep(2)


    
    
