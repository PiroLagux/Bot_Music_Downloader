from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, я буду скачивать музыку за тебя!')

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Ты нашёл пасхалку :3')

@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
    await message.answer('Ну это уже ОМЕГАПАСХАЛКА')
