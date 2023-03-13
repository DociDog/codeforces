from aiogram import types, executor
from dispatcher import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from parse import parsers
import aiogram.utils.markdown as md
import random
import logging
import tasks_out

import messages
import inline_keyboard

logging.basicConfig(
    level=logging.INFO,
    filename = "mylog.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

@dp.message_handler(commands=['start', 'tasks'])
async def show_weather(message: types.Message):
    await message.answer(text=messages.start(),
                         reply_markup=inline_keyboard.TASKS)
    
@dp.callback_query_handler(text='tasks')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.choosing_topic(),)
    
@dp.message_handler()
async def complexity(message: types.Message):
    compl = tasks_out.comlexiti(int(message.text))
    if compl == 'Вы написали неверное число с:':
        await message.answer(compl)
    else:
        for i in compl:
            await message.answer(f'Issue number: {i[0]}\nComplexity: {i[1]}\nTitle and themes: {i[2]}\nNumber of solutions: {i[3]}')
