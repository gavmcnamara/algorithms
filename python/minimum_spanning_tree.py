'''
Given an undirected graph G,
find the minimum spanning tree within G.
A minimum spanning tree connects all vertices(nodes)
in a graph with the smallest possible total
weight of edges. Your function should take in
and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
'''

# Vertices are represented as unique strings.
# The function definition should be question3(G)

def question3(G):
    # if graph G is <= 1, there is no rumtime errors
    if len(G) <= 1:
        return G

    # checks to make sure G is a dictionary
    # if not it will print error message
    if type(G) != dict:
        print "Error: G is not a dictionary!"

    # returns list of all available keys in dictionary
    vertex = G.keys()
    # creates empty list
    min_span_tree = {}
    # starting point for G
    start = G.keys()[0]
    # creates empty list to store dict graph G
    min_span_tree[start] = []

    while len(min_span_tree.keys()) < len(vertex):
        min_weight = float('inf')
        min_edge = None
