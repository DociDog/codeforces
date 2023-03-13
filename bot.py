from aiogram import executor
from dispatcher import dp
import handlers
import threading
import parse
import os 



from db import BotDB
bot = BotDB()

if __name__ == "__main__":
    #parse.parsers()
    executor.start_polling(dp, skip_updates=True)
    #os.system('parse.py')
   