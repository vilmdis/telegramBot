from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart, Command
import asyncio
from aiogram.enums import ChatAction
from dotenv import load_dotenv
import os
import keyboards as kb

router = Router()
load_dotenv()
START_TEXT = os.getenv('START_TEXT')
HELP_TEXT = os.getenv('HELP_TEXT')
BENCH = os.getenv('BENCH')
MASS = os.getenv('MASS')


@router.message(CommandStart())
async def start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await asyncio.sleep(1)
    await message.answer(text=START_TEXT,
                         reply_markup=kb.main)

@router.message(Command('help'))
async def help(message: Message):
    await message.answer(f'Here is the instruction:\n{HELP_TEXT}')

@router.message(F.text == "Anabolic Music")
async def music(message: Message):
    await message.answer(text="Here is the music:",
                         reply_markup=kb.music)

@router.message(F.text == "Gym")
async def gym_programs(message: Message):
    await message.answer(text="Choose the program:",
                         reply_markup=kb.gym)

@router.callback_query(F.data == "guids")
async def guids(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text='Here are some guids and tips for you:',
                                  reply_markup=kb.guids)

@router.callback_query(F.data == "bench")
async def bench_tips(callback: CallbackQuery):
    doc = FSInputFile(BENCH)
    await callback.message.delete()
    await callback.answer('Bench Press')
    await callback.bot.send_document(chat_id=callback.message.chat.id, document=doc, caption='Here are bench press tips:')

@router.callback_query(F.data == "mass")
async def mass_guids(callback: CallbackQuery):
    doc = FSInputFile(MASS)
    await callback.message.delete()
    await callback.answer('Mass')
    await callback.bot.send_document(chat_id=callback.message.chat.id, document=doc, caption='Here are mass guids:')

@router.callback_query(F.data == "back")
async def back_button(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Choose the program:", reply_markup=kb.gym)
    await callback.answer('')

@router.callback_query(F.data == "exit")
async def exit_button(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer('')
