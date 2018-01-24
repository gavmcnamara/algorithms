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
    vertices = set(G.keys())
    # creates empty list
    min_span_tree = {}
    # creates starting point for dict G
    start = G.keys()[0]
    # creates empty list to store dict graph G
    min_span_tree[start] = []

    while len(min_span_tree.keys()) < len(vertices):
        # all other vertices are initialized to infinity
        min_weight = float('inf')
        min_edge = None
        for vertex in min_span_tree.keys():
            for (node, weight) in G[vertex]:
                if node not in min_span_tree.keys():
                    edges = (weight, node)
                if len(edges) > 0:
                    w, v = edges
                if w < min_weight:
                    min_weight = w
                    min_edge = (vertex, v)
        min_span_tree[min_edge[0]].append((min_edge[1], min_weight))
        min_span_tree[min_edge[1]] = [(min_edge[0], min_weight)]
    return min_span_tree


print question3({'A': [('B', 1), ('E', 3)],
                 'B': [('A', 9), ('C', 1), ('D', 4), ('E', 4)],
                 'C': [('B', 3), ('D', 7), ('E', 3)],
                 'D': [('B', 3), ('C', 1)],
                 'E': [('A', 2), ('B', 5), ('C', 6)]})

print question3({'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]})

print question3({'A': []})

print question3({})