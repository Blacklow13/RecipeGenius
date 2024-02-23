import telebot
from telebot import types

bot = telebot.TeleBot('7043394890:AAHfDBDYkDI08kE7eeqfKtHl_ij17YiIUUU')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Загрузить картинку")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Этот бот поможет вам узнать название блюда на фотографии и предложит рецепт для его приготовления. Просто загрузите фото, и получите информацию о блюде!", reply_markup=markup)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть