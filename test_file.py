from urllib.request import urlopen
import geopandas

url = 'https://github.com/ArchDH/Data_Visualization/blob/main/Geo_data/Tokyo_N03-200101_13_GML/N03-20_13_200101.json'
with urlopen(url) as response:
    tokyo = geopandas.read_file(response)

