import networkx as nx


def show_graph_info(graph):
    flag = True
    if not graph.is_directed() or not graph.is_multigraph():
        print('In show_graph_info: Only information of MultiDiGraph can be show!')
        flag = False
    print('=================nodes==================')
    print('The graph have %d nodes' % len(graph.nodes))
    if flag:
        for n in graph.nodes:
            data = graph.node[n]
            print(n, data)
    print('=================edges==================')
    print('The graph have %d edges' % len(graph.edges))
    if flag:
        for e in graph.edges:
            data = graph.get_edge_data(e[0], e[1], e[2])
            print(e, data)


if __name__ == '__main__':
    g = nx.complete_graph(5)
    show_graph_info(g)
