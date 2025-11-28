from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from download_music import download_music
from aiogram.types import FSInputFile

get_message_router = Router()

@get_message_router.message(F.text)
async def get_name(message: Message):
    name_of_music = message.text
    download_music(name_of_music, message.chat.id)
    audio = FSInputFile(f"{message.chat.id}.mp3", f"{name_of_music}")
    await message.reply_audio(audio=audio)
