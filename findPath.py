import heapq

from intersection import Intersection
from intersection import Intersection_getWeight


def findPath(start: Intersection, goal: Intersection):
	def heuristic(intersectionA, intersectionB):
		return ((intersectionA.x - intersectionB.x) ** 2 + (intersectionA.y - intersectionB.y) ** 2) ** 0.5
	
	open_set = []
	heapq.heappush(open_set, (0, start, 0))
	came_from = {}
	g_score = {start: 0}
	f_score = {start: heuristic(start, goal)}
	
	while open_set:
		_, current, index = heapq.heappop(open_set)

		if current == goal:
			path = []
			while current in came_from:
				path.append(index)
				current = came_from[current]
			path.append(index)
			return path[::-1]
		
		for i in range(len(current.targets)):
			neighbor = current.targets[i]
			tentative_g_score = g_score[current] + Intersection_getWeight(current, neighbor)
			
			if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
				heapq.heappush(open_set, (f_score[neighbor], neighbor, i))
	
	return None

