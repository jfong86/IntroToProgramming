#Name:Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: Nov. 12, 2019
#create a map of New York City using folium library in Python

#import folium package for making maps
import folium

#Create a map with center at (40.75, -74.125)
mapNYC = folium.Map(location=[40.75, -74.125])

#add a marker for Hunter College to this map
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapNYC)

#Save the map
mapNYC.save(outfile='nycMap.html')
