from Map import *
from priority import Priority

map = Map()


map.intersections = [
	Intersection(300, 350), # down(0)
	Intersection(100, 250), # left(1)
	Intersection(300, 50), # top(2)
	Intersection(500, 250), # right(3)
]

map.cars = [
	Car(25, .1, map.intersections[0], map.intersections[2]),
	Car(25, .1, map.intersections[1], map.intersections[0]),
]




# fill map test
map.intersections[0].targets = [
	map.intersections[1],
	map.intersections[2],
	map.intersections[3],
]

map.intersections[1].targets = [
	map.intersections[0],
	map.intersections[2],
	map.intersections[3],
]

map.intersections[2].targets = [
	map.intersections[0],
	map.intersections[1],
	map.intersections[3],
]

map.intersections[3].targets = [
	map.intersections[0],
	map.intersections[1],
	map.intersections[2],
]

map.intersections[0].origins = [
	map.intersections[1],
	map.intersections[2],
	map.intersections[3],
]

map.intersections[1].origins = [
	map.intersections[0],
	map.intersections[2],
	map.intersections[3],
]

map.intersections[2].origins = [
	map.intersections[0],
	map.intersections[1],
	map.intersections[3],
]

map.intersections[3].origins = [
	map.intersections[0],
	map.intersections[1],
	map.intersections[2],
]


map.intersections[0].prios = [
	# from 0
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 1
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 2
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 3
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	]
]



map.intersections[1].prios = [
	# from 0
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 1
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 2
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 3
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	]
]



map.intersections[2].prios = [
	# from 0
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 1
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 2
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 3
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	]
]



map.intersections[3].prios = [
	# from 0
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 1
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 2
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	],
	
	# from 3
	[
		Priority(0, 10, []),
		Priority(1, 10, []),
		Priority(2, 10, []),
	]
]





