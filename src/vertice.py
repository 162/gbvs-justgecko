from src.edge import Edge


class Vertice():
    def __init__(self, name):
        self.name = name
        self.edges = []

    def new_edge(self, destination, weight):
        self.edges.append(Edge(destination, weight))
