from aiogram import Bot, Dispatcher
from configparser import ConfigParser
from aiogram.fsm.storage.memory import MemoryStorage

config = ConfigParser()
config.read("settings.ini")

admins = [int(admin_id) for admin_id in config['Tg']['ADMINS'].split(',')]

bot = Bot(token=config['Tg']['TOKEN'])
dp = Dispatcher(storage=MemoryStorage())

