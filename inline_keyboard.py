from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_TASKS = InlineKeyboardButton('New Tasks', callback_data='tasks')


TASKS = InlineKeyboardMarkup().add(BTN_TASKS)