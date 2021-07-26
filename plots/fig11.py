import matplotlib
from matplotlib import pyplot as plt
import csv
import json

# Function to calculate server CPU values
def get_cpu_usage(server):
    root_path = "../scalability-test/server/results/nmbs/" + server + "/"
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
base_cpu_x, base_cpu_y = get_cpu_usage("base")
base_arp_x, base_arp_y = get_response_time("base")

live_cpu_x, live_cpu_y = get_cpu_usage("live")
live_arp_x, live_arp_y = get_response_time("live")

historical_cpu_x, historical_cpu_y = get_cpu_usage("historical")
historical_arp_x, historical_arp_y = get_response_time("historical")

# Create subplots
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2)) = plt.subplots(nrows=1, ncols=2)
lw = 2

ax1.plot(base_cpu_x, base_cpu_y, marker='o', markersize=3.5, label="Planned schedules", linewidth=lw)
ax1.plot(live_cpu_x, live_cpu_y, marker='o', markersize=3.5, label="Live updates", linewidth=lw)
ax1.plot(historical_cpu_x, historical_cpu_y, marker='o', markersize=3.5, label="Historical", linewidth=lw)
ax1.set_ylabel("cpu use (%)")
ax1.set_xscale("log")
ax1.set_xticks([1, 2, 5, 10, 20, 50])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.set_yticks([0, 20, 40, 60, 80, 100])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)
ax1.grid(alpha=0.3)

ax2.plot(base_arp_x, base_arp_y, marker='o', markersize=3.5, label="Planned schedules", linewidth=lw)
ax2.plot(live_arp_x, live_arp_y, marker='o', markersize=3.5, label="Live updates", linewidth=lw)
ax2.plot(historical_arp_x, historical_arp_y, marker='o', markersize=3.5, label="Historical", linewidth=lw)
ax2.set_ylabel("average response time (ms)")
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xticks([1, 2, 5, 10, 20, 50])
ax2.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.set_yticks([700, 1500, 3000, 10000, 50000])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.spines["right"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax2.grid(alpha=0.3)

handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3)

plt.show()