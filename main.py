import requests
from bs4 import BeautifulSoup


def transliteration(cyrillic_text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia'.split('|')
    cyr_to_lat = {k: v for k, v in zip(cyrillic, latin)}

    latin_text = ''
    for letter in cyrillic_text:
        latin_text += cyr_to_lat.get(letter.lower(), letter)
    return latin_text


city_rus = input('Введите название города: ')
# нужно перевести кирилическое написание города в латинское для запроса
city = transliteration(city_rus)
print(city)