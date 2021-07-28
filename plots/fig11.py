import matplotlib
from matplotlib import pyplot as plt
import csv
import json

# Function to calculate server CPU values
def get_resource_usage(server, resource):
    root_path = "../scalability-test/server/results/nmbs/" + server + "/"
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

# Function to calculate average response time values
def get_response_time(server):
    root_path = "../scalability-test/client/results/nmbs/report-lc_" + server + ".json"
    cc = [1, 2, 5, 10, 20, 50]
    x = []
    y = []
    # Opening JSON file
    data = json.load(open(root_path))

    for i, d in enumerate(data):
        x.append(cc[i])
        y.append(d['averageResponseTime'])
    return x, y


# Get X and Y axises for each setup
base_cpu_x, base_cpu_y = get_resource_usage("base", "cpu")
base_ram_x, base_ram_y = get_resource_usage("base", "ram")
base_arp_x, base_arp_y = get_response_time("base")

live_cpu_x, live_cpu_y = get_resource_usage("live", "cpu")
live_ram_x, live_ram_y = get_resource_usage("live", "ram")
live_arp_x, live_arp_y = get_response_time("live")

historical_cpu_x, historical_cpu_y = get_resource_usage("historical", "cpu")
historical_ram_x, historical_ram_y = get_resource_usage("historical", "ram")
historical_arp_x, historical_arp_y = get_response_time("historical")

# Create subplots
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2, ax3)) = plt.subplots(nrows=1, ncols=3)
lw = 3

ax1.plot(base_cpu_x, base_cpu_y, marker='o', markersize=3.5, label="Planned schedules", linewidth=lw)
ax1.plot(live_cpu_x, live_cpu_y, marker='o', markersize=3.5, label="Live updates", linewidth=lw)
ax1.plot(historical_cpu_x, historical_cpu_y, marker='o', markersize=3.5, label="Historical", linewidth=lw)
ax1.set_ylabel("cpu use (%)")
ax1.set_xscale("log")
ax1.set_xticks([1, 2, 5, 10, 20, 50])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_yticks([0, 10, 20, 30, 40])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)
ax1.grid(alpha=0.3)

ax2.plot(base_ram_x, base_ram_y, marker='o', markersize=3.5, label="Planned schedules", linewidth=lw)
ax2.plot(live_ram_x, live_ram_y, marker='o', markersize=3.5, label="Live updates", linewidth=lw)
ax2.plot(historical_ram_x, historical_ram_y, marker='o', markersize=3.5, label="Historical", linewidth=lw)
ax2.set_ylabel("ram use (%)")
ax2.set_xscale("log")
ax2.set_xticks([1, 2, 5, 10, 20, 50])
ax2.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.set_yticks([0, 2, 4, 6, 8, 10])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax2.grid(alpha=0.3)

ax3.plot(base_arp_x, base_arp_y, marker='o', markersize=3.5, label="Planned schedules", linewidth=lw)
ax3.plot(live_arp_x, live_arp_y, marker='o', markersize=3.5, label="Live updates", linewidth=lw)
ax3.plot(historical_arp_x, historical_arp_y, marker='o', markersize=3.5, label="Historical", linewidth=lw)
ax3.set_ylabel("average response time (ms)")
ax3.set_xscale("log")
ax3.set_yscale("log")
ax3.set_xticks([1, 2, 5, 10, 20, 50])
ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.set_yticks([700, 1500, 3000, 10000, 50000])
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.spines["right"].set_visible(False)
ax3.spines["top"].set_visible(False)
ax3.grid(alpha=0.3)

handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3)

plt.show()