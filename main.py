from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from os import system, name
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
    userInput= input("-> ").lower()

    if userInput == "cls":
      cls()

    elif userInput == "exit":
      quit()

    elif userInput == "train":
      train()

    else:
      print("-> ", end="")
      print(chatbot.get_response(userInput))
      print()


except KeyboardInterrupt:
  print()
  print(" "+"\n Quitting ChatBot...")
  time.sleep(1)
  print(" "+"ChatBot Terminated")
  print()
  quit()
