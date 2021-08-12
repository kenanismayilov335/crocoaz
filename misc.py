import logging
import os
from aiogram import Bot, Dispatcher
from game import Game


bot = Bot(token=os.getenv('1902704837:AAGmqn9lAZlVEa0OT-0dod9pnoMoPzWkwhw'))
dp = Dispatcher(bot)
g = Game('crocobot.db')
logging.basicConfig(level=logging.INFO)
