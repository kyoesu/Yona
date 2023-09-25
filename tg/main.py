from base import *
import logging

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from secr import TOKEN

# Все обработчики должны быть присоединены к Router (или Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик обрабатывает сообщения с командой `/start`
    """
    # У большинства объектов событий есть псевдонимы для вызова методов API,
    # которые могут быть вызваны в контексте событий.
    # Например, если вы хотите ответить на входящее сообщение,
    # вы можете использовать псевдоним `message.answer(...)` и целевой чат будет передан в метод
    # :ref:`aiogram.methods.send_message.SendMessage` автоматически или вызвать метод API непосредственно через
    # экземпляр Bot: `bot.send_message(chat_id=message.chat.id, ...)`
    sql_new_user(message.from_user.id ,hbold(message.from_user.full_name))
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!")

@dp.message(Command('kkkk'))
async def command_handler(message: types.Message):
    # Ваш код для обработки команды
    await message.answer('Вы вызвали команду!')

@dp.message(Command('show'))
async def command_handler(message: types.Message):
    # Ваш код для обработки команды
    res=(" ".join(str(el) for el in sql_show_his(message.from_user.id)))

    await message.answer(res)





@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Обработчик будет пересылать полученное сообщение обратно отправителю

    По умолчанию, обработчик сообщений будет обрабатывать все типы сообщений (текст, фото, стикер и т. д.)
    """
    try:
        # Отправка копии полученного сообщения
        await message.send_copy(chat_id=message.chat.id)
        sql_send_mess(message.from_user.id,message.text,hbold(message.from_user.full_name))
    except TypeError:
        # Но не все типы поддерживаются для копирования, поэтому нужно обработать это
        await message.answer("Хорошая попытка!")


async def main() -> None:
    # Инициализация экземпляра Bot с режимом разбора по умолчанию,
    # который будет передаваться во всех вызовах API
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    
    # И запуск обработки событий
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())