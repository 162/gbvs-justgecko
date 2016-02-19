from src.graph import Graph
from math import log, exp

'''Я не знаю, как наззвать этот файл. Он по карте характеристики (feature  map) строить граф'''


def get_name(i, j):
    return '-'.join([str(i), str(j)])


def distance(a, b, kind):
    if kind == 'log':
        if a == 0:
            a = 0.01
        if b == 0:
            b = 0.01
        return abs(log(a/b))
    if kind == 'mod':
        return abs(a-b)


def f(a, b, sigma):
    return exp(-(a**2+b**2)/(2*sigma**2))


def weight(M, a, b, kind, sigma):
    return distance(M[a[0]][a[1]], M[b[0]][b[1]], kind)*f(a[0]-b[0], a[1]-b[1], sigma)


def constructor(M, sigma, kind='log'):
    g = Graph()
    for i in range(len(M)):
        for j in range(len(M[i])):
            for p in range(len(M)):
                for q in range(len(M[i])):
                    if p != i or q != j:
                        g.add_edge(get_name(i, j), get_name(p, q), weight(M, [i, j], [p, q], kind, sigma))
    g.normalize()
    return g


M = [[1, 2, 3, 2, 1],
     [2, 2, 3, 2, 2],
     [3, 3, 3, 3, 3],
     [2, 2, 2, 2, 2],
     [1, 2, 3, 2, 1]]
g = constructor(M, 1)
g.show()