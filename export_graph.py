import networkx as nx
import json
import os


def export_graph(graph, file_name):
    dir_path = os.path.join(os.getcwd(), 'export')
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except Exception as e:
            print(e)
    file_path = os.path.join(dir_path, '%s.json' % file_name)
    try:
        data = nx.node_link_data(graph)
        with open(file_path, 'w', encoding='utf-8') as fw:
            json.dump(data, fw)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    g = nx.complete_graph(5)
    export_graph(g, 'test')
