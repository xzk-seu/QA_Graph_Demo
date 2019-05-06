import networkx as nx
import json
import os
from show_graph_info import show_graph_info


# 有n条边的子图列表从文件导入
def load_subgraph_data_list(edge_number):
    file_path = os.path.join(os.getcwd(), 'export', '%d_sub_graph.json' % edge_number)
    with open(file_path, 'r') as fr:
        subgraph_data_list = json.load(fr)
    return subgraph_data_list


def load_graph(file_name):
    dir_path = os.path.join(os.getcwd(), 'export')
    file_path = os.path.join(dir_path, '%s.json' % file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as fr:
            data = json.load(fr)
        graph = nx.node_link_graph(data)
    except Exception as e:
        print(e)
    else:
        return graph


if __name__ == '__main__':
    g = load_graph('all_graph')
    show_graph_info(g)
