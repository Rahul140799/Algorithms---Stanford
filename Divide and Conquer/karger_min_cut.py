"""
Python program to implement Karger's Randomized Contraction algorithm to find the minimum cut of a given graph.
"""


import random
import copy


def read_file(filename):
    """
    Converts file into Adjacency List.
    Implemented as dictionary.
    """
    adjacency_list = {}
    with open(filename, "r") as file:
        lines = file.read().strip().split("\n")

    for line in lines:
        line_data = list(map(int, line.strip().split("\t")))
        adjacency_list[line_data[0]] = line_data[1:]

    return adjacency_list


def chooseRandomEdge(adjacency_list):
    """
    Returns vertices of selected edge.
    """
    choices = list(adjacency_list.keys())
    x = random.choice(choices)
    y = random.choice(adjacency_list[x])
    return (x, y)


def random_contraction(graph):
    """
    Implementation of the random contraction algorithm.
    """

    while len(graph) > 2:
        
        x,y = chooseRandomEdge(graph) 

        # Combine vertices to remove edge.
        graph[x].extend(graph[y])

        # Remove y from all lists.
        # Add x to all lists.
        for vertex in graph[y]:
            graph[vertex].remove(y)
            graph[vertex].append(x)

        # Remove self loops of x
        while x in graph[x]:
            graph[x].remove(x)

        del graph[y]

    for key in graph:
        return len(graph[key])


def find_min_cuts(filename, iterations):
    adjacency_list = read_file(filename)
    minimum_cut = 1000000
    for i in range(iterations):
        graph = copy.deepcopy(adjacency_list)
        number_of_cuts = random_contraction(graph)
        minimum_cut = min(minimum_cut,number_of_cuts)
    
    return minimum_cut

        
