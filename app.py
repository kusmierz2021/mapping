import json
from map import show_map
import os


data = json.loads(open('world.json', 'r', encoding='utf-8-sig').read())


countries = [item['properties']['NAME'] for item in data['features']]
countries_to_finish = len(countries)
named_countries = []


os.system("cls")

while True:
    named_countries.sort()
    print(named_countries)
    print("""
NAME ALL COUNTRIES!
enter 's' to show result map
enter 'x' to finish
\n
named countries: {}
countries to name: {}
""".format(len(named_countries), countries_to_finish))
    name = input("next country ->  ")
    if name == 'x':
        show_map(data, named_countries, True)
        break
    elif name == 's':
        show_map(data, named_countries)
    elif name.lower() in [name.lower() for name in countries]:
        if name.title() not in named_countries:
            named_countries.append(name.title())
            countries_to_finish -= 1
    os.system("cls")
