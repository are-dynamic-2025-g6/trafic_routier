from Map import Map
from car import Car

from StatObject import *

from frameLaps import FRAME_LAPS


def Stat_runLap(map: Map):
	map.stats.angryCars.run(map, Stat_countAngryCars)

	map.stats.wait.run(map, Stat_countWait)
	map.stats.maxWait.run(map, Stat_maxWait)
	
	map.stats.mostWaiting.run(map, Stat_countMostWaiting)
	map.stats.leastWaiting.run(map, Stat_countLeastWaiting)
	map.stats.sameWaiting.run(map, Stat_countSameWaiting)
	
	map.stats.mostUsed.run(map, Stat_countMostUsed)
	map.stats.leastUsed.run(map, Stat_countLeastUsed)
	map.stats.sameUsed.run(map, Stat_countSameUsed)

	map.stats.sumDist.run(map, Stat_countSumDist)
	


def Stat_onCarFinish(map: Map, car: Car):
	if car.spawnLapCount < 0:
		return
	
	car.finalTarget.finalTargetCarCount -= 1
	map.stats.addTrajectDuration(map.lapCount - car.spawnLapCount)



def Stat_countAngryCars(map: Map):
	count = 0
	carCount = 0
	for car in map.cars:
		if car.isAlive():
			carCount += 1
			if map.lapCount - car.spawnLapCount >= car.angryDuration:
				count += 1
	
	if carCount == 0:
		return 0
	
	return count / carCount


def Stat_maxWait(map: Map):
	bestWait = 0
	for car in map.cars:
		if car.isAlive() and car.spawnLapCount > 0:
			w = map.lapCount - car.spawnLapCount
			if w > bestWait:
				bestWait = w
	

	return bestWait


def Stat_countWait(map: Map):
	count = 0
	carCount = 0
	for car in map.cars:
		if car.isAlive():
			carCount += 1
			count += map.lapCount - car.spawnLapCount
	
	if carCount == 0:
		return 0
	
	return count / carCount




def Stat_countMostWaiting(map: Map):
	# Search for max used target
	bestValue = 0
	best = None

	for i in map.intersections:
		count = len(i.carsApproching)
		if count > bestValue:
			best = i
			bestValue = count

	if not best:
		return 0

	# Count wait
	count = 0
	carCount = 0
	for car in best.carsApproching:
		if car.isAlive():
			carCount += 1
			count += map.lapCount - car.spawnLapCount
	
	if carCount == 0:
		return 0
	
	return count / carCount


def Stat_countLeastWaiting(map: Map):
	# Search for min used target
	bestValue = 3e30
	best = None

	for i in map.intersections:
		count = len(i.carsApproching)
		if count < bestValue:
			best = i
			bestValue = count

	if not best:
		return 0

	# Count wait
	count = 0
	carCount = 0
	for car in best.carsApproching:
		if car.isAlive():
			carCount += 1
			count += map.lapCount - car.spawnLapCount
	
	if carCount == 0:
		return 0
	
	return count / carCount


def Stat_countSameWaiting(map: Map):
	best = map.intersections[0]

	# Count wait
	count = 0
	carCount = 0
	for car in best.carsApproching:
		if car.isAlive():
			carCount += 1
			count += map.lapCount - car.spawnLapCount
	
	if carCount == 0:
		return 0
	
	return count / carCount




def Stat_countMostUsed(map: Map):
	bestValue = 0

	for i in map.intersections:
		count = len(i.carsApproching)
		if count > bestValue:
			bestValue = count

	return bestValue


def Stat_countLeastUsed(map: Map):
	bestValue = len(map.cars)

	for i in map.intersections:
		count = len(i.carsApproching)
		if count < bestValue:
			bestValue = count

	return bestValue


def Stat_countSameUsed(map: Map):
	best = map.intersections[0]

	return len(best.carsApproching)






from math import sqrt

def Stat_countSumDist(map: Map):
	# cx = 600
	# cy = 600

	cx = 2.5 * 300
	cy = 2.5 * 300

	count = 0
	carCount = 0
	for car in map.cars:
		if car.isAlive():
			carCount += 1
			x, y = car.getCoord()
			count += sqrt((x-cx)**2 + (y-cy)**2)
	
	if carCount == 0:
		return 0
	
	return count / carCount






import bisect

def StatList_trajectDuration(mapList: list[Map], dataList):
	for i in range(len(mapList)):
		arr = mapList[i].stats.trajectDurations
		dataList[i] = arr


def StatList_waitList(mapList: list[Map], dataList):
	for i in range(len(mapList)):
		arr = []
		map = mapList[i]
		for car in map.cars:
			arr.append(map.lapCount - car.spawnLapCount)

		dataList[i] = arr


def StatList_waitListSorted(mapList: list[Map], dataList):
	for i in range(len(mapList)):
		arr = []
		map = mapList[i]
		for car in map.cars:
			bisect.insort(arr, map.lapCount - car.spawnLapCount)

		dataList[i] = arr


