import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor



logging.basicConfig(level=logging.INFO)

bot = Bot(token="5728932780:AAFQ-Hz0QAQHIV7j7s8hiH0n6Fj9adfKfhQ")
dp = Dispatcher(bot, storage=MemoryStorage())


