import networkx as nx
import json
import os


def export_interface(export_obj, file_name, export_type):
    if export_type == 'graph':
        data = nx.node_link_data(export_obj)
    elif export_type == 'list':
        data = export_obj
    else:
        raise Exception('export wrong type')

    dir_path = os.path.join(os.getcwd(), 'export')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, '%s.json' % file_name)
    with open(file_path, 'w', encoding='utf-8') as fw:
        json.dump(data, fw)


def export_graph(graph, file_name):
    try:
        export_interface(graph, file_name, 'graph')
    except Exception as e:
        print(e)


def export_subgraph_list(subgraph_list, file_name):
    try:
        export_interface(subgraph_list, file_name, 'list')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    g = nx.complete_graph(5)
    export_graph(g, 'test')
