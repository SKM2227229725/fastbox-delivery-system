import math

def calculate_distance(point1, point2):
    """
    Calculate Euclidean distance between two points.
    Each point is a list/tuple of [x, y] coordinates.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)