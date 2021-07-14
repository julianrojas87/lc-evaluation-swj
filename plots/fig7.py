import matplotlib.pyplot as plt


def autolabel(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(1.15*rect.get_width(), rect.get_y()+0.5*rect.get_height(),
                 '%d' % int(width),
                 ha='center', va='center', fontsize=14)


networks = [
    "Netherlands-Waterbus (100)", "Thailand-Greenbus (1000)", "Kobe-Subway (100)",
    "Sydney-Trainlink (500)", "San Francisco-BART (300)", "Spain-RENFE (5000)", 
    "Germany-DB (1000)", "Auckland-Waiheke (300)", "Belgium-NMBS (1000)", 
    "London-Tube (1000)", "Nairobi-SACCO (3000)", "Amsterdam-GVB (500)",
    "EU-Flixbus (3000)", "France-SNCF (1000)", "Brussels-STIB (300)", 
    "New York-MTABC (500)", "Madrid-CRTM (1000)", "Helsinki-HSL (877)", 
    "New Zealand-Bus (500)", "Chicago-CTA (3000)", 
    "Flanders-De Lijn (1861)", "Wallonia-TEC (1207)"
]

performance = [
    27, 36.27, 37, 45.81, 49.84, 154.23, 182.15, 283.67, 760.62, 942.02, 990.84,
    1885.51, 2220.44, 2295.44, 4816.93, 5319.87, 7761, 12004.97, 16394.7, 18332.73,
    34130.91, 36311.72
]

x_pos = [i for i, _ in enumerate(networks)]

rects = plt.barh(x_pos, performance, color='green')

plt.ylabel("Public transport network (connections/fragment)", fontsize=18)
plt.xlabel("Average query response time (ms)", fontsize=18)
plt.yticks(x_pos, networks, fontsize=14)
plt.xticks(fontsize=14)
plt.xscale('log')
#plt.gca().invert_yaxis()
autolabel(rects)

plt.show()
