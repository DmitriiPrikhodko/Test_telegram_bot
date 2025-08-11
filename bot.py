import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
import os
import string

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Не найден BOT_TOKEN в переменных окружения!")

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(
    level=logging.INFO,
    filename="./log/bot_log.log",
    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
)


@dp.message(Command(commands=["start"]))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Здравствуйте, {user_name}! \nДля транслитерации введите ваше ФИО на русском языке"
    logging.info(f"{user_name} {user_id} запустил бота")
    await bot.send_message(chat_id=user_id, text=text)


@dp.message()
async def transliteration(message: Message):
    transliter_dict = {
        "А": "A",
        "а": "a",
        "Б": "B",
        "б": "b",
        "В": "V",
        "в": "v",
        "Г": "G",
        "г": "g",
        "Д": "D",
        "д": "d",
        "Е": "E",
        "е": "e",
        "Ё": "E",
        "ё": "e",
        "Ж": "Zh",
        "ж": "zh",
        "З": "Z",
        "з": "z",
        "И": "I",
        "и": "i",
        "Й": "I",
        "й": "i",
        "К": "K",
        "к": "k",
        "Л": "L",
        "л": "l",
        "М": "M",
        "м": "m",
        "Н": "N",
        "н": "n",
        "О": "O",
        "о": "o",
        "П": "P",
        "п": "p",
        "Р": "R",
        "р": "r",
        "С": "S",
        "с": "s",
        "Т": "T",
        "т": "t",
        "У": "U",
        "у": "u",
        "Ф": "F",
        "ф": "f",
        "Х": "Kh",
        "х": "kh",
        "Ц": "Ts",
        "ц": "ts",
        "Ч": "Ch",
        "ч": "ch",
        "Ш": "Sh",
        "ш": "sh",
        "Щ": "Shch",
        "щ": "shch",
        "Ы": "Y",
        "ы": "y",
        "Ъ": "Ie",
        "ъ": "ie",
        "Э": "E",
        "э": "e",
        "Ю": "Iu",
        "ю": "iu",
        "Я": "Ia",
        "я": "ia",
        "ь": "",
        "Ь": "",
    }
    rus_letters = (
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    )
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    print(text)
    text_translit = ""
    flag = True
    for c in text:
        if c in string.punctuation or c == " ":
            text_translit += c
        elif c in rus_letters:
            text_translit += transliter_dict[c]
        else:
            await message.answer(
                "Ошибка: ФИО должно состоять только из букв русского алфавита"
            )
            flag = False
            break
    if flag:
        await message.answer(f"Ваше ФИО в латинской транслитерации: {text_translit}")

    logging.info(f"{user_name} {user_id} переводит: {text}")


if __name__ == "__main__":
    dp.run_polling(bot)
