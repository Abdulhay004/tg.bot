import asyncio
import logging

from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode

import config

dp = Dispatcher()


@dp.message(CommandStart()) #Start
async def handle_start(message: types.Message):
     await message.answer(
         text=f'Hello, {markdown.hbold(message.from_user.full_name)}',
         parse_mode=ParseMode.HTML,
     )

@dp.message(Command('help')) #Help
async def handle_help(message: types.Message):
    text = 'I\'m and echo bot.\nSend me any message!'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=len('I\'m and echo bot.\nSend me'),
        length=3,
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message() #Any messages
async def echo_message(message: types.Message):
    await message.answer(
        text='Wait a second...'
    )

    try:
        await message.send_copy(chat_id=message.chat.id) #Copy and send any message
    except TypeError:
        await message.reply(text='Something new!')

#Start bot
async def main():
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
