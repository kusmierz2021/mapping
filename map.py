import folium
import webbrowser

html = """
Country name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Population: %s 
"""


def get_color(name, named_countries):
    if name.title() in named_countries:
        return 'green'
    else:
        return 'red'


def show_map(data, named_countries, finish=False):
    map = folium.Map(location=[0, 0],
                     zoom_start=1.95,
                     tiles="Stamen Terrain" if finish else "Stamen Watercolor")

    fgc = folium.FeatureGroup(name="countries information")
    fgb = folium.FeatureGroup(name="boundaries")
    fgb.add_child(folium.GeoJson(
        data=open('world.json', 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor': 'green' if
                                  x['properties']['NAME'].title() in
                                  named_countries else 'red'}))

    for country in data['features']:
        if country['properties']['NAME'].title() in named_countries or finish:
            iframe = folium.IFrame(html=html % (country['properties']['NAME'],
                                                country['properties']['NAME'],
                                                country['properties']['POP2005']),
                                   width=200, height=100)

            fgc.add_child(folium.Marker(location=[country['properties']['LAT'],
                                                  country['properties']['LON']],
                                        popup=folium.Popup(iframe),
                                        icon=folium.Icon(get_color(
                                                country['properties']['NAME'],
                                                named_countries))))

    map.add_child(fgb)
    map.add_child(fgc)
    map.add_child(folium.LayerControl())
    map.save("map.html")

    webbrowser.open("map.html")
