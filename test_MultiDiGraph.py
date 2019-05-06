import networkx as nx
import csv
import os
import matplotlib.pyplot as plt


def load_data():
    dir_path = os.path.join(os.getcwd(), 'ontology')
    object_attribute_path = os.path.join(dir_path, 'object_attribute.csv')
    valued_attribute_path = os.path.join(dir_path, 'valued_attribute.csv')
    object_attribute_list = list()
    valued_attribute_list = list()
    with open(object_attribute_path, 'r', encoding='utf-8') as csv_file:
        csv_file.readline()
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            object_attribute_list.append(i)

    with open(valued_attribute_path, 'r', encoding='utf-8') as csv_file:
        csv_file.readline()
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            valued_attribute_list.append(i)

    return dict(object_attribute=object_attribute_list, valued_attribute=valued_attribute_list)


# 静态问答图生成
def graph_generation():
    graph = nx.MultiDiGraph()
    data = load_data()

    # 导入对象属性边
    for i in data['object_attribute']:
        label, successor, predecessors = i
        graph.add_edge(successor, predecessors, label, label=label, type='object')
    # 导入值属性边
    for i in data['valued_attribute']:
        label, successor, value_type = i
        predecessors = '%s:%s' % (value_type, label)
        graph.add_edge(successor, predecessors, label, label=label, type='value')

    # 为节点导入属性
    for n in graph.nodes:
        if ':' in n:
            graph.node[n]['label'] = 'literal'
        else:
            graph.node[n]['label'] = 'concept'
    nx.freeze(graph)
    return graph


def show(graph):
    nx.draw(graph)
    plt.show()


def run():
    graph = graph_generation()

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
