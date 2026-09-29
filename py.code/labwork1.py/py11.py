import math

def compute_distance(p1: tuple, p2: tuple) -> float:
    '''Computes the Euclidean distance between two points (x1, y1) and (x2, y2).'''
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

point1 = (1, 2)
point2 = (4, 6)
distance = compute_distance(point1, point2)
print(f'Distance between {point1} and {point2}: {distance}')