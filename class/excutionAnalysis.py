from datetime import *

class executionTimer(object):
	# Constructor
	def __init__(self):
		self.date = datetime(2022,9,23);
		self.startTime = self.date.today();
		self.endTime = self.startTime;
		self.executionTime = 0;

		# Providing some analysis for the data
		self.history = []
		self.average = 0 
		self.median = 0

	# Destructor
	def __del__(self):
		del self.date;
		del self.startTime;
		del self.endTime;
		del self.executionTime;
		del self.history[:]
		del self.average
		del self.median

	# print
	def __str__(self):
		return "executionTime = " + str(self.executionTime) + "\naverage = " + str(self.average) + "\nmedian = " + str(self.median)

	# sets the starting time to current date and time
	# also it clears the ending time in case the same object was reused again by the developer
	def executionStarts(self):
		try:
			self.startTime = self.date.today();
			del self.endTime;
			del self.executionTime;
		except:
			return False;

	# sets the endding time to current date and time
	# Then it calculate the differance between the start and end time and return the output in seconds
	def executionEnds(self):
		try:
			self.endTime = self.date.today();
			self.executionTime = (self.endTime - self.startTime).total_seconds();
			self.history.append(self.executionTime)
			return self.executionTime;
		except:
			return False;
	
	# returns the execution time (in seconds) of the previously timed task
	def getTimeTaken(self):
		try:
			return self.executionTime;
		except:
			return False;

	# reset the object to initial condition
	def clear(self):
		try:
			self.startTime = self.date.today();
			self.endTime = self.startTime;
			self.executionTime = 0;
			self.history = []
			self.average = 0 
			self.median = 0
		except:
			return False;

	# find the median of the tests (helpful in doing program analysis)
	def getMedian(self):
		try:
			self.history.sort();
			length = len(self.history);
			if length%2 == 0:
				self.median = (self.history[int(length/2-1)] + self.history[int(length/2)])/2;
			else:
				self.median = self.history[int(length/2)];
			return self.median;
		except:
			return False;
		
	# find the average of the tests (helpful in doing program analysis)
	def getAverage(self):
		try:
			length = len(self.history)
			total = 0;
			for x in range(length):
				total += self.history[x];
			self.average = total/length;
			return self.average;
		except:
			return False;

class excutionAnalysis(object):
	def __init__(self):
		self.data = {}
		self.total = 0
		self.percentages = {}

	# Destructor
	def __del__(self):
		del self.data
		del self.total
		del self.percentages

	def addProcess(self,name:str):
		self.data[name] = executionTimer()

	def executionStarts(self,name:str):
		self.data[name].executionStarts()

	def executionEnds(self,name:str):
		temp = self.data[name].executionEnds()
		self.total += self.data[name].getTimeTaken()
		return temp

	def analyzeData(self):
		for keys in self.data.keys():
			self.percentages[keys] = round((self.data[keys].getTimeTaken() / self.total)* 100,2)

	def __str__(self):
		temp = ""
		for keys in list(self.percentages.keys()):
			temp += ("Process Name - "+ str(keys) +"\t: " + str(self.percentages[keys]) + "%\n").expandtabs(30)
		return temp
