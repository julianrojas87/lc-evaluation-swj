import matplotlib.pyplot as plt
import csv

# Function to extract measures from csv files
def retrieve_data(ptn, measure):
    root_path = "/home/julian/Desktop/lc-evaluation/results/"
    x = []
    y = []

    with open(root_path + ptn + "/results.csv", 'r') as csvfile:
        data = list(csv.reader(csvfile, delimiter=','))
        for row in data:
            if row[1] == measure:
                for i in range(len(row)):
                    if i > 1 & i % 2 == 0:
                        x.append(float(row[i]))
                    if i > 1 & i % 2 != 0:
                        y.append(float(row[i]))

                return x, y

def get_min_value(x, y):
    return (x[y.index(min(y))], min(y))


#plot_type = "average_response_time"
#plot_type = "response_time_p10"
#plot_type = "response_time_p50"
#plot_type = "response_time_p75"
#plot_type = "response_time_p90"

#plot_type = "average_connection_response_time"
plot_type = "connection_response_time_p90"


# Get X and Y axises for each public transport network and min value point
amsterdam_gvb_x, amsterdam_gvb_y = retrieve_data("amsterdam-gvb", plot_type)
amsterdam_gvb_min = get_min_value(amsterdam_gvb_x, amsterdam_gvb_y)

auckland_waiheke_x, auckland_waiheke_y = retrieve_data("auckland-waiheke", plot_type)
auckland_waiheke_min = get_min_value(auckland_waiheke_x, auckland_waiheke_y)

chicago_cta_x, chicago_cta_y = retrieve_data("chicago-cta", plot_type)
chicago_cta_min = get_min_value(chicago_cta_x, chicago_cta_y)

delijn_x, delijn_y = retrieve_data("delijn", plot_type)
delijn_min = get_min_value(delijn_x, delijn_y)

deutsche_bahn_x, deutsche_bahn_y = retrieve_data("deutsche-bahn", plot_type)
deutsche_bahn_min = get_min_value(deutsche_bahn_x, deutsche_bahn_y)

flixbus_x, flixbus_y = retrieve_data("flixbus", plot_type)
flixbus_min = get_min_value(flixbus_x, flixbus_y)

helsinki_hsl_x, helsinki_hsl_y = retrieve_data("helsinki-hsl", plot_type)
helsinki_hsl_min = get_min_value(helsinki_hsl_x, helsinki_hsl_y)

kobe_subway_x, kobe_subway_y = retrieve_data("kobe-subway", plot_type)
kobe_subway_min = get_min_value(kobe_subway_x, kobe_subway_y)

london_tube_x, london_tube_y = retrieve_data("london-tube", plot_type)
london_tube_min = get_min_value(london_tube_x, london_tube_y)

madrid_bus_x, madrid_bus_y = retrieve_data("madrid-bus", plot_type)
madrid_bus_min = get_min_value(madrid_bus_x, madrid_bus_y)

nairobi_sacco_x, nairobi_sacco_y = retrieve_data("nairobi-sacco", plot_type)
nairobi_sacco_min = get_min_value(nairobi_sacco_x, nairobi_sacco_y)

new_york_mtabc_x, new_york_mtabc_y = retrieve_data("new-york-mtabc", plot_type)
new_york_mtabc_min = get_min_value(new_york_mtabc_x, new_york_mtabc_y)

nl_waterbus_x, nl_waterbus_y = retrieve_data("nl-waterbus", plot_type)
nl_waterbus_min = get_min_value(nl_waterbus_x, nl_waterbus_y)

nmbs_x, nmbs_y = retrieve_data("nmbs", plot_type)
nmbs_min = get_min_value(nmbs_x, nmbs_y)

nz_bus_x, nz_bus_y = retrieve_data("nz-bus", plot_type)
nz_bus_min = get_min_value(nz_bus_x, nz_bus_y)

renfe_x, renfe_y = retrieve_data("renfe", plot_type)
renfe_min = get_min_value(renfe_x, renfe_y)

san_francisco_bart_x, san_francisco_bart_y = retrieve_data("sf-bart", plot_type)
san_francisco_bart_min = get_min_value(san_francisco_bart_x, san_francisco_bart_y)

sncf_x, sncf_y = retrieve_data("sncf", plot_type)
sncf_min = get_min_value(sncf_x, sncf_y)

stib_x, stib_y = retrieve_data("stib", plot_type)
stib_min = get_min_value(stib_x, stib_y)

sydney_trainlink_x, sydney_trainlink_y = retrieve_data("sydney-trainlink", plot_type)
sydney_trainlink_min = get_min_value(sydney_trainlink_x, sydney_trainlink_y)

tec_x, tec_y = retrieve_data("tec", plot_type)
tec_min = get_min_value(tec_x, tec_y)

thailand_greenbus_x, thailand_greenbus_y = retrieve_data("thailand-greenbus", plot_type)
thailand_greenbus_min = get_min_value(thailand_greenbus_x, thailand_greenbus_y)

# Create subplots
plt.style.use('seaborn-darkgrid')
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle('Response Time per Connection vs LC fragment size', fontsize=26)
lw = 2

ax1.plot(nl_waterbus_x, nl_waterbus_y, marker='o', markersize=3.5, label="Netherlands-Waterbus", linewidth=lw)
ax1.annotate(str(int(nl_waterbus_min[0])) + "," + str("{:.3f}".format(nl_waterbus_min[1])), 
    xy=nl_waterbus_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax1.get_lines()[len(ax1.get_lines()) - 1].get_color())
ax1.plot(sydney_trainlink_x, sydney_trainlink_y, marker='o', markersize=3.5, label="Sydney-Trainlink", linewidth=lw)
ax1.annotate(str(int(sydney_trainlink_min[0])) + "," + str("{:.3f}".format(sydney_trainlink_min[1])), 
    xy=sydney_trainlink_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax1.get_lines()[len(ax1.get_lines()) - 1].get_color())
ax1.plot(thailand_greenbus_x, thailand_greenbus_y, marker='o', markersize=3.5, label="Thailand-GreenBus", linewidth=lw)
ax1.annotate(str(int(thailand_greenbus_min[0])) + "," + str("{:.3f}".format(thailand_greenbus_min[1])), 
    xy=thailand_greenbus_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax1.get_lines()[len(ax1.get_lines()) - 1].get_color())
ax1.legend(loc="upper right")
ax1.set_xlabel("fragment size (connections)")
ax1.set_ylabel("response time (ms) / connection")

ax2.plot(kobe_subway_x, kobe_subway_y, marker='o', markersize=3.5, label="Kobe-Subway", linewidth=lw)
ax2.annotate(str(int(kobe_subway_min[0])) + "," + str("{:.3f}".format(kobe_subway_min[1])), 
    xy=kobe_subway_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax2.get_lines()[len(ax2.get_lines()) - 1].get_color())
ax2.plot(deutsche_bahn_x, deutsche_bahn_y, marker='o', markersize=3.5, label="Germany-DB")
ax2.annotate(str(int(deutsche_bahn_min[0])) + "," + str("{:.3f}".format(deutsche_bahn_min[1])), 
    xy=deutsche_bahn_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax2.get_lines()[len(ax2.get_lines()) - 1].get_color())
ax2.plot(renfe_x, renfe_y, marker='o', markersize=3.5, label="Spain-RENFE", linewidth=lw)
ax2.annotate(str(int(renfe_min[0])) + "," + str("{:.3f}".format(renfe_min[1])), 
    xy=renfe_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax2.get_lines()[len(ax2.get_lines()) - 1].get_color())
ax2.plot(auckland_waiheke_x, auckland_waiheke_y, marker='o', markersize=3.5, label="Auckland-Waiheke", linewidth=lw)
ax2.annotate(str(int(auckland_waiheke_min[0])) + "," + str("{:.3f}".format(auckland_waiheke_min[1])), 
    xy=auckland_waiheke_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax2.get_lines()[len(ax2.get_lines()) - 1].get_color())
ax2.plot(nairobi_sacco_x, nairobi_sacco_y, marker='o', markersize=3.5, label="Nairobi-SACCO", linewidth=lw)
ax2.annotate(str(int(nairobi_sacco_min[0])) + "," + str("{:.3f}".format(nairobi_sacco_min[1])), 
    xy=nairobi_sacco_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax2.get_lines()[len(ax2.get_lines()) - 1].get_color())
ax2.plot(san_francisco_bart_x, san_francisco_bart_y, marker='o', markersize=3.5, label="San Francisco-BART", linewidth=lw)
ax2.annotate(str(int(san_francisco_bart_min[0])) + "," + str("{:.3f}".format(san_francisco_bart_min[1])), 
    xy=san_francisco_bart_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax2.get_lines()[len(ax2.get_lines()) - 1].get_color())
ax2.legend(loc="upper left")
ax2.set_xlabel("fragment size (connections)")
ax2.set_ylabel("response time (ms) / connection")

ax3.plot(amsterdam_gvb_x, amsterdam_gvb_y, marker='o', markersize=3.5, label="Amsterdam-GVB", linewidth=lw)
ax3.annotate(str(int(amsterdam_gvb_min[0])) + "," + str("{:.3f}".format(amsterdam_gvb_min[1])), 
    xy=amsterdam_gvb_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax3.get_lines()[len(ax3.get_lines()) - 1].get_color())
ax3.plot(nmbs_x, nmbs_y, marker='o', markersize=3.5, label="Belgium-NMBS", linewidth=lw)
ax3.annotate(str(int(nmbs_min[0])) + "," + str("{:.3f}".format(nmbs_min[1])), 
    xy=nmbs_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax3.get_lines()[len(ax3.get_lines()) - 1].get_color())
ax3.plot(sncf_x, sncf_y, marker='o', markersize=3.5, label="France-SNCF", linewidth=lw)
ax3.annotate(str(int(sncf_min[0])) + "," + str("{:.3f}".format(sncf_min[1])), 
    xy=sncf_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax3.get_lines()[len(ax3.get_lines()) - 1].get_color())
ax3.plot(stib_x, stib_y, marker='o', markersize=3.5, label="Brussels-STIB", linewidth=lw)
ax3.annotate(str(int(stib_min[0])) + "," + str("{:.3f}".format(stib_min[1])), 
    xy=stib_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax3.get_lines()[len(ax3.get_lines()) - 1].get_color())
ax3.plot(london_tube_x, london_tube_y, marker='o', markersize=3.5, label="London-Tube", linewidth=lw)
ax3.annotate(str(int(london_tube_min[0])) + "," + str("{:.3f}".format(london_tube_min[1])), 
    xy=london_tube_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax3.get_lines()[len(ax3.get_lines()) - 1].get_color())
ax3.plot(flixbus_x, flixbus_y, marker='o', markersize=3.5, label="EU-Flixbus", linewidth=lw)
ax3.annotate(str(int(flixbus_min[0])) + "," + str("{:.3f}".format(flixbus_min[1])), 
    xy=flixbus_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax3.get_lines()[len(ax3.get_lines()) - 1].get_color())
ax3.legend(loc="upper left")
ax3.set_xlabel("fragment size (connections)")
ax3.set_ylabel("response time (ms) / connection")

ax4.plot(new_york_mtabc_x, new_york_mtabc_y, marker='o', markersize=3.5, label="New York-MTABC", linewidth=lw)
ax4.annotate(str(int(new_york_mtabc_min[0])) + "," + str("{:.3f}".format(new_york_mtabc_min[1])), 
    xy=new_york_mtabc_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax4.get_lines()[len(ax4.get_lines()) - 1].get_color())
ax4.plot(madrid_bus_x, madrid_bus_y, marker='o', markersize=3.5, label="Madrid-CRTM", linewidth=lw)
ax4.annotate(str(int(madrid_bus_min[0])) + "," + str("{:.3f}".format(madrid_bus_min[1])), 
    xy=madrid_bus_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax4.get_lines()[len(ax4.get_lines()) - 1].get_color())
ax4.plot(tec_x, tec_y, marker='o', markersize=3.5, label="Wallonia-TEC", linewidth=lw)
ax4.annotate(str(int(tec_min[0])) + "," + str("{:.3f}".format(tec_min[1])), 
    xy=tec_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax4.get_lines()[len(ax4.get_lines()) - 1].get_color())
ax4.plot(delijn_x, delijn_y, marker='o', markersize=3.5, label="Flanders-De Lijn", linewidth=lw)
ax4.annotate(str(int(delijn_min[0])) + "," + str("{:.3f}".format(delijn_min[1])), 
    xy=delijn_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax4.get_lines()[len(ax4.get_lines()) - 1].get_color())
ax4.plot(helsinki_hsl_x, helsinki_hsl_y, marker='o', markersize=3.5, label="Helsinki-HSL", linewidth=lw)
ax4.annotate(str(int(helsinki_hsl_min[0])) + "," + str("{:.3f}".format(helsinki_hsl_min[1])), 
    xy=helsinki_hsl_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax4.get_lines()[len(ax4.get_lines()) - 1].get_color())
ax4.plot(nz_bus_x, nz_bus_y, marker='o', markersize=3.5, label="New Zealand-Bus", linewidth=lw)
ax4.annotate(str(int(nz_bus_min[0])) + "," + str("{:.3f}".format(nz_bus_min[1])), 
    xy=nz_bus_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax4.get_lines()[len(ax4.get_lines()) - 1].get_color())
ax4.plot(chicago_cta_x, chicago_cta_y, marker='o', markersize=3.5, label="Chicago-CTA", linewidth=lw)
ax4.annotate(str(int(chicago_cta_min[0])) + "," + str("{:.3f}".format(chicago_cta_min[1])), 
    xy=chicago_cta_min, textcoords="offset points", xytext=(0, 5), ha="center", color=ax4.get_lines()[len(ax4.get_lines()) - 1].get_color())
ax4.legend(loc="upper right")
ax4.set_xlabel("fragment size (connections)")
ax4.set_ylabel("response time (ms) / connection")

plt.legend()
plt.show()
