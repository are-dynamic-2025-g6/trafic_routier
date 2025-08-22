import heapq
import random


from intersection import Intersection
from intersection import Intersection_getWeight

def heuristic(a: Intersection, b: Intersection) -> float:
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


def findPath(start: Intersection, goal: Intersection) -> list[int]:
    open_set = []
    heapq.heappush(open_set, (0, random.random(), start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        _, _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                prev, _, idx = came_from[current]
                path.append(idx)
                current = prev
            return path[::-1]
        
        for idx, neighbor in enumerate(current.targets):
            tentative_g_score = g_score[current] + Intersection_getWeight(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                randSecurity = random.random()
                heapq.heappush(open_set, (f_score[neighbor], randSecurity, neighbor))
                came_from[neighbor] = (current, randSecurity, idx)
    
    return []