from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_top = KeyboardButton('/Топ-100')
main_movie = KeyboardButton('/Фильмы')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(main_top, main_movie)
movie_menu = ReplyKeyboardMarkup(resize_keyboard=True)

#buttons
page_forward = KeyboardButton('/Forward')
page_back = KeyboardButton('/Back')

movie_menu.row(page_back,page_forward)

url_kb = InlineKeyboardMarkup(row_width=2)
urlbutton = InlineKeyboardButton(text='1')
urlbutton2 = InlineKeyboardButton(text='2')
All_pages = [
    InlineKeyboardButton(text='3'),
    InlineKeyboardButton(text='4'),
    InlineKeyboardButton(text='5'),
    InlineKeyboardButton(text='6'),
    InlineKeyboardButton(text='7'),
    InlineKeyboardButton(text='8'),
    InlineKeyboardButton(text='9'),
    InlineKeyboardButton(text='10')
]
url_kb.add(urlbutton, urlbutton2).row(*All_pages).insert(InlineKeyboardMarkup(text='11'))

