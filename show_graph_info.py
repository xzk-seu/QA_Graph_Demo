import networkx as nx


def show_graph_info(graph):
    flag = True
    if not graph.is_multigraph():
        flag = False
    print('=================nodes==================')
    print('The graph have %d nodes' % len(graph.nodes))
    for n in graph.nodes:
        data = graph.node[n]
        print(n, data)
    print('=================edges==================')
    print('The graph have %d edges' % len(graph.edges))
    for e in graph.edges:
        # multigraph的边结构为(u, v, k)
        # 非multigraph的边结构为(u, v)
        if flag:
            data = graph.get_edge_data(e[0], e[1], e[2])
        else:
            data = graph.get_edge_data(e[0], e[1])
        print(e, data)


if __name__ == '__main__':
    g = nx.complete_graph(5)
    show_graph_info(g)
