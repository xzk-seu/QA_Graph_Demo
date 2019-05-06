import networkx as nx
import csv
import os
import json
import matplotlib.pyplot as plt


def run():
    # graph = nx.read_graphml('test.graphml')
    #
    # graph = nx.read_yaml('test.yaml')
    #
    # with open('test_adj.json', 'r') as fr:
    #     data = json.load(fr)
    # graph = nx.adjacency_graph(data)

    with open('test_link.json', 'r') as fr:
        data = json.load(fr)
    graph = nx.node_link_graph(data)

    # with open('test_cytoscape.json', 'r') as fr:
    #     data = json.load(fr)
    # graph = nx.cytoscape_graph(data)

    print(graph.edges)
    print(len(graph.edges))

    print(graph.nodes)
    print(len(graph.nodes))

    for n in graph.nodes:
        data = graph.node[n]
        print(n, data)

    for e in graph.edges:
        data = graph.get_edge_data(e[0], e[1], e[2])
        print(e, data)


if __name__ == '__main__':
    run()
