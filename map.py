import folium
import webbrowser
import json
import os


def get_color(name):
    if name.title() in named_countries:
        return 'green'
    else:
        return 'red'


data = json.loads(open('world.json', 'r', encoding='utf-8-sig').read())

html = """
Country name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Population: %s 
"""


countries = [item['properties']['NAME'] for item in data['features']]
countries_to_finish = len(countries)
named_countries = []


os.system("cls")

while True:
    named_countries.sort()
    print(named_countries)
    print("""
NAME ALL COUNTRIES!
enter 'x' to show results
\n
named countries: {}
countries to name: {}
""".format(len(named_countries), countries_to_finish))
    name = input("next country ->  ")
    if name == 'x':
        break
    elif name.lower() in [name.lower() for name in countries]:
        if name.title() not in named_countries:
            named_countries.append(name.title())
            countries_to_finish -= 1
    os.system("cls")


map = folium.Map(location=[0, 0],
                 zoom_start=1.95, tiles="Stamen Watercolor")

fg = folium.FeatureGroup(name="named countries")

for country in data['features']:
    iframe = folium.IFrame(html=html % (country['properties']['NAME'],
                                        country['properties']['NAME'],
                                        country['properties']['POP2005']),
                           width=200, height=100)

    fg.add_child(folium.Marker(location=[country['properties']['LAT'],
                                         country['properties']['LON']],
                               popup=folium.Popup(iframe),
                               icon=folium.Icon(get_color(
                                         country['properties']['NAME']))))

fg.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if
                              x['properties']['NAME'].title() in
                              named_countries else 'red'}))

map.add_child(fg)
map.save("map.html")

webbrowser.open("map.html")
