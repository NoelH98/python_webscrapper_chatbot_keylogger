from chatterbot import chatterbot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_listener(ListTrainer)

for files in os.listdir('C:/Users/'):
    data = open('C:/Users/' + files , 'r').readLines()
    bot.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
    reply = bot.get_response(message)
    print('ChatBot:', reply)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break

