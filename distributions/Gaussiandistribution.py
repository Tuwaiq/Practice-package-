import math
import matplotlib.pyplot as plt
from .Generaldistibution import Distribution 

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

	def read_data_file(self, file_name, sample = True ):
		with open(file_name) as file:
			data_list = []
			line = file.readline()
			while line:
				data_list.append(int(line))
				line = file.readline()
			file.close()

			self.data = data_list
			self.mean = self.calculate_mean
			self.stdev = self.calculate_stdev(sample)





	def plot_histogram(self):

		plt.hist(self.data)
		plt.title("Histogram of Data")
		plt.xlabel("data")
		plt.ylabel("count")


	def pdf(self, x):

		part1 = 1/(self.stdev * math.sqrt(2*math.pi))
		part2 = math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
		return part1 * part2


	def plot_histogram_pdf(self, n_spaces =50):

		mu = self.mean 
		sigma = self.stdev

		min_range = min(self.data)
		max_range = max(self.data)

		interval = (max_range  - min_range)/n_spaces

		x = []
		y = [] 

		for i in range(n_spaces):
			tmp = min_range + interval*i
			x.append(tmp)
			y.append(self.pdf(tmp))

			 fig, axes = plt.subplots(2,sharex=True)
        	fig.subplots_adjust(hspace=.5)
	        axes[0].hist(self.data, density=True)
	        axes[0].set_title('Normed Histogram of Data')
	        axes[0].set_ylabel('Density')

	        axes[1].plot(x, y)
	        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
	        axes[0].set_ylabel('Density')
	        plt.show()

        return x, y




	def __add__(self, other):

		result = Gaussian()
		result.mean = self.mean + other.mean 
		result.stdev = math.sqrt(self.stdev**2 + other.stdev**2)
		return result


	def __repr__(self):

		return "mean " + str(self.mean) +  ", standard deviation " + str(self.stdev)








