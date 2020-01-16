import requests
import datetime
from bs4 import BeautifulSoup


def transliteration(cyrillic_text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia'.split('|')
    cyr_to_lat = {k: v for k, v in zip(cyrillic, latin)}

    latin_text = ''
    for letter in cyrillic_text:
        latin_text += cyr_to_lat.get(letter.lower(), letter)
    return latin_text


if __name__ == '__main__':
    city_rus = input('Введите название города: ')

    # по умолчанию Москва
    if len(city_rus) == 0:
        city_rus = 'Москва'

    # нужно перевести кирилическое написание города в латинское для запроса
    city = transliteration(city_rus)
    # какой-то у них на сайте программный косяк с Санкт-Петербургом, остальные города пишутся нормально
    if city == 'sankt-peterburg':
        city = 'sankt_peterburg'

    url = f'https://pogoda.mail.ru/prognoz/{city}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = soup.find_all('div', class_ ="information__content__temperature")
        print(temperature[0].text)
        arx_temperature = soup.find_all('span', class_="entitem__item-value")
        if len(arx_temperature) == 4:
            max_temperature = arx_temperature[0].text.split()
            min_temperature = arx_temperature[1].text.split()
            print(f'В городе {city_rus}  были зарегистрированы:  ')
            print(f'максимальная температура {max_temperature[0]} в {max_temperature[1]} году')
            print(f'минимальная {min_temperature[0]} в {min_temperature[1]} году ')
        else:
            print('Архивных данных нет')
    else:
        print(f'Города {city_rus} нет')
