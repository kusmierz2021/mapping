import folium
import webbrowser


map = folium.Map(location=[52.23181144912179, 21.00601682474304],
                 zoom_start=12, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="visited places")

coordinates = [[52.22064940703729, 21.010000127674964],
               [52.21908390898992, 21.01185062652799]]

for coordinate in coordinates:
    fg.add_child(folium.Marker(location=coordinate,
                               popup="Gmach Główmy Politechniki Warszawskiej",
                               icon=folium.Icon("lightgreen", "beige")))
map.add_child(fg)

map.save("map1.html")

webbrowser.open("map1.html")
