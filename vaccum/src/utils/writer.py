import csv
from collections import deque
from matplotlib import pyplot as plt

def write_buffer_data(buffer, data_path, filename):
    with open(data_path + f"/data/{filename}.csv", mode="a", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(buffer)

    return 0

def plot_recent_graph(data_path, filename, count, config):
    max_points = config["max_graph_points"]
    vac_index = config["desired_column_index"]
    count_rem = count % max_points
    count_dev = count // max_points
    with open(data_path + f"/data/{filename}.csv", "r") as fread:
        reader = csv.reader(fread)
        rows = deque(reader, maxlen=max(0, count_rem - 4))
        x = [float(row[1]) / 1000. for row in rows]
        y = [float(row[vac_index]) for row in rows]
        plt.plot(x, y)
        plt.xticks(rotation=60)
        plt.xlabel('Time [s]')
        plt.ylabel('Vacuum [Pa]')
        plt.savefig(data_path + f"/plot/{count_dev}.png")
        plt.clf()

    return 0