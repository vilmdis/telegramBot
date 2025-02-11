from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from dotenv import load_dotenv
import os

load_dotenv()
SPOTIFY = os.getenv('SPOTIFY')
SOUNDCLOUD = os.getenv('SOUNDCLOUD')
POWER_LIGHT = os.getenv('POWER_LIGHT')
POWER_MIDDLE = os.getenv('POWER_MIDDLE')
POWER_HARD = os.getenv('POWER_HARD')

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Anabolic Music')],
    [KeyboardButton(text='Gym'), KeyboardButton(text='Food')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Choose your option...')

music = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Spotify', url=SPOTIFY)],
                                       [InlineKeyboardButton(text='SoundCloud', url=SOUNDCLOUD)]])

gym = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Bodybuilding', url=SPOTIFY), InlineKeyboardButton(text='Powerlifting', url=SOUNDCLOUD)],
                                       [InlineKeyboardButton(text='Guids', callback_data='guids')],
                                       [InlineKeyboardButton(text='Exit', callback_data='exit')]])

guids = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Bench', callback_data='bench'), InlineKeyboardButton(text='Mass', callback_data='mass')],
                                       [InlineKeyboardButton(text='Back', callback_data='back'), InlineKeyboardButton(text='Exit', callback_data='exit')]])

# power = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Light', url=SPOTIFY), InlineKeyboardButton(text='Middle', url=SOUNDCLOUD)],
#                                        [InlineKeyboardButton(text='Hard', callback_data=)]])
