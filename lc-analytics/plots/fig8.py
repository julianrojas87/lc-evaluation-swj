import matplotlib
import random
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

performance = [
    44, 63, 74, 79, 82, 214, 278, 524, 831, 910,
    1563, 1997, 2207, 2715, 6883, 8213, 8634, 13494,
    28706, 29718, 34507, 38461
]

stops = [44, 27, 361, 50, 112, 714, 433, 125, 606, 379, 2787, 
    1744, 4646, 1356, 2316, 3590, 5192, 8155, 2259, 31131, 11042, 29905]

connections = [936, 6086, 891, 7755, 1024, 6159, 7680, 6020, 57950, 321952, 5857, 
    51636, 79796, 180695, 350038, 343582, 706642, 689834, 153690, 623808, 1128828, 826572]

K = [1.179, 6.595, 0.192, 9.282, 3.206, 3.481, 4.476, 0.153, 35.367, 1056.554,
     6.711, 162.011, 20.196, 0.687, 2.474, 1.197, 3.937, 130.761, 0.509, 36.023, 2.209, 117.118]
D = [9.1, 84, 0.1, 63.1, 9.6, 1.6, 3.4, 0.4, 19.4,
     931.7, 0.8, 30.9, 1.4, 0.2, 0.3, 0.1, 0.2, 5.3, 0.07, 0.3, 0.06, 1.3]
C = [0, 0, 0.015, 0.198, 0.974, 2.692, 6.584, 0, 0.545, 6.778, 1.262, 27.142,
     2.575, 0.001, 0.138, 0.596, 2.614, 3.781, 0.032, 3.991, 0.331, 1.625]
ACD = [11.08, 2.57, 51.24, 4.53, 83.81, 32.97, 33.05, 1.6, 5.66, 2.51, 4.69,
       133.05, 16.52, 2.11, 1.76, 4.19, 5.49, 1.62, 2.01, 1.55, 1.37, 1.56]

# Create subplots
#plt.style.use('seaborn-darkgrid')
plt.rcParams.update({'font.size': 13})
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

for i in range(len(performance)):
    ax1.scatter(performance[i], stops[i], s=100, c=colors[i], alpha=0.5, label="n" + str(i) + " = " + networks[i])
    ax1.annotate("n" + str(i), (performance[i], stops[i]), fontsize=12)
    ax2.scatter(performance[i], connections[i], s=100, c=colors[i], alpha=0.5, label="n" + str(i) + " = " + networks[i])
    ax2.annotate("n" + str(i), (performance[i], connections[i]), fontsize=12)
    ax3.scatter(performance[i], K[i], s=100, c=colors[i], alpha=0.5, label="n" + str(i) + " = " + networks[i])
    ax3.annotate("n" + str(i), (performance[i], K[i]), fontsize=12)
    ax4.scatter(performance[i], D[i], s=100, c=colors[i], alpha=0.5)
    ax4.annotate("n" + str(i), (performance[i], D[i]), fontsize=12)
    ax5.scatter(performance[i], C[i], s=100, c=colors[i], alpha=0.5)
    ax5.annotate("n" + str(i), (performance[i], C[i]), fontsize=12)
    ax6.scatter(performance[i], ACD[i], s=100, c=colors[i], alpha=0.5)
    ax6.annotate("n" + str(i), (performance[i], ACD[i]), fontsize=12)

handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=5)

ax1.set_yscale("log")
ax1.set_xscale("log")
ax1.set_yticks([1, 10, 100, 1000, 10000, 20000, 35000])
ax1.set_xticks([10, 100, 1000, 10000, 30000])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_xlabel("response time (ms)")
ax1.set_ylabel("total stops")
ax1.grid()

ax2.set_yscale("log")
ax2.set_xscale("log")
#ax2.set_yticks([100, 1000, 10000, 30000, 50000, 1000, 1500])
ax2.set_xticks([10, 100, 1000, 10000, 30000])
ax2.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.set_xlabel("response time (ms)")
ax2.set_ylabel("total connections")
ax2.grid()

ax3.set_yscale("log")
ax3.set_xscale("log")
ax3.set_yticks([0.1, 1, 10, 100, 1000])
ax3.set_xticks([10, 100, 1000, 10000, 30000])
ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.set_xlabel("response time (ms)")
ax3.set_ylabel("K (average degree)")
ax3.grid()

ax4.set_yscale("log")
ax4.set_xscale("log")
ax4.set_yticks([0.01, 0.1, 1, 10, 100, 1000])
ax4.set_xticks([10, 100, 1000, 10000, 30000])
ax4.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.set_xlabel("response time (ms)")
ax4.set_ylabel("D (density) * 1000")
ax4.grid()

ax5.set_yscale("log")
ax5.set_xscale("log")
ax5.set_yticks([0.001, 0.01, 0.1, 1, 10, 30])
ax5.set_xticks([10, 100, 1000, 10000, 30000])
ax5.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.set_xlabel("response time (ms)")
ax5.set_ylabel("C (clustering coefficient)")
ax5.grid()

ax6.set_yscale("log")
ax6.set_xscale("log")
ax6.set_yticks([1, 10, 30, 50, 100, 200])
ax6.set_xticks([10, 100, 1000, 10000, 30000])
ax6.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.set_xlabel("response time (ms)")
ax6.set_ylabel("ACD (average connection duration)")
ax6.grid()

plt.show()
