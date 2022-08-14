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

		mean = self.caculate_mean()
		sigma = 0 

		if sample: 
			n = len(self.data) -1
		else:
			n = len(self.data)

		for number in self.data: 
			sigma += (number - mean )**2

		self.stdev = math.sqrt(sigma/n)

		return self.stdev


	def plot_histogram(self):

		plt.hist(self.data)
		plt.title("Histogram of Data")
		plt.xlabel("data")
		plt.ylabel("count")


	def pdf(self, x):

		pass


	def plot_histogram_pdf(self, n_spaces =50):

		pass


	def __add__(self, other):

		pass


	def __repr__(self):

		pass







