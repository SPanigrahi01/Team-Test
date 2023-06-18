#OpenAI
fileopen = open(r"C:\Users\panig\OneDrive\Desktop\AI\Data\api.txt", "r")
API = fileopen.read()
fileopen.close()
print(API)

import openai
from dotenv import load_dotenv

#code

openai.api_key = API

load_dotenv()
completion = openai.Completion()


def QNA(question,chat_log = None):
       
    
    Filelog = open("DataBase\qna_log.txt","r")
    chat_log_template = Filelog.read()
    Filelog.close()
    
    if chat_log is None:
        chat_log = chat_log_template
        
    prompt = f'{chat_log}Q : {question}\nA : '
    response = completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature =0,
        max_tokens =100,
        top_p =1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQ : {question} \nA : {answer}"
    Filelog = open("DataBase\qna_log.txt","w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    return answer



