from aiogram import Bot, Dispatcher, executor, types

# Инициализация бота с токеном, полученным от BotFather.
# Замените 'YOUR_BOT_TOKEN_HERE' на токен вашего бота.
bot = Bot('YOUR_BOT_TOKEN_HERE')

# Создание экземпляра диспетчера для обработки входящих сообщений.
dp = Dispatcher(bot)


# Обработчик сообщений.
# Этот декоратор указывает, что функция response_to_the_user будет
# вызываться при получении любого текстового сообщения пользователем.
@dp.message_handler()
async def response_to_the_user(message: types.Message):
    # Отправка приветственного сообщения пользователю.
    await message.reply('ПРИВЕТ! ВЫБИРАЙ ВО ЧТО БУДЕМ ИГРАТЬ!')

    # Создание инлайн-клавиатуры для выбора игры.
    markup = types.InlineKeyboardMarkup()

    # Добавление кнопок для каждой игры с соответствующими URL-ссылками.
    markup.add(types.InlineKeyboardButton('МИЛЛИОНЕР', url='https://ru.wwbm.com/index.php?sch=Map'))
    markup.add(types.InlineKeyboardButton('КОСЫНКА', url='https://xn--80a0aejb8dva.com/'))
    markup.add(types.InlineKeyboardButton('МАНДЖОНГ', url='https://pasyans.ru/majong'))
    markup.add(types.InlineKeyboardButton('САПЁР', url='https://xn--80a4adb6f.com/'))
    markup.add(types.InlineKeyboardButton('ДУРАК', url='https://durak.hlop.de/ru/'))

    # Ответ сообщением со списком игр и добавленной клавиатурой.
    await message.answer('СПИСОК ИГР:', reply_markup=markup)

# Запуск бота. Метод start_polling начинает прослушивание обновлений
# от Telegram API, позволяя боту реагировать на входящие сообщения.
executor.start_polling(dp)





