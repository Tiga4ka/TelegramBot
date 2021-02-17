import telebot # импорт бибилиотеки телебот
import config # импорт конфиг файла с токеном
import random # импорт рандом

from telebot import types # импортирует объекты чтоли

# Переменной присываеваем запуск бота с использованием токена
bot = telebot.TeleBot(config.TOKEN)

# Выполнить при команде /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # Открываем и отправляем стикер
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard тестируем, выдает рандомное число
    # Переменной присваеваем объект Ответная Клавиатура и меняем размер кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем кнопки, присваиваем их переменной
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")
    # Прибавляем к переменной объекты
    markup.add(item1, item2)


    # Отправляем сообщение
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}! \nЯ - <b>{1.first_name}</b>, бот от которого вы охренеете!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)




@bot.message_handler(content_types=['text'])
def lalala(message):
    # Если сообщение в чате равно == личное сообщение
    if message.chat.type == 'private':
        # если текст вот такой,
        if message.text == 'Рандомное число':
            # отправь в сообщении рандомное число из функции random
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Как дела?':
            # Инлайновая клавиатура.
            # Создаем инлайн клавиатуру. Сколько столбцов для вариантов ответа
            markup = types.InlineKeyboardMarkup(row_width=1)
            # Создаем кнопки
            # callback_data присваевает ответу переменную
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            markup.add(item1, item2)

            # Здесь пишем сообщение и сразу форму для ответа, присваиваем инлайн клаву
            bot.send_message(message.chat.id, 'Отлично, как сам?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')


# Пишем реакцию на ответ инлайновой клавиатуры. Не понятные какието функции
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            # если ответное сообщение  'good'
            if call.data == 'good':
                bot.send_message(call.message.chat.id, "Вот и отличненько!😄")
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, "Бывает .. 😳")

            # удаляем кнопки после сообщения
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как дела?", reply_markup=None)
            # показать уведомление
            #bot.answer_callback_query(chat_id=call.message.chat.id, show_alert= False, text="Пхахаха это что еще за хрень!!")

    except Exception as e:
        print(repr("Ошибка"))

# RUN
bot.polling(none_stop=True)


# Повторяет сообщения:
# def lalala(message):
    # bot.send_message(message.chat.id, message.text)


# МОИ ВОПРОСЫ
# 1. Как отправляется сообщение, кто придумал команду message.chat.id
# 2. Не высвечивает уведомление
#
