import networkx as nx
import matplotlib.pyplot as plt


class Draw:
    def __init__(self, graph):
        self.graph = graph

    def draw(self):
        G = nx.DiGraph()
        # create the graph
        edges = self.graph.edges
        for edge in edges:
            G.add_node(edge.begin, name=str(edge.begin))
            G.add_node(edge.end, name=str(edge.end))
            G.add_edge(edge.begin, edge.end, input=str(edge.weight))

        pos = nx.shell_layout(G)
        nx.draw_networkx_edge_labels(G, pos, font_size=12, alpha=1, rotate=False)
        nx.draw_networkx(G)
        plt.show()
