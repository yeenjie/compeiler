import networkx as nx
import matplotlib.pyplot as plt


def draw(graph):
    colors = []
    G = nx.DiGraph()
    # create the graph
    edges = graph.edges
    node_set = set()
    start_node = graph.start_state
    for edge in edges:
        if edge.begin in node_set:
            pass
        else:
            node_set.add(edge.begin)
            if edge.begin == start_node:  # 颜色处理
                colors.append('r')
            else:
                colors.append('b')
            G.add_node(edge.begin, name=str(edge.begin))  # 添加节点

        if edge.end in node_set:
            pass
        else:
            node_set.add(edge.end)
            if edge.end == start_node:  # 颜色处理
                colors.append('r')
            else:
                colors.append('b')
            G.add_node(edge.end, name=str(edge.end))  # 添加节点
        G.add_edge(edge.begin, edge.end, i=str(edge.weight))  # 添加边

    pos = nx.spring_layout(G)
    nx.draw_networkx_edge_labels(G, pos, font_size=12, alpha=1, rotate=False)
    nx.draw_networkx_nodes(G, pos, node_size=600, node_color=colors)
    nx.draw_networkx_edges(G, pos, width=3)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    plt.show()

    plt.show()


class Draw:
    pass
