import matplotlib.pyplot as plt
import numpy as np

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

def matplotlib_demo():
	plot_demo()
