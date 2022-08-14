class Distribution: 

	def __init__(self, mu = 0, sigma=1):
		""" super class for distribution classes """

		self.mean = mu
		self.stdev = sigma
		self.data = []

	def read_data_file(self, file_name):
		""" function to read data from a file format one number per line """
		
