import matplotlib.pyplot as plt


def autolabel(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(1.15*rect.get_width(), rect.get_y()+0.5*rect.get_height(),
                 '%d' % int(width),
                 ha='center', va='center')


networks = [
    "Netherlands-Waterbus (100)", "Kobe-Subway (50)", "Sydney-Trainlink (100)", "San Francisco-BART (100)",
    "Thailand-Greenbus (100)", "Spain-RENFE (1000)", "Germany-DB (300)", "Auckland-Waiheke (100)",
    "Belgium-NMBS (1000)", "London-Tube (1000)", "Nairobi-SACCO (3000)", "EU-Flixbus (3000)",
    "France-SNCF (3000)", "Amsterdam-GVB (1000)", "Brussels-STIB (1000)", "New York-MTABC (300)",
    "Madrid-CRTM (1000)", "Helsinki-HSL (3000)", "New Zealand-Bus (300)", "Wallonia-TEC (1207)",
    "Chicago-CTA (3000)", "Flanders-De Lijn (3000)"
]

performance = [
    44, 63, 74, 79, 82, 214, 278, 524, 831, 910,
    1563, 1997, 2207, 2715, 6883, 8213, 8634, 13494,
    28706, 29718, 34507, 38461
]

x_pos = [i for i, _ in enumerate(networks)]

rects = plt.barh(x_pos, performance, color='green')

plt.ylabel("Public transport network (connections/fragment)", fontsize=14)
plt.xlabel("(90th percentile) Query response time (ms)", fontsize=14)
plt.yticks(x_pos, networks, fontsize=12)
plt.xscale('log')
#plt.gca().invert_yaxis()
autolabel(rects)

plt.show()
