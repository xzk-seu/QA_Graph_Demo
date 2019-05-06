import networkx as nx
import csv
import os
from show_graph_info import show_graph_info
from export_graph import export_graph


# 从ontology文件夹导入数据
def load_data():
    dir_path = os.path.join(os.getcwd(), 'ontology')
    object_attribute_path = os.path.join(dir_path, 'object_attribute.csv')
    valued_attribute_path = os.path.join(dir_path, 'valued_attribute.csv')
    object_attribute_list = list()
    valued_attribute_list = list()

    # 导入对象属性
    with open(object_attribute_path, 'r', encoding='utf-8') as csv_file:
        csv_file.readline()
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            object_attribute_list.append(i)
    # 导入值属性
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
    # 使graph不能再被修改
    nx.freeze(graph)

    export_graph(graph, 'all_graph')
    return graph


def run():
    graph = graph_generation()
    show_graph_info(graph)
    export_graph(graph, 'all_graph')


if __name__ == '__main__':
    run()
