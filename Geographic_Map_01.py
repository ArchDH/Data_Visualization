# -*- coding: utf-8 -*-
"""
Python Visualization
Title : Choropleth example using GeoJason and Plotly
Data : 20th OCT 2020
"""
import matplotlib.pyplot as plt
import geopandas

# Load a geojson file
adrs = "Geo_data/Tokyo_N03-200101_13_GML/N03-20_13_200101.json"
tokyo = geopandas.read_file(adrs, encoding='SHIFT-JIS')

# Plotting
ax = plt.axes()
ax.set(xlim=(138.8, 140), ylim=(35.4, 36))
# polygon infill
tokyo.plot(ax=ax)
# boundary
tokyo.boundary.plot(ax=ax, edgecolor='k')
plt.tight_layout()
plt.show()