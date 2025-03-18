from intersection import *
from car import *
from findPath import findPath


intersections: list[Intersection] = [
	Intersection(300, 150), # center(0)
	Intersection(570, 250), # right(1)
	Intersection(200, 50), # top(2)
	Intersection(50, 200), # left(3)
	Intersection(200, 400), # bottom(4)
	Intersection(100, 400) # add(5)
]

cars: list[Car] = [
	Car(25, .1, intersections[3], intersections[5])
]


from priority import Priority


# fill map test
intersections[0].targets = [
	intersections[1],
	intersections[3],
]

intersections[0].origins = [
	intersections[1],
	intersections[2],
	intersections[3],
	intersections[4],
]


intersections[0].prios = [
	# from 0 (ie. intersections[1])
	[
		Priority(1, 10, [1]) # straight right
	],
	
	# from 1 (ie. intersections[2])
	[
		Priority(0, 10, [2, 3]), # turn left
		Priority(1, 10, []), # turn right
	],
	
	# from 2 (ie. intersections[3])
	[
		Priority(0, 10, [3]) # straight right
	],
	
	# from 3 (ie. intersections[4])
	[
		Priority(1, 10, [0, 1]), # turn left
		Priority(0, 10, []), # turn right
	]
]




intersections[2].targets = [
	intersections[0]
]

intersections[3].targets = [
	intersections[0],
	intersections[5]
]

intersections[4].targets = [
	intersections[0]
]

intersections[5].targets = [
    intersections[4]
]

print(findPath(intersections[3], intersections[1]))
