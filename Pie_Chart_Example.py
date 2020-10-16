"""
Python Visualization
Title : Pie Chart Example
Data : 15th OCT 2020
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set a Korean font
plt.rc('font', family='chosunilboNM', size=11)

# Import excel data
data_adrs = // directory to data file

# When no headers exist, you have to state header=None explicitly.
# Pandas read method returns DataFrame
data = pd.read_excel(data_adrs, header=0)

# to numpy 2d array
npdata = data.to_numpy()
row_size = npdata.shape[1]

# Draw pie charts
# Get a new cmap
cmap = plt.get_cmap('Set2', row_size)
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(14, 7))
kw = dict(arrowprops=dict(arrowstyle="-"), zorder=0, va="center")
sub_titles = ["국적별 외자계기업 비율", "업종별 외자계기업 비율", "지역별 외자계기업 비율"]

for num in range(3):
    wedges, texts, auto = ax[num].pie(npdata[:, 2*num-1], wedgeprops=dict(width=0.8), autopct='%1.1f%%', shadow=False,
                                      colors=cmap(range(row_size)))

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2 + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax[num].annotate(npdata[i, 2*num], xy=(x, y), xytext=(1.3*np.sign(x), 1.3*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax[num].set_title(sub_titles[num], y=1.01)

fig.suptitle("외자계 기업의 일본지사에 대한 조사 (2018년 일본정부)", fontsize=18, y=1.02)
plt.tight_layout()
plt.show()
#plt.savefig(fname='figure.jpeg', facecolor=None, dpi=1200, bbox_inches='tight')