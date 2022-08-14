import math
import matplotlib.pyplot as plt

class Gaussian(Distribution):

	"""class for caculating and visualizing a Gaussian distribution """
	def __init__ (self, mu=0, sigma =1):
		Distribution.__init__(self, mu, sigma)

	def calculate_mean(self):

		self.mean = sum(self.data)/len(self.data)
		return self.mean


	def calculate_stdev(self, sample=True):

		pass


	def plot_histogram(self):

		pass


	def pdf(self, x):

		pass


	def plot_histogram_pdf(self, n_spaces =50):

		pass


	def __add__(self, other):

		pass


	def __repr__(self):

		pass







