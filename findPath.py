import heapq

def findPath(graph, start, goal, heuristic):
	# File de priorité (min-heap)
	open_set = []
	heapq.heappush(open_set, (0, start))  # (coût estimé, noeud actuel)

	# Coûts depuis le départ
	g_score = {node: float('inf') for node in graph}
	g_score[start] = 0

	# Chemins reconstruits
	came_from = {}

	while open_set:
		_, current = heapq.heappop(open_set)

		if current == goal:
			# Reconstruire le chemin
			path = []
			while current in came_from:
				path.append(current)
				current = came_from[current]
			path.append(start)
			return path[::-1]  # Retourner le chemin dans l'ordre

		for neighbor, cost in graph[current].items():
			tentative_g_score = g_score[current] + cost

			if tentative_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				f_score = tentative_g_score + heuristic(neighbor, goal)
				heapq.heappush(open_set, (f_score, neighbor))

	return None  # Aucun chemin trouvé

# Exemple de graphe orienté et pondéré
graph = {
	'A': {'B': 2, 'C': 4},
	'B': {'C': 1, 'D': 7},
	'C': {'D': 3},
	'D': {}
}

# Heuristique (exemple simplifié : distance directe)
def heuristic(n, goal):
	heuristic_values = {'A': 6, 'B': 4, 'C': 2, 'D': 0}  # Approximations
	return heuristic_values[n]

# Exécution de A*
start = 'A'
goal = 'D'
chemin = a_star(graph, start, goal, heuristic)
print("Chemin trouvé :", chemin)
