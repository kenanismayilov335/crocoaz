import logging
import os
from aiogram import Bot, Dispatcher
from game import Game


bot = Bot(token=os.getenv('1510723916:AAFO8ShkUfsM0wEOb4Xsco47bLybZh3LeDo'))
dp = Dispatcher(bot)
g = Game('crocobot.db')
logging.basicConfig(level=logging.INFO)
