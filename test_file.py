import json
import geopandas
import matplotlib.pyplot as plt

adrs = "Geo_data/Tokyo_N03-200101_13_GML/N03-20_13_200101.json"
tokyo = geopandas.read_file(adrs)
