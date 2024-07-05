import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def plot_demo():
	x = np.linspace(-10, 10, 20)
	y = 3*x-2

	plt.plot(x, y, '-r', label='y=3x-2')
	plt.show()

	# https://stackoverflow.com/questions/8409095/set-markers-for-individual-points-on-a-line-in-matplotlib
	plt.plot(range(10), linestyle='--', marker='o', color='b')
	plt.show()

	plt.plot(x, y, linestyle='--', marker='o', color='b')
	plt.show()

def directed_graph_demo():

	# Create a directed graph
	G = nx.DiGraph()

	# Add nodes and edges
	components = [
		("VMware vCenter Server", "VMware ESXi"),
		("VMware vSphere Client", "VMware vCenter Server"),
		("Virtual Machines (VMs)", "VMware ESXi"),
		("VMware vSAN", "VMware ESXi"),
		("VMware NSX", "VMware ESXi"),
		("VMware vSphere Client", "VMware ESXi"),
		("VMware Site Recovery Manager", "VMware vCenter Server"),
		("VMware High Availability (HA)", "VMware ESXi"),
		("VMware Fault Tolerance (FT)", "VMware ESXi"),
		("VMware vSphere Distributed Resource Scheduler (DRS)", "VMware vCenter Server"),
	]

	# Adding nodes and edges to the graph
	G.add_edges_from(components)

	# Draw the graph
	pos = nx.spring_layout(G, seed=42)
	plt.figure(figsize=(12, 8))

	# Draw nodes and edges
	nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)

	# Display the diagram
	plt.title("Relations between VMware ESXi and Other VMware Components")
	plt.show()


def matplotlib_demo():
	# plot_demo()
	directed_graph_demo()

matplotlib_demo()
