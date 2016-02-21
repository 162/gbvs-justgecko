from constructor import *


def build_activity_map(test, sigma, iterations):
    width, height = len(test), len(test[0])
    graph = get_markov_chain(test, sigma)
    matrix, points = get_matrix(graph)
    activity_map = get_activity_map(matrix, points, width, height)
    for i in range(iterations):
        activity_map = normalize_am(activity_map, sigma)
    return activity_map

M = [[1, 2, 3, 2, 1],
     [2, 2, 3, 2, 2],
     [3, 3, 3, 3, 3],
     [2, 2, 2, 2, 2],
     [1, 2, 3, 2, 1]]