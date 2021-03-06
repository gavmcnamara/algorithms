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
    if len(G) <= 1:
        return G

    if type(G) != dict:
        print "Error: G is not a dictionary!"

    vertices = set(G.keys())
    min_span_tree = {}
    start = G.keys()[0]
    min_span_tree[start] = []

    while len(min_span_tree.keys()) < len(vertices):
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

''' Efficiency: O(n*m) due to the fact of edges and
vertices are each visited once in the while loop.
Code design: I chose Prim's algorithm which at each step will
choose the cheapest route to the next step. In this case,
the cheapest next step is the edge with the lowest weight.
I used a boolean array (min_span_tree) to represent the set of
vertices included in the MST. If a value min_span_tree[v] is true,
then vertex v is included in MST, otherwise not.
'''