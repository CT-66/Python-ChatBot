from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from os import system, name
import colorama
from colorama import Fore, Style
import time
import sys
    
def cls(): 
  system('clear')

def quit():
  sys.exit()

chatbot= ChatBot("ChatBot")

def train():
  trainer= ChatterBotCorpusTrainer(chatbot)
  trainer.train('chatterbot.corpus.english')

try:

  while True:
    userInput= input(Fore.YELLOW+Style.BRIGHT+"▶ "+Fore.YELLOW+Style.BRIGHT).lower()

    if "cls" in userInput:
      cls()

    elif "exit" in userInput:
      quit()

    else:
      print(Fore.BLUE+Style.BRIGHT+"▶ "+Fore.BLUE+Style.BRIGHT, end="")
      print(chatbot.get_response(userInput))
      print()


except KeyboardInterrupt:
  print()
  print(Fore.RED+" "+"\n Quitting ChatBot...")
  time.sleep(1)
  print(Fore.RED+" "+"ChatBot Terminated")
  print()
  quit()
