import telebot
import random
from telebot import types
from settings import TOKEN


f = open('jokes.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Дзен")
        markup.add(item1)
        item2 = types.KeyboardButton("Шутка")
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nШутка для получения шутки\n '
                                    'Дзен для получения одного из постулатов Python', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.strip() == "Шутка":
        answer = random.choice(jokes)
    elif message.text.strip() == "Дзен":
        answer = random.choice(facts)
    bot.send_message(message.from_user.id, answer)


bot.polling(none_stop=True, interval=0)
