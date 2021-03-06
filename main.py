import folium
from jinja2.environment import get_spontaneous_environment
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name = list(data["NAME"])

def color_gen(elevation):
    if 0 <= elevation < 1000:
        return "green"  
    elif  1000<=elevation<2000:
        return "purple"
    elif 2000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


html = """
<h4>Volcano information:</h4><br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
map=folium.Map(location=[38,-99.09],zoom_start=6, tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name ="Volcanoes Mapping")
for lt,ln,ele,name in (zip(lat,lon,elev,name)):
    iframe=folium.IFrame(html= html % (name, name, ele), width =200 ,height = 100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6 , popup=folium.Popup(iframe),fill_color=color_gen(ele),color='black',fil_opacity=0.8))
fgp=folium.FeatureGroup(name ="Population Mapping")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'greeen' if x['properties']['POP2005'] < 10000000 
else  'orange' if 10000000 <=x['properties']['POP2005']<=20000000  else 'red'} ) )
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("localhost.html")