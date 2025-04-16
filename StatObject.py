from math import floor

def expAverage(average, value, param):
	return value * param + (1-param) * average

class StatObjectData:
	def __init__(self):
		self.average = 0
		self.list = [0]
		self.currentList = []

	def run(self, map, method):
		self.currentList.append(method(map))
	

	def add(self):
		if len(self.currentList) == 0:
			return

		average = 0
		for i in self.currentList:
			average += i

		average /= len(self.currentList)

		# self.average = expAverage(
			# self.average,
			# average,
			# .5
		# )

		self.average = average
		
		self.list.append(self.average)
		self.currentList.clear()




class StatObject:
	TRAJECT_DURATION_FRAME = 60

	def __init__(self):
		self.trajectDurations: list[int] = [0]
		
		self.angryCars = StatObjectData()
		self.wait = StatObjectData()
		self.maxWait = StatObjectData()

		self.mostWaiting = StatObjectData()
		self.leastWaiting = StatObjectData()
		self.sameWaiting = StatObjectData()

		self.mostUsed = StatObjectData()
		self.leastUsed = StatObjectData()
		self.sameUsed = StatObjectData()

		self.sumDist = StatObjectData()

		

	def addTrajectDuration(self, duration: int):
		index = floor(duration/StatObject.TRAJECT_DURATION_FRAME)
		
		length = len(self.trajectDurations)
		if index < length:
			self.trajectDurations[index] += 1
			return
		
		self.trajectDurations.extend([0] * (index - length))
		self.trajectDurations.append(1)


			
