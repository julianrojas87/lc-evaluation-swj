import matplotlib
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

colors = ['#556b2f', '#7f0000', '#483d8b', 
    '#3cb371', '#b8860b', '#008b8b', 
    '#9acd32', '#00008b', '#ff4500', 
    '#ffd700', '#7fff00', '#ba55d3', 
    '#00ff7f', '#00ffff', '#0000ff', 
    '#ff00ff', '#1e90ff', '#eee8aa', 
    '#dda0dd', '#ff1493', '#ffa07a', '#87cefa']

networks = [
    "Netherlands-Waterbus", "Kobe-Subway", "Sydney-Trainlink",
    "San Francisco-BART", "Thailand-Greenbus", "Spain-RENFE",
    "Germany-DB", "Auckland-Waiheke", "Belgium-NMBS",
    "London-Tube", "Nairobi-SACCO", "EU-Flixbus",
    "France-SNCF", "Amsterdam-GVB", "Brussels-STIB",
    "New York-MTABC", "Madrid-CRTM", "Helsinki-HSL",
    "New Zealand-Bus", "Wallonia-TEC", "Chicago-CTA", "Flanders-De Lijn"
]

performance = np.array([
    27, 37, 45.81, 49.84, 36.27, 154.23, 182.15, 283.67, 760.62, 942.02,
    990.84, 2220.44, 2295.44, 1885.51, 4816.93, 5319.87, 7761, 12004.97,
    16394.7, 36311.72, 27887.7, 34130.91 
])

fragmentation = [100, 100, 500, 300, 1000, 5000, 1000, 300, 1000, 1000, 
    3000, 3000, 1000, 500, 300, 500, 1000, 877, 500, 1207, 300, 1861]

stops = np.array([44, 27, 361, 50, 112, 714, 433, 125, 606, 379, 2787, 
    1744, 4646, 1356, 2316, 3590, 5192, 8155, 2259, 31131, 11042, 29905])

connections = np.array([936, 6086, 891, 7755, 1024, 6159, 7680, 6020, 57950, 321952, 5857, 
    51636, 79796, 180695, 350038, 343582, 706642, 689834, 153690, 623808, 1128828, 826572])

K = np.array([1.179, 6.595, 0.192, 9.282, 3.206, 3.481, 4.476, 0.153, 35.367, 1056.554,
     6.711, 162.011, 20.196, 0.687, 2.474, 1.197, 3.937, 130.761, 0.509, 36.023, 2.209, 117.118])

D = np.array([9.1, 84, 0.1, 63.1, 9.6, 1.6, 3.4, 0.4, 19.4,
     931.7, 0.8, 30.9, 1.4, 0.2, 0.3, 0.1, 0.2, 5.3, 0.07, 0.3, 0.06, 1.3])

C = np.array([0, 0, 0.015, 0.198, 0.974, 2.692, 6.584, 0, 0.545, 6.778, 1.262, 27.142,
     2.575, 0.001, 0.138, 0.596, 2.614, 3.781, 0.032, 3.991, 0.331, 1.625])

ACD = np.array([11.08, 2.57, 51.24, 4.53, 83.81, 32.97, 33.05, 1.6, 5.66, 2.51, 4.69,
       133.05, 16.52, 2.11, 1.76, 4.19, 5.49, 1.62, 2.01, 1.55, 1.37, 1.56])

SCQ = [120, 140, 380, 370, 450, 4100, 2970, 390, 9760, 13030, 5070, 33470, 39540, 
    9190, 13770, 28220, 87420, 76440, 20510, 234310, 64240, 322240]

# Calculate Pearson coefficient
pearson_stops = np.corrcoef(stops, performance)[0][1]
print("pearson_stops = " + str(pearson_stops))
pearson_connections = np.corrcoef(connections, performance)[0][1]
print("pearson_connections = " + str(pearson_connections))
pearson_K = np.corrcoef(K, performance)[0][1]
pearson_D = np.corrcoef(D, performance)[0][1]
pearson_C = np.corrcoef(C, performance)[0][1]
pearson_ACD = np.corrcoef(ACD, performance)[0][1]

# Create subplots
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

for i in range(len(performance)):
    ax1.scatter(np.log10(performance[i]), np.log10(stops[i]), s=100, c=colors[i], alpha=0.5, label="n" + str(i) + " = " + networks[i])
    ax1.annotate("n" + str(i), (np.log10(performance[i]), np.log10(stops[i])), fontsize=14)
    ax2.scatter(np.log10(performance[i]), np.log10(connections[i]), s=100, c=colors[i], alpha=0.5, label="n" + str(i) + " = " + networks[i])
    ax2.annotate("n" + str(i), (np.log10(performance[i]), np.log10(connections[i])), fontsize=14)
    ax3.scatter(np.log10(performance[i]), np.log10(K[i]), s=100, c=colors[i], alpha=0.5, label="n" + str(i) + " = " + networks[i])
    ax3.annotate("n" + str(i), (np.log10(performance[i]), np.log10(K[i])), fontsize=14)
    ax4.scatter(np.log10(performance[i]), np.log10(D[i]), s=100, c=colors[i], alpha=0.5)
    ax4.annotate("n" + str(i), (np.log10(performance[i]), np.log10(D[i])), fontsize=14)
    ax5.scatter(performance[i], C[i], s=100, c=colors[i], alpha=0.5)
    ax5.annotate("n" + str(i), (performance[i], C[i]), fontsize=14)
    ax6.scatter(np.log10(performance[i]), np.log10(ACD[i]), s=100, c=colors[i], alpha=0.5)
    ax6.annotate("n" + str(i), (np.log10(performance[i]), np.log10(ACD[i])), fontsize=14)


handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=5)
formatter = lambda x, pos: f'{10 ** x:g}'

sns.regplot(ax=ax1, x=np.log10(performance), y=np.log10(stops), scatter_kws={'facecolors':colors, 'alpha': 0.0})
x_ticks = np.log10(np.array([10, 50, 100, 500, 1000, 5000, 10000, 20000, 40000]))
ax1.set_xticks(x_ticks)
y_ticks1 = np.log10(np.array([10, 50, 100, 500, 1000, 5000, 10000, 35000]))
ax1.set_yticks(y_ticks1)
ax1.get_xaxis().set_major_formatter(formatter)
ax1.get_yaxis().set_major_formatter(formatter)
ax1.set_xlabel("average response time (ms)")
ax1.set_ylabel("total stops")
ax1.grid(alpha=0.3)

sns.regplot(ax=ax2, x=np.log10(performance), y=np.log10(connections), scatter_kws={'facecolors':colors, 'alpha': 0.0})
ax2.set_xticks(x_ticks)
y_ticks2= np.log10(np.array([700, 1500, 3000, 10000, 50000, 150000, 300000, 1200000]))
ax2.set_yticks(y_ticks2)
ax2.get_xaxis().set_major_formatter(formatter)
ax2.get_yaxis().set_major_formatter(formatter)
ax2.set_xlabel("average response time (ms)")
ax2.set_ylabel("total connections")
ax2.grid(alpha=0.3)

sns.regplot(ax=ax3, x=np.log10(performance), y=np.log10(K), scatter_kws={'facecolors':colors, 'alpha': 0.0})
ax3.set_xticks(x_ticks)
y_ticks3= np.log10(np.array([0.1, 1, 10, 100, 1100]))
ax3.set_yticks(y_ticks3)
ax3.get_xaxis().set_major_formatter(formatter)
ax3.get_yaxis().set_major_formatter(formatter)
ax3.set_xlabel("average response time (ms)")
ax3.set_ylabel("K (average degree)")
ax3.grid(alpha=0.3)

sns.regplot(ax=ax4, x=np.log10(performance), y=np.log10(D), scatter_kws={'facecolors':colors, 'alpha': 0.0})
ax4.set_xticks(x_ticks)
y_ticks4= np.log10(np.array([0.1, 1, 10, 100, 1000]))
ax4.set_yticks(y_ticks4)
ax4.get_xaxis().set_major_formatter(formatter)
ax4.get_yaxis().set_major_formatter(formatter)
ax4.set_xlabel("average response time (ms)")
ax4.set_ylabel("D (density) * 1000")
ax4.grid(alpha=0.3)

ax5 = sns.regplot(ax=ax5, x=performance, y=C, scatter_kws={'facecolors':colors, 'alpha': 0.0}, logx=True)
ax5.set_xscale("log")
ax5.set_yscale("log")
ax5.set_yticks([0.001, 0.01, 0.1, 1, 10, 30])
ax5.set_xticks([10, 100, 1000, 10000, 30000])
ax5.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.set_xlabel("average response time (ms)")
ax5.set_ylabel("C (clustering coefficient)")
ax5.grid(alpha=0.3)

sns.regplot(ax=ax6, x=np.log10(performance), y=np.log10(ACD), scatter_kws={'facecolors':colors, 'alpha': 0.0})
ax6.set_xticks(x_ticks)
y_ticks6= np.log10(np.array([1, 10, 30, 50, 100, 200]))
ax6.set_yticks(y_ticks6)
ax6.get_xaxis().set_major_formatter(formatter)
ax6.get_yaxis().set_major_formatter(formatter)
ax6.set_xlabel("average response time (ms)")
ax6.set_ylabel("ACD (average connection duration)")
ax6.grid(alpha=0.3)

plt.show()
