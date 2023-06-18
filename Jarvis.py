# import speech_recognition as sr
# import os
# from Body.Speak import Speak
# from googletrans import Translator
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QNA
from Body.Listen import Listen
print(">> Starting...")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting Now!!!")
from Main import MainTaskExe


def MainEXE():
    
    Speak("Hello")
    Speak("I'm Jarvis, I'm Ready.")
    
    while True:
        
        Data = Listen()
        Data = str(Data).replace(".","")
        DataLen = len(Data)
        if DataLen >= 3:
            if "open" in Data or "start" in Data or "launch" in Data or "visit" in Data or ("send" in Data and "whatsapp" in Data):
                ValueReturn = MainTaskExe(Data)
                if ValueReturn == True:
                    pass
            elif "stop" == Data:
                Speak("Bye, have a Good-day")
                break
            elif DataLen >= 3:
                if "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data or "Solve" in Data:
                    Reply = QNA(Data)
                else:            
                    Reply = ReplyBrain(Data)
                Speak(Reply)
        
def ClapDetect():
    query = Tester()
    
    if "True-Mic" in query:
        print("")
        print(">> clap Detected!!")
        print("")
        MainEXE()
        
    else:
        pass
    
ClapDetect()


# def Listen():
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source, 0, 8)

#     try:
#         print("reading...")
#         query = r.recognize_google(audio, language="en")

#     except:
#         return ""

#     query = str(query).lower()
#     print(query)
#     return query

# # Translate Audio

# def TranslationHinToEng(Text):
#     line = str(Text)
#     translate = Translator()
#     result = translate.translate(line)
#     data = result.text
#     print(f"You : {data}.")
#     return data

# # Mic connect

# def MicExecution():
#     query = Listen()
#     data = TranslationHinToEng(query)
#     return data

# #EXE

# def MainExe():
#     print("Out")
#     while True:
#         print("In")
#         query = Listen()
        
#         if "hello" in query:
#             Speak("Hi! I am Jarvis!")
            
#         elif "how are you" in query:
#             Speak("I'm fine!!!")
            
#         elif "bye" in query:
#             Speak("Bye.")
            
#         elif "stop" in query:
#             Speak("Breaking")
#             break
        
#         else:
#             Speak("in-but-out.")
            
            
