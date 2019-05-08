import networkx as nx
import os
from itertools import combinations
from graph_generation import graph_generation
from load_graph import load_graph, load_subgraph_data_list
from export_graph import export_subgraph_list
from show_graph_info import show_graph_info
from export_graph import export_graph


# 检查all_graph是否存在，若不存在则根据本体文件生成
def get_all_graph():
    all_graph_path = os.path.join(os.getcwd(), 'export', 'all_graph.json')
    if not os.path.exists(all_graph_path):
        print('The all_graph is not exist,generating...')
        graph = graph_generation()
    else:
        print('The all_graph is existing, loading...')
        graph = load_graph('all_graph')
    return graph


# 得到all_graph中所有由一条值属性边构成子图，并将其序列化后以list类型返回
def get_subgraph_with_one_edge(all_graph):
    subgraph_data_list = list()
    for e in all_graph.edges:
        # 获取边上的属性值
        edge_attribute = all_graph.get_edge_data(e[0], e[1], e[2])
        edge_type = edge_attribute.setdefault('type', None)
        # 判断一条边是否是值属性边
        if edge_type == 'value':
            subgraph = all_graph.edge_subgraph([e])
            # 序列化为dict格式
            subgraph_data = nx.node_link_data(subgraph)
            subgraph_data_list.append(subgraph_data)
    return subgraph_data_list


# 对子图进行扩张，得到多一条边的子图
# 对图中的概念节点，在全局图中，寻找其他的前驱和后继，找到一个生成一个子图，判断是否重复
def subgraph_expend(subgraph, all_graph):
    pass


# 生成有n条边的子图列表
# 并将其序列化后以list类型返回
def get_subgraph_with_multi_edge(edge_number, all_graph):
    subgraph_data_list = list()
    edge_combinations = combinations(all_graph.edges, edge_number)
    for edges_set in edge_combinations:
        candidate_subgraph = all_graph.edge_subgraph(edges_set)
        is_connected = nx.algorithms.is_weakly_connected(candidate_subgraph)
        if not is_connected:
            print('not connected', edges_set)
            continue

        flag = False
        for n in candidate_subgraph.nodes:
            if candidate_subgraph.node[n]['label'] == 'literal':
                flag = True
        if not flag:
            print('pass', edges_set)
            continue
        print(edges_set)
        subgraph_data = nx.node_link_data(candidate_subgraph)
        subgraph_data_list.append(subgraph_data)
    print(len(subgraph_data_list))
    return subgraph_data_list


def run():
    all_graph = get_all_graph()
    # subgraph_list = get_subgraph_with_one_edge(all_graph)
    # export_subgraph_list(subgraph_list, '1_sub_graph')

    # subgraph_list = get_subgraph_with_multi_edge(2, all_graph)
    # export_subgraph_list(subgraph_list, '2_sub_graph')
    number_of_edges = int(input('Please the maximum number of edges: '))

    for m in range(1, number_of_edges+1):
        subgraph_list = get_subgraph_with_multi_edge(m, all_graph)
        export_subgraph_list(subgraph_list, '%d_sub_graph' % m)


if __name__ == '__main__':
    run()
