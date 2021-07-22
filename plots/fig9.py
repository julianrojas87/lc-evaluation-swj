import matplotlib
from matplotlib import pyplot as plt
import csv

# Function to calculate Y-axis (CPU) values of a transit network
def get_cpu_usage(ptn, server):
    root_path = "../scalability-test/server/results/" + ptn + "/" + server + "/"
    x = [1, 2, 5, 10, 20, 50]
    y = []

    for i in x:
        with open(root_path + str(i) + ".csv", 'r') as csvfile:
            data = list(csv.reader(csvfile, delimiter=','))
            cpu = 0
            for index, d in enumerate(data):
                if(index > 0):
                    cpu += float(d[2])
            cpu = cpu / (len(data) - 1)
            y.append(cpu)

    return x, y

# Function to calculate the average CPU usage of NGINX for a set of networks
def get_nginx_usage(networks):
    root_path = "../scalability-test/server/results/"
    x = [1, 2, 5, 10, 20, 50]
    y = []

    for i in x:
        cpu = 0
        count = 0
        for net in networks:
            with open(root_path + net + "/lc_cache/" + str(i) + ".csv", "r") as csvfile:
                data = list(csv.reader(csvfile, delimiter=','))
                for index, d in enumerate(data):
                    if(index > 0 and d[1] == 'server_nginx_1'):
                        cpu += float(d[2])
                        count += 1
        cpu = cpu / count
        y.append(cpu)

    return x, y

# Get X and Y axises for each public transport network
amsterdam_gvb_otp_x, amsterdam_gvb_otp_y = get_cpu_usage("amsterdam-gvb", "otp")
amsterdam_gvb_lc_x, amsterdam_gvb_lc_y = get_cpu_usage("amsterdam-gvb", "lc_cache")

chicago_cta_otp_x, chicago_cta_otp_y = get_cpu_usage("chicago-cta", "otp")
chicago_cta_lc_x, chicago_cta_lc_y = get_cpu_usage("chicago-cta", "lc_cache")

delijn_otp_x, delijn_otp_y = get_cpu_usage("delijn", "otp")
delijn_lc_x, delijn_lc_y = get_cpu_usage("delijn", "lc_cache")

helsinki_hsl_otp_x, helsinki_hsl_otp_y = get_cpu_usage("helsinki-hsl", "otp")
helsinki_hsl_lc_x, helsinki_hsl_lc_y = get_cpu_usage("helsinki-hsl", "lc_cache")

kobe_subway_otp_x, kobe_subway_otp_y = get_cpu_usage("kobe-subway", "otp")
kobe_subway_lc_x, kobe_subway_lc_y = get_cpu_usage("kobe-subway", "lc_cache")

london_tube_otp_x, london_tube_otp_y = get_cpu_usage("london-tube", "otp")
london_tube_lc_x, london_tube_lc_y = get_cpu_usage("london-tube", "lc_cache")

madrid_bus_otp_x, madrid_bus_otp_y = get_cpu_usage("madrid-bus", "otp")
madrid_bus_lc_x, madrid_bus_lc_y = get_cpu_usage("madrid-bus", "lc_cache")

nairobi_sacco_otp_x, nairobi_sacco_otp_y = get_cpu_usage("nairobi-sacco", "otp")
nairobi_sacco_lc_x, nairobi_sacco_lc_y = get_cpu_usage("nairobi-sacco", "lc_cache")

new_york_mtabc_otp_x, new_york_mtabc_otp_y = get_cpu_usage("new-york-mtabc", "otp")
new_york_mtabc_lc_x, new_york_mtabc_lc_y = get_cpu_usage("new-york-mtabc", "lc_cache")

nl_waterbus_otp_x, nl_waterbus_otp_y = get_cpu_usage("nl-waterbus", "otp")
nl_waterbus_lc_x, nl_waterbus_lc_y = get_cpu_usage("nl-waterbus", "lc_cache")

nmbs_otp_x, nmbs_otp_y = get_cpu_usage("nmbs", "otp")
nmbs_lc_x, nmbs_lc_y = get_cpu_usage("nmbs", "lc_cache")

sf_bart_otp_x, sf_bart_otp_y = get_cpu_usage("sf-bart", "otp")
sf_bart_lc_x, sf_bart_lc_y = get_cpu_usage("sf-bart", "lc_cache")

stib_otp_x, stib_otp_y = get_cpu_usage("stib", "otp")
stib_lc_x, stib_lc_y = get_cpu_usage("stib", "lc_cache")

sydney_trainlink_otp_x, sydney_trainlink_otp_y = get_cpu_usage("sydney-trainlink", "otp")
sydney_trainlink_lc_x, sydney_trainlink_lc_y = get_cpu_usage("sydney-trainlink", "lc_cache")

tec_otp_x, tec_otp_y = get_cpu_usage("tec", "otp")
tec_lc_x, tec_lc_y = get_cpu_usage("tec", "lc_cache")

thailand_greenbus_otp_x, thailand_greenbus_otp_y = get_cpu_usage("thailand-greenbus", "otp")
thailand_greenbus_lc_x, thailand_greenbus_lc_y = get_cpu_usage("thailand-greenbus", "lc_cache")

# Calculate NGINX average CPU usage per plot
#nginx1_x, nginx1_y = get_nginx_usage(['sydney-trainlink', 'thailand-greenbus', 'kobe-subway'])
#nginx2_x, nginx2_y = get_nginx_usage(['nairobi-sacco', 'sf-bart', 'amsterdam-gvb', 'nmbs'])
#nginx3_x, nginx3_y = get_nginx_usage(['stib', 'london-tube', 'new-york-mtabc', 'madrid-bus'])
#nginx4_x, nginx4_y = get_nginx_usage(['tec', 'delijn', 'chicago-cta', 'helsinki-hsl'])

# Create subplots
plt.rcParams.update({'font.size': 12})
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(nrows=4, ncols=2)
lw = 2

ax1.plot(nl_waterbus_otp_x, nl_waterbus_otp_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw)
ax1.plot(sydney_trainlink_otp_x, sydney_trainlink_otp_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw)
ax1.plot(thailand_greenbus_otp_x, thailand_greenbus_otp_y, marker='o', markersize=3.5, label="Thailand-Greenbus", linewidth=lw)
ax1.plot(kobe_subway_otp_x, kobe_subway_otp_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw)
ax1.set_title("OpenTripPlanner Server")
ax1.set_ylabel("cpu use (%)")
ax1.set_xscale("log")
ax1.set_xticks([1, 2, 5, 10, 20, 50])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_yticks([0, 20, 40, 60, 80, 100])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)
ax1.grid(alpha=0.3)


ax3.plot(nairobi_sacco_otp_x, nairobi_sacco_otp_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw)
ax3.plot(sf_bart_otp_x, sf_bart_otp_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw)
ax3.plot(amsterdam_gvb_otp_x, amsterdam_gvb_otp_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw)
ax3.plot(nmbs_otp_x, nmbs_otp_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw)
ax3.set_ylabel("cpu use (%)")
ax3.set_xscale("log")
ax3.set_xticks([1, 2, 5, 10, 20, 50])
ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.set_yticks([0, 20, 40, 60, 80, 100])
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.spines["right"].set_visible(False)
ax3.spines["top"].set_visible(False)
ax3.grid(alpha=0.3)


ax5.plot(stib_otp_x, stib_otp_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw)
ax5.plot(london_tube_otp_x, london_tube_otp_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw)
ax5.plot(new_york_mtabc_otp_x, new_york_mtabc_otp_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw)
ax5.plot(madrid_bus_otp_x, madrid_bus_otp_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw)
ax5.set_ylabel("cpu use (%)")
ax5.set_xscale("log")
ax5.set_xticks([1, 2, 5, 10, 20, 50])
ax5.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.set_yticks([0, 20, 40, 60, 80, 100])
ax5.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.spines["right"].set_visible(False)
ax5.spines["top"].set_visible(False)
ax5.grid(alpha=0.3)


ax7.plot(tec_otp_x, tec_otp_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw)
ax7.plot(delijn_otp_x, delijn_otp_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw)
ax7.plot(helsinki_hsl_otp_x, helsinki_hsl_otp_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw)
ax7.plot(chicago_cta_otp_x, chicago_cta_otp_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw)
ax7.set_xlabel("concurrent clients")
ax7.set_ylabel("cpu use (%)")
ax7.set_xscale("log")
ax7.set_xticks([1, 2, 5, 10, 20, 50])
ax7.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax7.set_yticks([0, 20, 40, 60, 80, 100])
ax7.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax7.spines["right"].set_visible(False)
ax7.spines["top"].set_visible(False)
ax7.grid(alpha=0.3)


ax2.plot(nl_waterbus_lc_x, nl_waterbus_lc_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw)
ax2.plot(sydney_trainlink_lc_x, sydney_trainlink_lc_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw)
ax2.plot(thailand_greenbus_lc_x, thailand_greenbus_lc_y, marker='o', markersize=3.5, label="Thailand-Greenbus", linewidth=lw)
ax2.plot(kobe_subway_lc_x, kobe_subway_lc_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw)
ax2.set_title("Linked Connections Server")
ax2.set_ylabel("cpu use (%)")
ax2.set_xscale("log")
ax2.set_xticks([1, 2, 5, 10, 20, 50])
ax2.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.set_yticks([0, 20, 40, 60, 80, 100])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax2.grid(alpha=0.3)


ax4.plot(nairobi_sacco_lc_x, nairobi_sacco_lc_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw)
ax4.plot(sf_bart_lc_x, sf_bart_lc_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw)
ax4.plot(amsterdam_gvb_lc_x, amsterdam_gvb_lc_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw)
ax4.plot(nmbs_lc_x, nmbs_lc_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw)
ax4.set_ylabel("cpu use (%)")
ax4.set_xscale("log")
ax4.set_xticks([1, 2, 5, 10, 20, 50])
ax4.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.set_yticks([0, 20, 40, 60, 80, 100])
ax4.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.spines["right"].set_visible(False)
ax4.spines["top"].set_visible(False)
ax4.grid(alpha=0.3)


ax6.plot(stib_lc_x, stib_lc_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw)
ax6.plot(london_tube_lc_x, london_tube_lc_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw)
ax6.plot(new_york_mtabc_lc_x, new_york_mtabc_lc_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw)
ax6.plot(madrid_bus_lc_x, madrid_bus_lc_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw)
ax6.set_ylabel("cpu use (%)")
ax6.set_xscale("log")
ax6.set_xticks([1, 2, 5, 10, 20, 50])
ax6.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.set_yticks([0, 20, 40, 60, 80, 100])
ax6.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.spines["right"].set_visible(False)
ax6.spines["top"].set_visible(False)
ax6.grid(alpha=0.3)


ax8.plot(tec_lc_x, tec_lc_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw)
ax8.plot(delijn_lc_x, delijn_lc_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw)
ax8.plot(helsinki_hsl_lc_x, helsinki_hsl_lc_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw)
ax8.plot(chicago_cta_lc_x, chicago_cta_lc_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw)
ax8.set_xlabel("concurrent clients")
ax8.set_ylabel("cpu use (%)")
ax8.set_xscale("log")
ax8.set_xticks([1, 2, 5, 10, 20, 50])
ax8.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax8.set_yticks([0, 20, 40, 60, 80, 100])
ax8.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax8.spines["right"].set_visible(False)
ax8.spines["top"].set_visible(False)
ax8.grid(alpha=0.3)


handles1, labels1 = ax1.get_legend_handles_labels()
handles3, labels3 = ax3.get_legend_handles_labels()
handles5, labels5 = ax5.get_legend_handles_labels()
handles7, labels7 = ax7.get_legend_handles_labels()

fig.legend(handles1, labels1, loc="upper right", ncol=1, handlelength=3)
fig.legend(handles3, labels3, loc="center left", ncol=1, handlelength=3)
fig.legend(handles5, labels5, loc="center right", ncol=1, handlelength=3)
fig.legend(handles7, labels7, loc="lower right", ncol=1, handlelength=3)

#fig.set_size_inches(25, 20)
#plt.savefig("/home/julian/Desktop/test.svg")

plt.show()