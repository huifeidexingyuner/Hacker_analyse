#!/usr/bin/python
#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import networkx as nx
from Class_GraphMatrix import *

def create_undirected_matrix(my_graph):
	nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

	matrix = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
			  [0, 0, 1, 0, 1, 0, 0, 0],  # b
			  [0, 0, 0, 1, 0, 0, 0, 0],  # c
			  [0, 0, 0, 0, 1, 0, 0, 0],  # d
			  [0, 0, 0, 0, 0, 1, 0, 0],  # e
			  [0, 0, 1, 0, 0, 0, 1, 1],  # f
			  [0, 0, 0, 0, 0, 1, 0, 1],  # g
			  [0, 0, 0, 0, 0, 1, 1, 0]]  # h

	my_graph = Graph_Matrix(nodes, matrix)
	print(my_graph)
	return my_graph

def create_directed_matrix(my_graph):
	nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	inf = float('inf')
	matrix = [[0, 2, 1, 3, 9, 4, inf, inf],  # a
			  [inf, 0, 4, inf, 3, inf, inf, inf],  # b
			  [inf, inf, 0, 8, inf, inf, inf, inf],  # c
			  [inf, inf, inf, 0, 7, inf, inf, inf],  # d
			  [inf, inf, inf, inf, 0, 5, inf, inf],  # e
			  [inf, inf, 2, inf, inf, 0, 2, 2],  # f
			  [inf, inf, inf, inf, inf, 1, 0, 6],  # g
			  [inf, inf, inf, inf, inf, 9, 8, 0]]  # h

	my_graph = Graph_Matrix(nodes, matrix)
	print(my_graph)
	return my_graph

def create_directed_graph_from_edges(my_graph):
	nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	edge_list = [('A', 'F', 9), ('A', 'B', 10), ('A', 'G', 15), ('B', 'F', 2),
				 ('G', 'F', 3), ('G', 'E', 12), ('G', 'C', 10), ('C', 'E', 1),
				 ('E', 'D', 7)]

	my_graph = Graph_Matrix(nodes)
	my_graph.add_edges_from_list(edge_list)
	print(my_graph)

	# my_graph.DepthFirstSearch()
	#
	# draw_directed_graph(my_graph)

	return my_graph



def draw_undircted_graph(my_graph):
	G = nx.Graph()  # 建立一个空的无向图G
	for node in my_graph.vertices:
		G.add_node(str(node))
	for edge in my_graph.edges:
		G.add_edge(str(edge[0]), str(edge[1]))

	print("nodes:", G.nodes())  # 输出全部的节点
	print("edges:", G.edges())  # 输出全部的边
	print("number of edges:", G.number_of_edges())  # 输出边的数量
	nx.draw(G, with_labels=True)
	plt.savefig("undirected_graph.png")
	plt.show()


def draw_directed_graph(my_graph):
	G = nx.DiGraph()  # 建立一个空的无向图G
	for node in my_graph.vertices:
		G.add_node(str(node))
	# for edge in my_graph.edges:
	# G.add_edge(str(edge[0]), str(edge[1]))
	G.add_weighted_edges_from(my_graph.edges_array)

	print("nodes:", G.nodes())  # 输出全部的节点
	print("edges:", G.edges())  # 输出全部的边
	print("number of edges:", G.number_of_edges())  # 输出边的数量
	nx.draw(G, with_labels=True)
	plt.savefig("directed_graph.png")
	plt.show()


if __name__ == '__main__':
	my_graph = Graph_Matrix()
	# created_graph = create_undirected_matrix(my_graph)
	created_graph = create_directed_matrix(my_graph)
	# created_graph = create_directed_graph_from_edges(my_graph)

	# draw_undircted_graph(created_graph)
	draw_directed_graph(created_graph)