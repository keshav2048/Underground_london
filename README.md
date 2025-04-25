🚇 London Underground Graph Algorithms (Dijkstra + Kruskal)
This Python project models the London Underground network as a weighted, undirected graph using adjacency lists. It performs shortest path analysis using Dijkstra’s algorithm, and network optimization using Kruskal’s algorithm to create a Minimum Spanning Tree (MST).

🎯 Features
✅ Shortest path analysis using Dijkstra’s algorithm from every station to all others

🔍 Identifies the longest shortest path and the route taken

🌲 Constructs a Minimum Spanning Tree (MST) using Kruskal’s algorithm

✂️ Detects redundant edges (that can be removed without breaking connectivity)

📊 Plots a histogram of all shortest travel times between station pairs

🧠 Core Concepts Used
Custom graph data structure using adjacency lists

Dijkstra’s algorithm for shortest path calculation

Kruskal’s algorithm for network optimization

Recursive path tracing using predecessor arrays

Data visualization with Matplotlib

London_underground_travel/
│
├── adjacency_list_graph.py           # Adjacency list-based graph structure
├── adjacency_matrix_graph.py         # Adjacency matrix-based graph structure
├── dll_sentinel.py                   # Doubly linked list (used in data structures)
├── heap.py                           # Min Heap logic
├── heap_priority_queue.py           # Heap-based priority queue
├── min_heap_priority_queue.py       # Alt implementation of min heap PQ
├── disjoint_set_forest.py           # Used in Kruskal’s algorithm
├── merge_sort.py                    # Merge sort implementation for comparisons
├── dijkstra.py                      # Dijkstra’s shortest path algorithm
├── mst.py                           # Kruskal’s Minimum Spanning Tree
├── single_source_shortest_paths.py  # Supporting structure for Dijkstra
├── dll.py                           # forms double linked list 
│
├── Task_1A.py                        # Measures time taken btw 2 stations
├── Task_1B.py                        # Average Execution Time vs. Network Size with Theoretical Complexity Overlay(Time)
├── Task_2A.py                        # Calculates Stops btw 2 stations
├── Task_2B.py                        # Average Execution Time vs. Network Size with Theoretical Complexity Overlay(Stops)
├── task_3A.py                        # Calulates all possible outcome and creates a histogram(time) 
├── task_3B.py                        # Calulates all possible outcome and creates a histogram(stops)
├── Task 4A.py                        # create a MST by removing all unneseccary stations
├── task_4b.py                        # creates a histogram of the MST
│
├── .idea/                            # IDE configs (optional)
├── __pycache__/                      # Python cache files (ignore)
└── README.md                         # This file
