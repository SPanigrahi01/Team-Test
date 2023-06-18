# Speak Functions - Two Speak Functions

# Windows Based - pip install pyttsx3
# Chrome Based - pip install selenium==4.1.3

# Windows Based

import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"You : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()

#chrome
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep

edge_options = Options()
edge_options.add_argument('--log-level=3')
edge_options.headless = True

Path = "DataBase\msedgedriver.exe"
service = Service(Path)

driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window()
sleep(10)

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):
    lengthoftext = len(str(Text))
    
    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        Data = str(Text)
        xpathofset = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH, value=xpathofset).send_keys(Data)
        driver.find_element(By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
        
        if lengthoftext >= 30:
            sleep(5)
        elif lengthoftext >= 40:
            sleep(7)
        elif lengthoftext >= 55:
            sleep(9)
        elif lengthoftext >= 70:
            sleep(11)
        elif lengthoftext >= 100:
            sleep(14)
        elif lengthoftext >= 120:
            sleep(15)
        else:
            sleep(2)

