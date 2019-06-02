from Edge import *


class Graph:

    def __init__(self):
        self.start_state = 0
        self.store_state = 0
        self.characters = []
        self.edges = []
        self.nodes = {}

    def add_edge(self, edge):
        self.edges.append(edge)
        return edge

    def __str__(self):
        g = ""
        for edge in self.edges:
            g += edge.__str__()
        return g

    def get_new_state(self):
        re_state = self.store_state
        self.store_state += 1
        return re_state

    def get_now_state(self):
        return self.store_state - 1
