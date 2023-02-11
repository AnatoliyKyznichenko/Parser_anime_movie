from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup
import requests
import keyboard
from key import my_key
from keyboard import url_kb
import time

bot = Bot(my_key)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(f'''Привет {message.from_user.full_name} я бот для поиска лучших аниме
      <b><a href='https://yummyanime.tv/'>Anime</a></b>:)''',
      parse_mode='html', disable_web_page_preview=0, reply_markup=keyboard.main_menu)


@dp.message_handler(commands=['Топ-100'])
async def anime_parser(message: types.message):
    url = 'https://yummyanime.tv/1top-100/'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.find_all('div', class_='movie-item')
    image = 'https://yummyanime.tv/'
    for item in title:
        name = item.find_all('div', class_='movie-item__title')[0]
        name = name['title']
        rating = item.find_all('div', class_='movie-item__rating')[0].text
        link = item.select('.movie-item__inner > a')[0]
        link = 'https://yummyanime.tv/1top-100' + link['href']
        year = item.select('.movie-item__meta > span')[0].text
        img = item.find('div', class_='movie-item__img').find_all('img')
        for i in img:
            img = image + i['src']

        time.sleep(0.3)
        await bot.send_photo(message.chat.id, img,
        caption="<b>" + name + "</b>\n<i>" + year + rating + f"</i>\n<a href='{link}'>Ссылка на сайт</a>",
        parse_mode='html')


@dp.message_handler(commands=['Фильмы'])
async def anime_parser(message: types.message):
    url = 'https://yummyanime.tv/movies/'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    image = 'https://yummyanime.tv/'
    page_count = int(soup.find('div', class_='pagination__inner').find_all('a')[-1].text.strip())
    for i in range(1, page_count + 1):
        print(f'[INFO] Обработка {i} страницы')
        url = f'https://yummyanime.tv/movies/page/{i}/'
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        title = soup.find_all('div', class_='movie-item')
        for item in title:
            try:
                name = item.find_all('div', class_='movie-item__title')[0]
                name = name['title']
                rating = item.find_all('div', class_='movie-item__rating')[0].text
                link = item.select('.movie-item__inner > a')[0]
                link = 'https://yummyanime.tv/1top-100' + link['href']
                year = item.select('.movie-item__meta > span')[0].text
                img = item.find('div', class_='movie-item__img').find_all('img')
                for i in img:
                    img = image + i['src']

                time.sleep(0.3)
                await bot.send_photo(message.chat.id, img,
                caption="<b>" + name + "</b>\n<i>" + year + rating + f"</i>\n<a href='{link}'>Ссылка на сайт</a>",
                parse_mode='html')
            except:
                ValueError


if __name__ == '__main__':
    executor.start_polling(dp)


#print(name)
#print(f'Рейтинг -{rating}')
#print(year)
#print(f'Ссылка {link}')
#print(f'Фото {img}')