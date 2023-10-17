# -*- coding: utf-8 -*-


#solution for r2

import networkx as nx

# Graph a road network to indicate traffic density using weighted edges.

road_networks = nx.Graph()
road_networks.add_edge(2, 7, weight=0.9)
road_networks.add_edge(0, 4, weight=0.2)
road_networks.add_edge(3, 6, weight=0.9)
road_networks.add_edge(6, 5, weight=0.8)
road_networks.add_edge(8, 3, weight=1.2)
road_networks.add_edge(8, 7, weight=0.8)
road_networks.add_edge(4, 8, weight=0.7)

road_networks.add_edge(4, 5, weight=1.1)
road_networks.add_edge(7, 6, weight=0.9)
road_networks.add_edge(7, 7, weight=0.5)
road_networks.add_edge(1, 8, weight=1.1)
road_networks.add_edge(1, 5, weight=0.7)
road_networks.add_edge(6, 4, weight=0.6)
road_networks.add_edge(6, 5, weight=1.0)
road_networks.add_edge(4, 3, weight=0.5)

#Initial

van_1_queue = [0]  # Van 1 queue with starting position
van_2_queue = [0]  # Van 2 queue with starting position
van_1_deliveries = []  # List of deliveries for Van 1
van_2_deliveries = []  # List of deliveries for Van 2

# Create a function that applies Dijkstra's algorithm to determine a van's subsequent node.
def Cal_node(cur_loc, target):
    shortest_path = nx.shortest_path(road_networks, source=cur_loc, target=target, weight='weight')
    return shortest_path[1] if len(shortest_path) > 1 else cur_loc  # Next node or remain in place currently

# Main
for clock_ticks in range(1, 4):  # 1 to 3 Clock Ticks
    print(f"clock ticks {clock_ticks}")

 # Manage requests for pickup and delivery
    if clock_ticks == 1:
        van_1_queue.append(7)  # Place customer 1's pick-up location in the line for van 1
        van_1_deliveries.extend([("id01", "p", 6), ("id01", "d", 5)]) #Van 1 picks up and delivers the customer's records.


        van_2_queue.append(5)  # Place customer 2's pick-up location in the line for van 2
        van_2_deliveries.extend([("id02", "p", 4), ("id02", "d", 5)])  #Van 2 picks up and delivers records for client 2

    if clock_ticks == 2:
        van_1_queue.append(3)  # Place customer 3's pick-up location in the line for van 1
        van_1_deliveries.extend([("id03", "p", 3), ("id03", "d", 6)])  #Van 1 will pick up and deliver records for client 3

        van_1_queue.append(3)  # Place customer 4's pick-up location in the line for van 1
        van_1_deliveries.extend([("id04", "p", 4), ("id04", "d", 5)])  #Van 2 picks up and delivers records for client 4

    if clock_ticks == 3:
        van_1_queue.append(3)  # Add customer 5's pickup location to Van 1's queue
        van_1_deliveries.extend([("id05", "p", 4), ("id05", "d", 6)])  # Van 1 picks up and delivers records for client 5

        van_1_queue.append(1)  # Add customer 6's pickup location to Van 1's queue
        van_1_deliveries.extend([("id06", "p", 4), ("id06", "d", 3)]) # Van 1 picks up and delivers records for client 6

    # Determine the next node for each van
    next_node_van_1 = Cal_node(van_1_queue[-1], van_1_queue[-2]) if len(van_1_queue) > 1 else 0  # Calculate next node for Van 1
    next_node_van_2 = Cal_node(van_2_queue[-1], van_2_queue[-2]) if len(van_2_queue) > 1 else 0

    # Print the queue and path contents.
    print("Service Queue for Van #1:", van_1_deliveries)
    print("Service Queue for Van #2", van_2_deliveries)
    print("Vehicle 1 -- Path:", van_1_queue)
    print("Vehicle 2 -- Path", van_2_queue)
    print("\n\n")

    print("last Step:")
print("Service Queue for Van #1:", van_1_deliveries)
print("Service Queue for Van #2:", van_2_deliveries)
print("Vehicle 1 -- Path:", van_1_queue)
print("Vehicle 2 -- Path:", van_2_queue)

#solution for r3
import networkx as nx
import random
import statistics
import matplotlib.pyplot as plt  #Visualization using Matplotlib import

# Network at random with 100 nodes and a connectivity of 3..
random_graphs = nx.random_regular_graph(3, 100)

# Create a function to determine how far nodes in the graph are from another.
def cal_distance(node_1, node_2):
    # Determine the length of the shortest path between the source  and target nodes.
    return nx.shortest_path_length(random_graphs, source=node_1, target=node_2)

# Create a 30 car fleet in your head
count_vehicles = 30
total_travel_dist = 0
total_trip = 0

# Start action
hour_Simulation = 24
Hourly_reservations = random.randint(450, 600)  # Make a certain amount of arbitrary reservations each hour.

for hour in range(hour_Simulation):
    for _ in range(Hourly_reservations):
        # Create a reservation at random for nodes.
        source_nodes = random.randint(0, 99)
        target_nodes = random.randint(0, 99)

        # Utilizing the specified function, determine the travel distance for the reservation.
        distance = cal_distance(source_nodes, target_nodes)

        # recent statistics
        total_travel_dist += distance
        total_trip += 1

# Determine the average metrics
average_daily_dist = total_travel_dist / (count_vehicles * hour_Simulation)
average_daily_trip = total_trip / (count_vehicles * hour_Simulation)

# Print results
print("Average Daily Distance Covered by the Fleet:", average_daily_dist)
print("The fleet's average daily number of trips:", average_daily_trip)

# Utilize NetworkX and Matplotlib to plot the random graph.
pos = nx.spring_layout(random_graphs, seed=42)  # Set the framework and the seeds for coherence
nx.draw(random_graphs, pos, with_labels=False, node_size=10, node_color='b', alpha=0.7)
plt.title("A random graph of 100 nodes has an average connectivity of 3.")
plt.show()

#solution for r4
import networkx as nx
import random
import statistics
import matplotlib.pyplot as plt

# Make a random graph of 100 nodes with a connectedness of 3 per node.
random_graphs = nx.random_regular_graph(3, 100)

# Create a function to determine how far nodes in the graph are from another.
def cal_distance(node_1, node_2):
    # In the random graph, determine the length of the shortest path between nodes 1 and 2.
    shortest_path_length = nx.shortest_path_length(random_graphs, source=node_1, target=node_2)
    return shortest_path_length

# Create a 60-vehicle fleet in your head
count_vehicles = 60
total_travel_dist = 0  # Set the overall distance traveled to zero.
total_trip = 0  # Set the overall number of trips to zero.

# 24 hours worth of simulation
hour_Simulation = 24
Hourly_reservations = random.randint(450, 600)  # Make a certain number of reservations at random each hour.

# loop for hour
for hour in range(hour_Simulation):
    #Repeat the process for each reservation made at this time.
    for _ in range(Hourly_reservations):
        # Create a reservation at random for nodes.
        source_nodes = random.randint(0, 99)
        target_nodes = random.randint(0, 99)

        # Utilize the cal_distance function to determine the distance for the reservation.
        distance = cal_distance(source_nodes, target_nodes)

        # Current data
        total_travel_dist += distance  #Distance from this trip added to overall distance
        total_trip += 1  #An increase in the overall number of journeys

#Determine the fleet's average daily distance traveled.
average_daily_dist = total_travel_dist / (count_vehicles * hour_Simulation)

# Determine the average daily mileage of the fleet as a whole.
average_daily_trip = total_trip / (count_vehicles * hour_Simulation)

# Print results
print("Over the Fleet, the Average Daily Distance is:", average_daily_dist)
print("Over the Fleet, the Average Daily Trips:", average_daily_trip)

#Create a random graph and add labels.
plt.figure(figsize=(11, 7))
pos = nx.spring_layout(random_graphs, seed=42)
nx.draw(random_graphs, pos, with_labels=True, node_size=100, node_color='orange', font_size=8, font_color='black', alpha=0.7)

plt.title("100 nodes in a random graph with an average connectedness of 3.")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

# show plot
plt.show()

#ANSWER FOR R5 WITH 4 CONNECTIVITY
import networkx as nx
import random
import statistics
import matplotlib.pyplot as plt  # Plot data by importing Matplotlib.

# Make a random 100-node graph with an average connectedness of four.
random_graphs = nx.random_regular_graph(4, 100)

# Create a function to calculate the separation between nodes in graph.
def cal_distance(node_1, node_2):
    # Find the random graph's shortest path between nodes 1 and 2.
    shortest_path_length = nx.shortest_path_length(random_graphs, source=node_1, target=node_2)
    return shortest_path_length

#Create a 60-vehicle fleet in your head
count_vehicles = 60
total_travel_dist = 0  # Set the overall distance to zero.
total_trip = 0  #Initialize the number of trips overall

# Simulate for 24 hours
hour_Simulation = 24
Hourly_reservations = random.randint(450, 600)  # Make a set of reservations at random each hour.

#Repeat each hour of the day's simulation in a loop.
for hour in range(hour_Simulation):

 #Repeat this procedure for every reservation made during this time.

    for _ in range(Hourly_reservations):
        # Create a reservation at random for nodes.
        source_nodes = random.randint(0, 99)
        target_nodes = random.randint(0, 99)

        #Make a reservation and use the cal_distance function to determine the distance.
        distance = cal_distance(source_nodes, target_nodes)

        # recent statistics
        total_travel_dist += distance  # Distance from this trip added to overall distance
        total_trip += 1  # raising the overall number of trips

# Determine the fleet's average daily distance traveled.
average_daily_dist = total_travel_dist / (count_vehicles * hour_Simulation)

# Determine the average daily mileage of the fleet as a whole.
average_daily_trip = total_trip / (count_vehicles * hour_Simulation)

# Print results
print("New Average Daily Distance per day:", average_daily_dist)

# Create a labeled random graph.
plt.figure(figsize=(11, 7))
pos = nx.spring_layout(random_graphs, seed=38)
nx.draw(random_graphs, pos, with_labels=True, node_size=100, node_color='purple', font_size=8, font_color='black', alpha=0.8)

plt.title("100 nodes in a random graph with an average connectedness of 4.")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

#plot display
plt.show()

!jupyter nbconvert --to html /content/finalCOde.ipynb

