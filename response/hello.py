import pyttsx3
from response.response import *

tts_engine = pyttsx3.init()


def hello_response():
    tts_engine.say("Привет")

pharse_list.append(Type_pharse([
    'привет','добрый день','здраствуйте'
],hello_response))



def how_you_response():
    tts_engine.say("все отлично")

pharse_list.append(Type_pharse([
    'как ты','как дела','как настроение'
],how_you_response))

