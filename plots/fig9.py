import matplotlib
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
from matplotlib import lines as mlines
import csv

# Function to calculate Y-axis (CPU) values of a transit network
def get_resource_usage(ptn, server, resource):
    root_path = "../scalability-test/server/results/" + ptn + "/" + server + "/"
    x = [1, 2, 5, 10, 20, 50]
    y = []
    res = 2 if resource == "cpu" else 3

    for i in x:
        with open(root_path + str(i) + ".csv", 'r') as csvfile:
            data = list(csv.reader(csvfile, delimiter=','))
            r = 0
            for index, d in enumerate(data):
                if(index > 0):
                    r += float(d[res])
            r = r / (len(data) - 1)
            y.append(r)

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
amsterdam_gvb_otp_cpu_x, amsterdam_gvb_otp_cpu_y = get_resource_usage("amsterdam-gvb", "otp", "cpu")
amsterdam_gvb_lc_cpu_x, amsterdam_gvb_lc_cpu_y = get_resource_usage("amsterdam-gvb", "lc_cache", "cpu")
amsterdam_gvb_otp_ram_x, amsterdam_gvb_otp_ram_y = get_resource_usage("amsterdam-gvb", "otp", "ram")
amsterdam_gvb_lc_ram_x, amsterdam_gvb_lc_ram_y = get_resource_usage("amsterdam-gvb", "lc_cache", "ram")

chicago_cta_otp_cpu_x, chicago_cta_otp_cpu_y = get_resource_usage("chicago-cta", "otp", "cpu")
chicago_cta_lc_cpu_x, chicago_cta_lc_cpu_y = get_resource_usage("chicago-cta", "lc_cache", "cpu")
chicago_cta_otp_ram_x, chicago_cta_otp_ram_y = get_resource_usage("chicago-cta", "otp", "ram")
chicago_cta_lc_ram_x, chicago_cta_lc_ram_y = get_resource_usage("chicago-cta", "lc_cache", "ram")

delijn_otp_cpu_x, delijn_otp_cpu_y = get_resource_usage("delijn", "otp", "cpu")
delijn_lc_cpu_x, delijn_lc_cpu_y = get_resource_usage("delijn", "lc_cache", "cpu")
delijn_otp_ram_x, delijn_otp_ram_y = get_resource_usage("delijn", "otp", "ram")
delijn_lc_ram_x, delijn_lc_ram_y = get_resource_usage("delijn", "lc_cache", "ram")

helsinki_hsl_otp_cpu_x, helsinki_hsl_otp_cpu_y = get_resource_usage("helsinki-hsl", "otp", "cpu")
helsinki_hsl_lc_cpu_x, helsinki_hsl_lc_cpu_y = get_resource_usage("helsinki-hsl", "lc_cache", "cpu")
helsinki_hsl_otp_ram_x, helsinki_hsl_otp_ram_y = get_resource_usage("helsinki-hsl", "otp", "ram")
helsinki_hsl_lc_ram_x, helsinki_hsl_lc_ram_y = get_resource_usage("helsinki-hsl", "lc_cache", "ram")

kobe_subway_otp_cpu_x, kobe_subway_otp_cpu_y = get_resource_usage("kobe-subway", "otp", "cpu")
kobe_subway_lc_cpu_x, kobe_subway_lc_cpu_y = get_resource_usage("kobe-subway", "lc_cache", "cpu")
kobe_subway_otp_ram_x, kobe_subway_otp_ram_y = get_resource_usage("kobe-subway", "otp", "ram")
kobe_subway_lc_ram_x, kobe_subway_lc_ram_y = get_resource_usage("kobe-subway", "lc_cache", "ram")

london_tube_otp_cpu_x, london_tube_otp_cpu_y = get_resource_usage("london-tube", "otp", "cpu")
london_tube_lc_cpu_x, london_tube_lc_cpu_y = get_resource_usage("london-tube", "lc_cache", "cpu")
london_tube_otp_ram_x, london_tube_otp_ram_y = get_resource_usage("london-tube", "otp", "ram")
london_tube_lc_ram_x, london_tube_lc_ram_y = get_resource_usage("london-tube", "lc_cache", "ram")

madrid_bus_otp_cpu_x, madrid_bus_otp_cpu_y = get_resource_usage("madrid-bus", "otp", "cpu")
madrid_bus_lc_cpu_x, madrid_bus_lc_cpu_y = get_resource_usage("madrid-bus", "lc_cache", "cpu")
madrid_bus_otp_ram_x, madrid_bus_otp_ram_y = get_resource_usage("madrid-bus", "otp", "ram")
madrid_bus_lc_ram_x, madrid_bus_lc_ram_y = get_resource_usage("madrid-bus", "lc_cache", "ram")

nairobi_sacco_otp_cpu_x, nairobi_sacco_otp_cpu_y = get_resource_usage("nairobi-sacco", "otp", "cpu")
nairobi_sacco_lc_cpu_x, nairobi_sacco_lc_cpu_y = get_resource_usage("nairobi-sacco", "lc_cache", "cpu")
nairobi_sacco_otp_ram_x, nairobi_sacco_otp_ram_y = get_resource_usage("nairobi-sacco", "otp", "ram")
nairobi_sacco_lc_ram_x, nairobi_sacco_lc_ram_y = get_resource_usage("nairobi-sacco", "lc_cache", "ram")

new_york_mtabc_otp_cpu_x, new_york_mtabc_otp_cpu_y = get_resource_usage("new-york-mtabc", "otp", "cpu")
new_york_mtabc_lc_cpu_x, new_york_mtabc_lc_cpu_y = get_resource_usage("new-york-mtabc", "lc_cache", "cpu")
new_york_mtabc_otp_ram_x, new_york_mtabc_otp_ram_y = get_resource_usage("new-york-mtabc", "otp", "ram")
new_york_mtabc_lc_ram_x, new_york_mtabc_lc_ram_y = get_resource_usage("new-york-mtabc", "lc_cache", "ram")

nl_waterbus_otp_cpu_x, nl_waterbus_otp_cpu_y = get_resource_usage("nl-waterbus", "otp", "cpu")
nl_waterbus_lc_cpu_x, nl_waterbus_lc_cpu_y = get_resource_usage("nl-waterbus", "lc_cache", "cpu")
nl_waterbus_otp_ram_x, nl_waterbus_otp_ram_y = get_resource_usage("nl-waterbus", "otp", "ram")
nl_waterbus_lc_ram_x, nl_waterbus_lc_ram_y = get_resource_usage("nl-waterbus", "lc_cache", "ram")

nmbs_otp_cpu_x, nmbs_otp_cpu_y = get_resource_usage("nmbs", "otp", "cpu")
nmbs_lc_cpu_x, nmbs_lc_cpu_y = get_resource_usage("nmbs", "lc_cache", "cpu")
nmbs_otp_ram_x, nmbs_otp_ram_y = get_resource_usage("nmbs", "otp", "ram")
nmbs_lc_ram_x, nmbs_lc_ram_y = get_resource_usage("nmbs", "lc_cache", "ram")

sf_bart_otp_cpu_x, sf_bart_otp_cpu_y = get_resource_usage("sf-bart", "otp", "cpu")
sf_bart_lc_cpu_x, sf_bart_lc_cpu_y = get_resource_usage("sf-bart", "lc_cache", "cpu")
sf_bart_otp_ram_x, sf_bart_otp_ram_y = get_resource_usage("sf-bart", "otp", "ram")
sf_bart_lc_ram_x, sf_bart_lc_ram_y = get_resource_usage("sf-bart", "lc_cache", "ram")

stib_otp_cpu_x, stib_otp_cpu_y = get_resource_usage("stib", "otp", "cpu")
stib_lc_cpu_x, stib_lc_cpu_y = get_resource_usage("stib", "lc_cache", "cpu")
stib_otp_ram_x, stib_otp_ram_y = get_resource_usage("stib", "otp", "ram")
stib_lc_ram_x, stib_lc_ram_y = get_resource_usage("stib", "lc_cache", "ram")

sydney_trainlink_otp_cpu_x, sydney_trainlink_otp_cpu_y = get_resource_usage("sydney-trainlink", "otp", "cpu")
sydney_trainlink_lc_cpu_x, sydney_trainlink_lc_cpu_y = get_resource_usage("sydney-trainlink", "lc_cache", "cpu")
sydney_trainlink_otp_ram_x, sydney_trainlink_otp_ram_y = get_resource_usage("sydney-trainlink", "otp", "ram")
sydney_trainlink_lc_ram_x, sydney_trainlink_lc_ram_y = get_resource_usage("sydney-trainlink", "lc_cache", "ram")

tec_otp_cpu_x, tec_otp_cpu_y = get_resource_usage("tec", "otp", "cpu")
tec_lc_cpu_x, tec_lc_cpu_y = get_resource_usage("tec", "lc_cache", "cpu")
tec_otp_ram_x, tec_otp_ram_y = get_resource_usage("tec", "otp", "ram")
tec_lc_ram_x, tec_lc_ram_y = get_resource_usage("tec", "lc_cache", "ram")

thailand_greenbus_otp_cpu_x, thailand_greenbus_otp_cpu_y = get_resource_usage("thailand-greenbus", "otp", "cpu")
thailand_greenbus_lc_cpu_x, thailand_greenbus_lc_cpu_y = get_resource_usage("thailand-greenbus", "lc_cache", "cpu")
thailand_greenbus_otp_ram_x, thailand_greenbus_otp_ram_y = get_resource_usage("thailand-greenbus", "otp", "ram")
thailand_greenbus_lc_ram_x, thailand_greenbus_lc_ram_y = get_resource_usage("thailand-greenbus", "lc_cache", "ram")

# Calculate NGINX average CPU usage per plot
#nginx1_x, nginx1_y = get_nginx_usage(['sydney-trainlink', 'thailand-greenbus', 'kobe-subway'])
#nginx2_x, nginx2_y = get_nginx_usage(['nairobi-sacco', 'sf-bart', 'amsterdam-gvb', 'nmbs'])
#nginx3_x, nginx3_y = get_nginx_usage(['stib', 'london-tube', 'new-york-mtabc', 'madrid-bus'])
#nginx4_x, nginx4_y = get_nginx_usage(['tec', 'delijn', 'chicago-cta', 'helsinki-hsl'])

# Create subplots
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(nrows=4, ncols=2)
lw = 3

colors = ['#556b2f', '#7f0000', '#483d8b', 
    '#3cb371', '#b8860b', '#008b8b', 
    '#9acd32', '#00008b', '#ff4500', 
    '#ffd700', '#7fff00', '#ba55d3', 
    '#00ff7f', '#00ffff', '#0000ff', 
    '#ff00ff', '#1e90ff', '#eee8aa', 
    '#dda0dd', '#ff1493', '#ffa07a', '#87cefa']

ax1.plot(nl_waterbus_lc_cpu_x, nl_waterbus_lc_cpu_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw, color=colors[0])
ax1.plot(kobe_subway_lc_cpu_x, kobe_subway_lc_cpu_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw, color=colors[1])
ax1.plot(sydney_trainlink_lc_cpu_x, sydney_trainlink_lc_cpu_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw, color=colors[2])
ax1.plot(thailand_greenbus_lc_cpu_x, thailand_greenbus_lc_cpu_y, marker='o', markersize=3.5, label="Thailand-Greenbus", linewidth=lw, color=colors[4])
ax1.plot(nl_waterbus_otp_cpu_x, nl_waterbus_otp_cpu_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw, linestyle="dotted", color=colors[0])
ax1.plot(kobe_subway_otp_cpu_x, kobe_subway_otp_cpu_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw, linestyle="dotted", color=colors[1])
ax1.plot(sydney_trainlink_otp_cpu_x, sydney_trainlink_otp_cpu_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw, linestyle="dotted", color=colors[2])
ax1.plot(thailand_greenbus_otp_cpu_x, thailand_greenbus_otp_cpu_y, marker='o', markersize=3.5, label="Thailand-Greenbus", linewidth=lw, linestyle="dotted", color=colors[4])
ax1.set_title("CPU use")
ax1.set_ylabel("cpu use (%)")
ax1.set_xscale("log")
ax1.set_xticks([1, 2, 5, 10, 20, 50])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_yticks([0, 10, 20, 40, 70])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)
ax1.grid(alpha=0.3)

ax3.plot(nairobi_sacco_lc_cpu_x, nairobi_sacco_lc_cpu_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw, color=colors[10])
ax3.plot(sf_bart_lc_cpu_x, sf_bart_lc_cpu_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw, color=colors[3])
ax3.plot(amsterdam_gvb_lc_cpu_x, amsterdam_gvb_lc_cpu_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw, color=colors[13])
ax3.plot(nmbs_lc_cpu_x, nmbs_lc_cpu_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw, color=colors[8])
ax3.plot(nairobi_sacco_otp_cpu_x, nairobi_sacco_otp_cpu_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw, linestyle="dotted", color=colors[10])
ax3.plot(sf_bart_otp_cpu_x, sf_bart_otp_cpu_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw, linestyle="dotted", color=colors[3])
ax3.plot(amsterdam_gvb_otp_cpu_x, amsterdam_gvb_otp_cpu_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw, linestyle="dotted", color=colors[13])
ax3.plot(nmbs_otp_cpu_x, nmbs_otp_cpu_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw, linestyle="dotted", color=colors[8])
ax3.set_ylabel("cpu use (%)")
ax3.set_xscale("log")
ax3.set_xticks([1, 2, 5, 10, 20, 50])
ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.set_yticks([0, 20, 40, 60, 80, 100])
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.spines["right"].set_visible(False)
ax3.spines["top"].set_visible(False)
ax3.grid(alpha=0.3)

ax5.plot(stib_lc_cpu_x, stib_lc_cpu_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw, color=colors[14])
ax5.plot(london_tube_lc_cpu_x, london_tube_lc_cpu_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw, color=colors[9])
ax5.plot(new_york_mtabc_lc_cpu_x, new_york_mtabc_lc_cpu_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw, color=colors[15])
ax5.plot(madrid_bus_lc_cpu_x, madrid_bus_lc_cpu_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw, color=colors[16])
ax5.plot(stib_otp_cpu_x, stib_otp_cpu_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw, linestyle="dotted", color=colors[14])
ax5.plot(london_tube_otp_cpu_x, london_tube_otp_cpu_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw, linestyle="dotted", color=colors[9])
ax5.plot(new_york_mtabc_otp_cpu_x, new_york_mtabc_otp_cpu_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw, linestyle="dotted", color=colors[15])
ax5.plot(madrid_bus_otp_cpu_x, madrid_bus_otp_cpu_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw, linestyle="dotted", color=colors[16])
ax5.set_ylabel("cpu use (%)")
ax5.set_xscale("log")
ax5.set_xticks([1, 2, 5, 10, 20, 50])
ax5.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.set_yticks([0, 20, 40, 60, 80, 100])
ax5.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.spines["right"].set_visible(False)
ax5.spines["top"].set_visible(False)
ax5.grid(alpha=0.3)

ax7.plot(tec_lc_cpu_x, tec_lc_cpu_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw, color=colors[19])
ax7.plot(delijn_lc_cpu_x, delijn_lc_cpu_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw, color=colors[21])
ax7.plot(helsinki_hsl_lc_cpu_x, helsinki_hsl_lc_cpu_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw, color=colors[17])
ax7.plot(chicago_cta_lc_cpu_x, chicago_cta_lc_cpu_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw, color=colors[20])
ax7.plot(tec_otp_cpu_x, tec_otp_cpu_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw, linestyle="dotted", color=colors[19])
ax7.plot(delijn_otp_cpu_x, delijn_otp_cpu_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw, linestyle="dotted", color=colors[21])
ax7.plot(helsinki_hsl_otp_cpu_x, helsinki_hsl_otp_cpu_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw, linestyle="dotted", color=colors[17])
ax7.plot(chicago_cta_otp_cpu_x, chicago_cta_otp_cpu_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw, linestyle="dotted", color=colors[20])
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


ax2.plot(nl_waterbus_lc_ram_x, nl_waterbus_lc_ram_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw, color=colors[0])
ax2.plot(kobe_subway_lc_ram_x, kobe_subway_lc_ram_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw, color=colors[1])
ax2.plot(sydney_trainlink_lc_ram_x, sydney_trainlink_lc_ram_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw, color=colors[2])
ax2.plot(thailand_greenbus_lc_ram_x, thailand_greenbus_lc_ram_y, marker='o', markersize=3.5, label="Thailand-Greenbus", linewidth=lw, color=colors[4])
ax2.plot(nl_waterbus_otp_ram_x, nl_waterbus_otp_ram_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw, linestyle="dotted", color=colors[0])
ax2.plot(kobe_subway_otp_ram_x, kobe_subway_otp_ram_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw, linestyle="dotted", color=colors[1])
ax2.plot(sydney_trainlink_otp_ram_x, sydney_trainlink_otp_ram_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw, linestyle="dotted", color=colors[2])
ax2.plot(thailand_greenbus_otp_ram_x, thailand_greenbus_otp_ram_y, marker='o', markersize=3.5, label="Thailand-Greenbus", linewidth=lw, linestyle="dotted", color=colors[4])
ax2.set_title("RAM use")
ax2.set_ylabel("ram use (%)")
ax2.set_xscale("log")
ax2.set_xticks([1, 2, 5, 10, 20, 50])
ax2.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.set_yticks([0, 20, 40, 60, 80])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax2.grid(alpha=0.3)


ax4.plot(nairobi_sacco_lc_ram_x, nairobi_sacco_lc_ram_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw, color=colors[10])
ax4.plot(sf_bart_lc_ram_x, sf_bart_lc_ram_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw, color=colors[3])
ax4.plot(amsterdam_gvb_lc_ram_x, amsterdam_gvb_lc_ram_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw, color=colors[13])
ax4.plot(nmbs_lc_ram_x, nmbs_lc_ram_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw, color=colors[8])
ax4.plot(nairobi_sacco_otp_ram_x, nairobi_sacco_otp_ram_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw, linestyle="dotted", color=colors[10])
ax4.plot(sf_bart_otp_ram_x, sf_bart_otp_ram_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw, linestyle="dotted", color=colors[3])
ax4.plot(amsterdam_gvb_otp_ram_x, amsterdam_gvb_otp_ram_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw, linestyle="dotted", color=colors[13])
ax4.plot(nmbs_otp_ram_x, nmbs_otp_ram_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw, linestyle="dotted", color=colors[8])
ax4.set_ylabel("ram use (%)")
ax4.set_xscale("log")
ax4.set_xticks([1, 2, 5, 10, 20, 50])
ax4.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.set_yticks([0, 20, 40, 60, 80])
ax4.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.spines["right"].set_visible(False)
ax4.spines["top"].set_visible(False)
ax4.grid(alpha=0.3)


ax6.plot(stib_lc_ram_x, stib_lc_ram_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw, color=colors[14])
ax6.plot(london_tube_lc_ram_x, london_tube_lc_ram_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw, color=colors[9])
ax6.plot(new_york_mtabc_lc_ram_x, new_york_mtabc_lc_ram_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw, color=colors[15])
ax6.plot(madrid_bus_lc_ram_x, madrid_bus_lc_ram_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw, color=colors[16])
ax6.plot(stib_otp_ram_x, stib_otp_ram_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw, linestyle="dotted", color=colors[14])
ax6.plot(london_tube_otp_ram_x, london_tube_otp_ram_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw, linestyle="dotted", color=colors[9])
ax6.plot(new_york_mtabc_otp_ram_x, new_york_mtabc_otp_ram_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw, linestyle="dotted", color=colors[15])
ax6.plot(madrid_bus_otp_ram_x, madrid_bus_otp_ram_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw, linestyle="dotted", color=colors[16])
ax6.set_ylabel("ram use (%)")
ax6.set_xscale("log")
ax6.set_xticks([1, 2, 5, 10, 20, 50])
ax6.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.set_yticks([0, 20, 40, 60])
ax6.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.spines["right"].set_visible(False)
ax6.spines["top"].set_visible(False)
ax6.grid(alpha=0.3)


ax8.plot(tec_lc_ram_x, tec_lc_ram_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw, color=colors[19])
ax8.plot(delijn_lc_ram_x, delijn_lc_ram_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw, color=colors[21])
ax8.plot(helsinki_hsl_lc_ram_x, helsinki_hsl_lc_ram_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw, color=colors[17])
ax8.plot(chicago_cta_lc_ram_x, chicago_cta_lc_ram_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw, color=colors[20])
ax8.plot(tec_otp_ram_x, tec_otp_ram_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw, linestyle="dotted", color=colors[19])
ax8.plot(delijn_otp_ram_x, delijn_otp_ram_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw, linestyle="dotted", color=colors[21])
ax8.plot(helsinki_hsl_otp_ram_x, helsinki_hsl_otp_ram_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw, linestyle="dotted", color=colors[17])
ax8.plot(chicago_cta_otp_ram_x, chicago_cta_otp_ram_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw, linestyle="dotted", color=colors[20])
ax8.set_xlabel("concurrent clients")
ax8.set_ylabel("ram use (%)")
ax8.set_xscale("log")
ax8.set_xticks([1, 2, 5, 10, 20, 50])
ax8.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax8.set_yticks([0, 20, 40, 60, 80])
ax8.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax8.spines["right"].set_visible(False)
ax8.spines["top"].set_visible(False)
ax8.grid(alpha=0.3)


handles1, labels1 = ax1.get_legend_handles_labels()
handles3, labels3 = ax3.get_legend_handles_labels()
handles5, labels5 = ax5.get_legend_handles_labels()
handles7, labels7 = ax7.get_legend_handles_labels()

ax1_handles = [mpatches.Patch(color=colors[0]), mpatches.Patch(color=colors[1]), 
    mpatches.Patch(color=colors[2]), mpatches.Patch(color=colors[4])]

ax3_handles = [mpatches.Patch(color=colors[10]), mpatches.Patch(color=colors[3]), 
    mpatches.Patch(color=colors[13]), mpatches.Patch(color=colors[8])]

ax5_handles = [mpatches.Patch(color=colors[14]), mpatches.Patch(color=colors[9]), 
    mpatches.Patch(color=colors[15]), mpatches.Patch(color=colors[16])]

ax7_handles = [mpatches.Patch(color=colors[19]), mpatches.Patch(color=colors[21]), 
    mpatches.Patch(color=colors[17]), mpatches.Patch(color=colors[20])]

general_handles = [mlines.Line2D([], [], color='black', linewidth=2, linestyle='dotted', marker='o', markersize=3.5, label='OpenTripPlanner'),
    mlines.Line2D([], [], color='black', linewidth=2, linestyle='solid', marker='o', markersize=3.5, label='Linked Connections Server')]

fig.legend(ax1_handles, labels1[:4], loc="upper right", ncol=1, handlelength=3)
fig.legend(ax3_handles, labels3[:4], loc="center left", ncol=1, handlelength=3)
fig.legend(ax5_handles, labels5[:4], loc="center right", ncol=1, handlelength=3)
fig.legend(ax7_handles, labels7[:4], loc="lower right", ncol=1, handlelength=3)

fig.legend(handles=general_handles, loc="lower center", ncol=2)

plt.show()