from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

bot_weather = Bot("6070487998:AAG__Wb_falnU1Hon1LKzu01Hx_TIE8j-oU")
dp = Dispatcher(bot_weather)

async def on_start(_):
    print('Бот запущен')

@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
   kb = [
       [
           types.KeyboardButton(text="Синий"),
           types.KeyboardButton(text="Желтый"),
           types.KeyboardButton(text="Красный"),
           types.KeyboardButton(text="Розовый"),
           types.KeyboardButton(text="Белый"),
           types.KeyboardButton(text="Фиолетовый")
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.reply("Привет!\nЯ Помогу выбрать тебе цветы по цвету!\nВыбери цвет и я пришлю тебе список цветов!", reply_markup=keyboard)

@dp.message_handler()
async def com_start(message: Message):
    if message.text == 'Синий':
        await message.reply(f'Василек\n Дельфиниум\n Ирис\n Аконит\n Барвинок\n Аюга\n Вероника\n Гиацинт\n')
    if message.text == 'Желтый':
        await message.reply(f'Форзиция\n Керрия\n Магония\n Нарциссы\n Примула\n Адонис\n Крокус\n Тюльпаны\n')
    if message.text == 'Красный':
        await message.reply(f'Примула\n Целозия\n Бегония\n Мак\n Годеция\n Корейская хризантема\n Флокс\n Космея\n')
    if message.text == 'Розовый':
        await message.reply(f'Агростемма\n Гладиолус\n Аквилегия\n Дицентра\n Анемона\n Армерия\n Пион\n Канна\n')
    if message.text == 'Белый':
        await message.reply(f'Астильба\n Иберис\n Гортензия\n Хризантема\n Ландыш\n Гипсофила\n Ромашка\n Георгина\n')
    if message.text == 'Фиолетовый':
        await message.reply(f'Рододендрон\n Сирень\n Скумпия\n Астра\n Фиалка\n Буддлея\n Лилия\n Лаванда\n')
executor.start_polling(dp, skip_updates = True, on_startup = on_start)