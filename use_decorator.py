import requests
from parametrize_decor import logger


@logger('main.log')
def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    base_url = 'https://akabab.github.io/superhero-api/api/'
    response = requests.get(base_url+'all.json')
    all_heroes = response.json()
    smartest = dict()
    for hero in all_heroes:
        name = hero['name']
        if name in list_:
            smartest[name] = hero['powerstats']['intelligence']
    the_smartest_superhero += max(smartest, key=lambda x: smartest[x])
    return the_smartest_superhero


list_ = {'Hulk', 'Captain America', 'Thanos'}

print(get_the_smartest_superhero())
