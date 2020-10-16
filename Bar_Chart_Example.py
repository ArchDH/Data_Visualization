"""
Python Visualization
Title : Bar Chart Example
Data : 16th OCT 2020
"""
import pandas as pd
import matplotlib.pyplot as plt

# Set a Korean font
plt.rc('font', family='chosunilboNM', size=13)

# Import excel data
raw_data = pd.read_excel('base_wage_in_Japan.xlsx', header=0)
npdata = raw_data.to_numpy()

# Get a new cmap
cmap = plt.get_cmap('Set2', 2)

# Value annotation function
def annotate(bars, num):
    """Attach a text label above each bar"""
    for bar in bars:
        height = bar.get_height()
        ax[num].annotate('{} 만엔'.format(height),
                         xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 10),
                         textcoords="offset points",
                         ha='center', va='bottom')

# Draw bar chart
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))
bars1 = ax[0].bar(npdata[:, 0], npdata[:, 1], color=cmap(0))
ax[0].set(ylim=(0, 800))
ax[0].set_title("나이에 따른 연봉 변화")
ax[0].set_ylabel("연봉 (엔)")
ax[0].set_xlabel("나이")
annotate(bars1, 0)

bars2 = ax[1].bar(npdata[:, 0], npdata[:, 2], color=cmap(1))
ax[1].set(ylim=(0, 60))
ax[1].set_title("나이에 따른 기본급 변화")
ax[1].set_ylabel("기본급 (엔)")
ax[1].set_xlabel("나이")
annotate(bars2, 1)

fig.suptitle("일본 직장인의 나이에 따른 연봉 및 기본급 평균 (2018년 일본정부)", y=1.05)
fig.tight_layout()
plt.savefig(fname='figure.jpeg', facecolor=None, dpi=900, bbox_inches='tight')
