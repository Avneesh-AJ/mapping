import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name = list(data["NAME"])


html = """
<h4>Volcano information:</h4><br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
map=folium.Map(location=[38,-99.09],zoom_start=6, tiles="Stamen Terrain")
fg=folium.FeatureGroup(name ="My Map")
for lt,ln,ele,name in (zip(lat,lon,elev,name)):
    iframe=folium.IFrame(html= html % (name, name, ele), width =200 ,height = 100)
    fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("localhost.html")