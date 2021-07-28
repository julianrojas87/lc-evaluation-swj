import matplotlib
from matplotlib import pyplot as plt
import json

# Function to calculate Y-axis (average response time) values of a transit network
def get_response_time(ptn, server):
    root_path = "../scalability-test/client/results/" + ptn + "/report-" + server + ".json"
    cc = [1, 2, 5, 10, 20, 50]
    x = []
    y = []
    # Opening JSON file
    data = json.load(open(root_path))

    for i, d in enumerate(data):
        if(i < 6):
            if(server == 'otp'):
                if(d['latency']['average'] > 0):
                    x.append(cc[i])
                    y.append(d['latency']['average'])
            else:
                if(d['averageResponseTime'] > 0):
                    x.append(cc[i])
                    y.append(d['averageResponseTime'])
    return x, y

# Get X and Y axises for each public transport network
amsterdam_gvb_otp_x, amsterdam_gvb_otp_y = get_response_time("amsterdam-gvb", "otp")
amsterdam_gvb_lc_x, amsterdam_gvb_lc_y = get_response_time("amsterdam-gvb", "lc_cache")

chicago_cta_otp_x, chicago_cta_otp_y = get_response_time("chicago-cta", "otp")
chicago_cta_lc_x, chicago_cta_lc_y = get_response_time("chicago-cta", "lc_cache")

delijn_otp_x, delijn_otp_y = get_response_time("delijn", "otp")
delijn_lc_x, delijn_lc_y = get_response_time("delijn", "lc_cache")

helsinki_hsl_otp_x, helsinki_hsl_otp_y = get_response_time("helsinki-hsl", "otp")
helsinki_hsl_lc_x, helsinki_hsl_lc_y = get_response_time("helsinki-hsl", "lc_cache")

kobe_subway_otp_x, kobe_subway_otp_y = get_response_time("kobe-subway", "otp")
kobe_subway_lc_x, kobe_subway_lc_y = get_response_time("kobe-subway", "lc_cache")

london_tube_otp_x, london_tube_otp_y = get_response_time("london-tube", "otp")
london_tube_lc_x, london_tube_lc_y = get_response_time("london-tube", "lc_cache")

madrid_bus_otp_x, madrid_bus_otp_y = get_response_time("madrid-bus", "otp")
madrid_bus_lc_x, madrid_bus_lc_y = get_response_time("madrid-bus", "lc_cache")

nairobi_sacco_otp_x, nairobi_sacco_otp_y = get_response_time("nairobi-sacco", "otp")
nairobi_sacco_lc_x, nairobi_sacco_lc_y = get_response_time("nairobi-sacco", "lc_cache")

new_york_mtabc_otp_x, new_york_mtabc_otp_y = get_response_time("new-york-mtabc", "otp")
new_york_mtabc_lc_x, new_york_mtabc_lc_y = get_response_time("new-york-mtabc", "lc_cache")

nl_waterbus_otp_x, nl_waterbus_otp_y = get_response_time("nl-waterbus", "otp")
nl_waterbus_lc_x, nl_waterbus_lc_y = get_response_time("nl-waterbus", "lc_cache")

nmbs_otp_x, nmbs_otp_y = get_response_time("nmbs", "otp")
nmbs_lc_x, nmbs_lc_y = get_response_time("nmbs", "lc_cache")

sf_bart_otp_x, sf_bart_otp_y = get_response_time("sf-bart", "otp")
sf_bart_lc_x, sf_bart_lc_y = get_response_time("sf-bart", "lc_cache")

stib_otp_x, stib_otp_y = get_response_time("stib", "otp")
stib_lc_x, stib_lc_y = get_response_time("stib", "lc_cache")

sydney_trainlink_otp_x, sydney_trainlink_otp_y = get_response_time("sydney-trainlink", "otp")
sydney_trainlink_lc_x, sydney_trainlink_lc_y = get_response_time("sydney-trainlink", "lc_cache")

tec_otp_x, tec_otp_y = get_response_time("tec", "otp")
tec_lc_x, tec_lc_y = get_response_time("tec", "lc_cache")

thailand_greenbus_otp_x, thailand_greenbus_otp_y = get_response_time("thailand-greenbus", "otp")
thailand_greenbus_lc_x, thailand_greenbus_lc_y = get_response_time("thailand-greenbus", "lc_cache")

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

ax1.plot(nl_waterbus_otp_x, nl_waterbus_otp_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw, color=colors[0])
ax1.plot(sydney_trainlink_otp_x, sydney_trainlink_otp_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw, color=colors[2])
ax1.plot(thailand_greenbus_otp_x, thailand_greenbus_otp_y, marker='o', markersize=3.5, label="Thailand-Greenbus", linewidth=lw, color=colors[4])
ax1.plot(kobe_subway_otp_x, kobe_subway_otp_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw, color=colors[1])
ax1.set_title("OpenTripPlanner Server")
ax1.set_ylabel("average response time (ms)")
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_xticks([1, 2, 5, 10, 20, 50])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_yticks([20, 100, 200, 500, 1000, 2000])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)
ax1.grid(alpha=0.3)


ax3.plot(nairobi_sacco_otp_x, nairobi_sacco_otp_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw, color=colors[10])
ax3.plot(sf_bart_otp_x, sf_bart_otp_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw, color=colors[3])
ax3.plot(amsterdam_gvb_otp_x, amsterdam_gvb_otp_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw, color=colors[13])
ax3.plot(nmbs_otp_x, nmbs_otp_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw, color=colors[8])
ax3.set_ylabel("average response time (ms)")
ax3.set_xscale("log")
ax3.set_yscale("log")
ax3.set_xticks([1, 2, 5, 10, 20, 50])
ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.set_yticks([50, 100, 500, 1000, 3000, 7000])
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.spines["right"].set_visible(False)
ax3.spines["top"].set_visible(False)
ax3.grid(alpha=0.3)


ax5.plot(stib_otp_x, stib_otp_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw, color=colors[14])
ax5.plot(london_tube_otp_x, london_tube_otp_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw, color=colors[9])
ax5.plot(new_york_mtabc_otp_x, new_york_mtabc_otp_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw, color=colors[15])
ax5.plot(madrid_bus_otp_x, madrid_bus_otp_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw, color=colors[16])
ax5.set_ylabel("average response time (ms)")
ax5.set_xscale("log")
ax5.set_yscale("log")
ax5.set_xticks([1, 2, 5, 10, 20, 50])
ax5.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.set_yticks([200, 500, 1500, 3000, 8000, 20000])
ax5.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.spines["right"].set_visible(False)
ax5.spines["top"].set_visible(False)
ax5.grid(alpha=0.3)


ax7.plot(tec_otp_x, tec_otp_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw, color=colors[19])
ax7.plot(delijn_otp_x, delijn_otp_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw, color=colors[21])
ax7.plot(helsinki_hsl_otp_x, helsinki_hsl_otp_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw, color=colors[17])
ax7.plot(chicago_cta_otp_x, chicago_cta_otp_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw, color=colors[20])
ax7.set_xlabel("concurrent clients")
ax7.set_ylabel("average response time (ms)")
ax7.set_xscale("log")
ax7.set_yscale("log")
ax7.set_xticks([1, 2, 5, 10, 20, 50])
ax7.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax7.set_yticks([500, 1500, 3000, 10000, 30000, 60000])
ax7.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax7.spines["right"].set_visible(False)
ax7.spines["top"].set_visible(False)
ax7.grid(alpha=0.3)

ax2.plot(nl_waterbus_lc_x, nl_waterbus_lc_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw, color=colors[0])
ax2.plot(sydney_trainlink_lc_x, sydney_trainlink_lc_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw, color=colors[2])
ax2.plot(thailand_greenbus_lc_x, thailand_greenbus_lc_y, marker='o', markersize=3.5, label="Thailand-Greenbus", linewidth=lw, color=colors[4])
ax2.plot(kobe_subway_lc_x, kobe_subway_lc_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw, color=colors[1])
ax2.set_title("Linked Connections Server")
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xticks([1, 2, 5, 10, 20, 50])
ax2.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.set_yticks([20, 100, 200, 500, 1000, 2000])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax2.grid(alpha=0.3)

ax4.plot(nairobi_sacco_lc_x, nairobi_sacco_lc_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw, color=colors[10])
ax4.plot(sf_bart_lc_x, sf_bart_lc_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw, color=colors[3])
ax4.plot(amsterdam_gvb_lc_x, amsterdam_gvb_lc_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw, color=colors[13])
ax4.plot(nmbs_lc_x, nmbs_lc_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw, color=colors[8])
ax4.set_xscale("log")
ax4.set_yscale("log")
ax4.set_xticks([1, 2, 5, 10, 20, 50])
ax4.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.set_yticks([50, 100, 500, 1000, 3000, 7000])
ax4.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.spines["right"].set_visible(False)
ax4.spines["top"].set_visible(False)
ax4.grid(alpha=0.3)

ax6.plot(stib_lc_x, stib_lc_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw, color=colors[14])
ax6.plot(london_tube_lc_x, london_tube_lc_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw, color=colors[9])
ax6.plot(new_york_mtabc_lc_x, new_york_mtabc_lc_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw, color=colors[15])
ax6.plot(madrid_bus_lc_x, madrid_bus_lc_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw, color=colors[16])
ax6.set_xscale("log")
ax6.set_yscale("log")
ax6.set_xticks([1, 2, 5, 10, 20, 50])
ax6.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.set_yticks([200, 500, 1500, 3000, 8000, 20000])
ax6.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.spines["right"].set_visible(False)
ax6.spines["top"].set_visible(False)
ax6.grid(alpha=0.3)

ax8.plot(tec_lc_x, tec_lc_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw, color=colors[19])
ax8.plot(delijn_lc_x, delijn_lc_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw, color=colors[21])
ax8.plot(helsinki_hsl_lc_x, helsinki_hsl_lc_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw, color=colors[17])
ax8.plot(chicago_cta_lc_x, chicago_cta_lc_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw, color=colors[20])
ax8.set_xlabel("concurrent clients")
ax8.set_xscale("log")
ax8.set_yscale("log")
ax8.set_xticks([1, 2, 5, 10, 20, 50])
ax8.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax8.set_yticks([500, 1500, 3000, 10000, 30000, 60000])
ax8.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax8.spines["right"].set_visible(False)
ax8.spines["top"].set_visible(False)
ax8.grid(alpha=0.3)

handles1, labels1 = ax1.get_legend_handles_labels()
handles3, labels3 = ax3.get_legend_handles_labels()
handles5, labels5 = ax5.get_legend_handles_labels()
handles7, labels7 = ax7.get_legend_handles_labels()

fig.legend(handles1, labels1, loc="upper right", ncol=1)
fig.legend(handles3, labels3, loc="center left", ncol=1)
fig.legend(handles5, labels5, loc="center right", ncol=1)
fig.legend(handles7, labels7, loc="lower right", ncol=1)

plt.show()
