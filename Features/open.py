import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()
    
    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
        
    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
        
        
    elif "open" in Query:
        Nameoftheapp = Query.replace("open","")
        pyautogui.press('win')
        sleep(2)
        keyboard.write(Nameoftheapp)
        sleep(2)
        keyboard.press('enter')
        sleep(1)
        return True
    
    elif "start" in Query:
        Nameoftheapp = Query.replace("start","")
        if "edge" in Nameoftheapp:
            os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        return True