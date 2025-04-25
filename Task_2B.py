import dll  # Importing the LinkedList class
import dijkstra  # Importing the Dijkstra function
import random
import time
import math
import matplotlib.pyplot as plt
from adjacency_list_graph import *


# Network sizes to test
network_sizes = range(1000, 2001, 100)
average_execution_times = []
theoretical_complexity = []

for num_stations in network_sizes:
    graph = AdjacencyListGraph(num_stations, False, True)
    num_edges = num_stations * 10  # 10 edges per station

    for _ in range(num_edges):
        u = random.randint(0, num_stations - 1)
        v = random.randint(0, num_stations - 1)
        while v == u:
            v = random.randint(0, num_stations - 1)
        if graph.has_edge(u,v):
            continue
        else:
            graph.insert_edge(u, v, 1)

    execution_times = []
    for _ in range(10):  # Number of trials per network size
        source_station = random.randint(0, num_stations - 1)
        start_time = time.time()
        distances, _ = dijkstra.dijkstra(graph, source_station)
        end_time = time.time()
        exec_time_ms = (end_time - start_time) * 1000
        execution_times.append(exec_time_ms)

    average_execution_time = sum(execution_times) / len(execution_times)
    average_execution_times.append(average_execution_time)

    theoretical_complexity.append(num_stations * math.log(num_stations))

max_exec_time = max(average_execution_times)
max_theoretical = max(theoretical_complexity)
normalized_theoretical = [t * (max_exec_time / max_theoretical) for t in theoretical_complexity]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(network_sizes, average_execution_times, marker='o', color='b', label='Average Execution Time (ms)')
plt.plot(network_sizes, normalized_theoretical, linestyle='dotted', color='r', label='Theoretical Complexity O(n log n)')

plt.title('Average Execution Time vs. Network Size with Theoretical Complexity Overlay')
plt.xlabel('Network Size (number of stations)')
plt.ylabel('Average Execution Time (ms)')
plt.legend()
plt.grid(True)
plt.show()

