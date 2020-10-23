from urllib.request import urlopen
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import googletrans as gt

# Get Korean font
plt.rc('font', family='chosunilboNM', size=13)

# The url must be given as a raw file
url = 'https://raw.githubusercontent.com/ArchDH/Data_Visualization/main/Geo_data/Tokyo_N03-200101_13_GML/N03-20_13_200101.geojson'
with urlopen(url) as response:
    tokyo = gpd.read_file(response, encoding='SHIFT-JIS')

for i, v in enumerate(tokyo[:-1]['N03_004']):
    if v != tokyo['N03_004'].at[i+1]:
        print(v)