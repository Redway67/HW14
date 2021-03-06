import requests
import datetime
from bs4 import BeautifulSoup

MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря']

url_mail = f'https://pogoda.mail.ru/prognoz/'


def transliteration(cyrillic_text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia'.split('|')
    cyr_to_lat = {k: v for k, v in zip(cyrillic, latin)}

    latin_text = ''
    for letter in cyrillic_text:
        latin_text += cyr_to_lat.get(letter.lower(), letter)
    return latin_text


def get_temperature(city_rus):
    # по умолчанию Москва
    if len(city_rus) == 0:
        city_rus = 'Москва'
    # для запроса нужно перевести кирилическое написание города в латинское
    city = transliteration(city_rus)
    # какой-то у них на сайте программный косяк с Санкт-Петербургом, остальные города пишутся нормально
    if city == 'sankt-peterburg':
        city = 'sankt_peterburg'

    url = url_mail + city
    response = requests.get(url)

    print(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        temperature = soup.find_all('div', class_="information__content__temperature")
        today_temperature = temperature[0].text.split()[0]
        answer = f'В городе {city_rus} сейчас {today_temperature}. \n'

        # найдем архивную температуру
        arx_temperature = soup.find_all('span', class_="entitem__item-value")
        # если архивной температуры нет, то сайт сообщает зачем-то время восхода и заката, нам это не нужно
        if len(arx_temperature) == 4:
            d = datetime.date.today()
            month = MONTHS[d.month + 1]
            max_temperature = arx_temperature[0].text.split()
            min_temperature = arx_temperature[1].text.split()
            answer = answer + f'Сегодня {d.day} {month}:\n'
            answer = answer + f'максимальная температура {max_temperature[0]} была в {max_temperature[1]} году\n'
            answer = answer + f'минимальная {min_temperature[0]} в {min_temperature[1]} году\n '
        else:
            answer = answer + 'Архивных данных по температуре нет'
    else:
        answer = f'Города {city_rus} нет'

    return answer


if __name__ == '__main__':
    city_cyr = input('Введите название города: ')
    print(get_temperature(city_cyr))
