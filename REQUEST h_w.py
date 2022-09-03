from pprint import pprint
import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
sp = response.json()

hero_dict = {}
herous = ['Hulk', 'Captain America', 'Thanos']
for hero in sp:
    if hero['name'] in herous:
        hero_dict[hero['name']] = hero['powerstats']['intelligence']
# pprint(hero_dict)

pprint(max(hero_dict))