"""
Python Visualization
Title : Single Pie Chart Example
Data : 20th OCT 2020
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Korean Font
plt.rc("font", family="chosunilboNM", size=13)

# Import excel data using Pandas
adrs = "excel_data/fixed_costs_in_living.xlsx"
raw_data = pd.read_excel(adrs, header=0)
npdata = raw_data.to_numpy()
row, col = npdata.shape[:]

# get a new cmap
cmap = plt.get_cmap("Pastel1")

# Draw a pie char
fig, ax = plt.subplots(figsize=(14, 7))
patches, texts, autotexts = ax.pie(npdata[:, 1], colors=cmap(range(row)), wedgeprops={"width": 0.5},
       shadow=False, explode=[0.1]*row, autopct='%1.0f%%')

# Add annotations
kw = {"arrowprops": {"arrowstyle": "-"}, "zorder": 1, "va": "center", "fontsize": 10}
ax.annotate("합계 {} 엔".format(sum(npdata[:, 1])), xy=(0, 0), xytext=(-0.25, 0))
for (i, p), a in zip(enumerate(patches), autotexts):
       # annotation for patches
       ang = (p.theta2 - p.theta1) / 2 + p.theta1
       x = np.cos(np.deg2rad(ang))
       y = np.sin(np.deg2rad(ang))
       hor_algn = {-1: "right", 1: "left"}[int(np.sign(x))]
       cnt_style = "angle,angleA=0,angleB={}".format(ang)
       kw["arrowprops"].update({"connectionstyle": cnt_style})
       ax.annotate(npdata[i, 0], xy=(x, y), xytext=(1.3*np.sign(x), 1.10*y),
                   horizontalalignment=hor_algn, **kw)

       # annotation for autotexts
       (auto_x, auto_y) = a.get_position()
       a.set_position(xy=(auto_x*1.3, auto_y*1.3))

plt.title("고정비들의 비율")
plt.tight_layout()
#plt.show()
plt.savefig(fname='figure_fixed_cost.jpeg', facecolor=None, dpi=1200, bbox_inches='tight')