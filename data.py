from intersection import *
from car import *


intersections: list[Intersection] = [
    Intersection(200, 100),
    Intersection(200, 250),
    Intersection(400, 100),
    Intersection(400, 200),
    Intersection(400, 300),
    Intersection(600, 200),
]

cars: list[Car] = [Car(intersections[0], intersections[1])]



# init map
intersections[0].directions = [intersections[1], intersections[2]]
intersections[1].directions = [intersections[3]]
intersections[2].directions = [intersections[3]]
intersections[3].directions = [intersections[0], intersections[4], intersections[5]]
intersections[4].directions = [intersections[3]]
intersections[5].directions = [intersections[3]]
