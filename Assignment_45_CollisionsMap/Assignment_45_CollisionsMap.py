#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: Nov. 12, 2019
"""
write a program that asks the user for the name of a CSV file,
name of the output file, and creates a map with markers for all the traffic collisions from the input file.
"""

import folium
import pandas as pd

inFile = input("Enter CSV file name:")
outFile = input("Enter output file:")

collisionDF = pd.read_csv(inFile)

collisionMap = folium.Map(location=[40.768731,-73.964915], tiles="Cartodb Positron", zoom_start = 10)

for index, row in collisionDF.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup = name)
    newMarker.add_to(collisionMap)

collisionMap.save(outfile = outFile)
