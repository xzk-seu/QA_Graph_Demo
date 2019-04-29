import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import to_pydot
import pydot


def classic_graph():
    K_5 = nx.complete_graph(5)
    K_3_5 = nx.complete_bipartite_graph(3, 5)
    barbell = nx.barbell_graph(10, 10)
    lollipop = nx.lollipop_graph(10, 20)

    g_list = [K_5, K_3_5, barbell, lollipop]
    for n, g in enumerate(g_list):
        plt.subplot(221 + n)
        nx.draw(g, with_labels=True, font_weight='bold')
    plt.show()


def classic_small_graphs():
    petersen = nx.petersen_graph()
    tutte = nx.tutte_graph()
    maze = nx.sedgewick_maze_graph()
    tet = nx.tetrahedral_graph()

    g_list = [petersen, tutte, maze, tet]
    for n, g in enumerate(g_list):
        plt.subplot(221+n)
        nx.draw(g, with_labels=True, font_weight='bold')
    plt.show()


def show(graph):
    # nx.draw(graph, with_labels=True, font_weight='bold')
    # nx.draw_circular(graph, with_labels=True, font_weight='bold')
    # nx.draw_kamada_kawai(graph, with_labels=True, font_weight='bold')
    # nx.draw_spectral(graph, with_labels=True, font_weight='bold')
    nx.draw_spring(graph, with_labels=True, font_weight='bold')
    # nx.draw(graph, with_labels=True, font_weight='bold')
    # nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()


def directed_graphs():
    g = nx.DiGraph()
    g.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75), (2, 3, 0.75), (3, 4, 0)])
    plt.subplot(121)
    nx.draw(g, with_labels=True, font_weight='bold')
    g = g.subgraph([1, 3])
    print(g.edges)
    plt.subplot(122)
    nx.draw(g, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    directed_graphs()
    # classic_graph()
    # directed_graphs()
    # G = nx.petersen_graph()
    # plt.subplot(111)

    # nx.draw(G, with_labels=True, font_weight='bold')
    # plt.subplot(122)
    #
    # nx.draw_shell(G, nlist=[range(5, 10), range(5)],
    #               with_labels=True, font_weight='bold')
    # plt.show()
