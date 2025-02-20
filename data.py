from intersection import *
from car import *


intersections: list[Intersection] = [
	Intersection(400, 250), # center(0)
	Intersection(600, 300), # right(1)
	Intersection(400, 100), # top(2)
	Intersection(200, 200), # left(3)
	Intersection(400, 400), # bottom(4)
]

cars: list[Car] = [
	Car(intersections[4], intersections[0])
]

from priority import Priority


# fill map test
intersections[0].directions = [
	intersections[1],
	intersections[3],
]

intersections[0].received = [
	intersections[1],
	intersections[2],
	intersections[3],
	intersections[4],
]

intersections[0].prios = [
	# from 0 (ie. intersections[1])
	[
		Priority(1, [1]) # straight right
	],
    
	# from 1 (ie. intersections[2])
	[
        Priority(0, [2, 3]), # turn left
        Priority(1, []), # turn right
	],
    
	# from 2 (ie. intersections[3])
    [
        Priority(0, [3]) # straight right
	],
    
	# from 3 (ie. intersections[4])
    [
        Priority(1, [0, 1]), # turn left
        Priority(0, []), # turn right
	]
]



intersections[1].directions = [
	intersections[0]
]

intersections[2].directions = [
	intersections[0]
]

intersections[3].directions = [
	intersections[0]
]

intersections[4].directions = [
	intersections[0]
]


