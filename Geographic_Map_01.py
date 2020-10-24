import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Get Korean font
plt.rc('font', family='chosunilboNM', size=13)

# The urls must be given as a raw file
# Obtain geojson data
url_json = 'https://raw.githubusercontent.com/ArchDH/Data_Visualization/main/Geo_data/Tokyo_N03-200101_13_GML/N03-20_13_200101.geojson'
tokyo = gpd.read_file(url_json)
tokyo = tokyo[:113]

# Obtain average rent data
url_rent = 'https://raw.githubusercontent.com/ArchDH/Data_Visualization/main/excel_data/average_rent_in_Tokyo_2020.xlsx'
avr_rent = pd.read_excel(url_rent)

rent = [0]*tokyo.shape[0]
for i, ward in enumerate(tokyo['N03_004'][:113]):
    rent[i] = (avr_rent.loc[avr_rent['district'] == ward]['1K/1DK'].to_numpy()[0][:3])
tokyo['avr_rent'] = rent

# Obtain centroid of each polygon
gs = gpd.GeoSeries(tokyo['geometry'])
crs = gs.to_crs(epsg=6668)
tokyo['centroid'] = crs.centroid

# Plot geojson data
# Geopandas mapping tool is the interface to the matplotlib library.
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 7))
new_cmap = plt.get_cmap('Oranges')
tokyo.plot(column='avr_rent', legend=True, legend_kwds={"title": "월세 [만엔]", "bbox_to_anchor": (1.3, 1.0), "frameon": False}
           , edgecolor='grey', cmap=new_cmap, ax=ax)
ax.set(xlim=(139.5, 139.934), ylim=(35.4846, 35.9097))

# Ward name annotation
# googletrans library is the google translator API
from googletrans import Translator
translator = Translator()
for (i, ward), cent in zip(enumerate(tokyo[:-1]['N03_004']), tokyo['centroid']):
    if ward != tokyo['N03_004'].at[i+1]:
        kr_ward = translator.translate(ward, dest='korean')
        ax.annotate(kr_ward.text, xy=(cent.x, cent.y))

plt.title("도쿄 23구내 월세평균", size=16)
plt.tight_layout()
plt.show()
# #plt.savefig(fname='figure.jpeg', facecolor=None, dpi=1200, bbox_inches='tight')