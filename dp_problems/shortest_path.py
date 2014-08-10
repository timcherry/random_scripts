POINTS = [ 
(4, 5, 0.35), 
(5, 4, 0.35),
(4, 7, 0.37),
(5, 7, 0.28),
(7, 5, 0.28),
(5, 1, 0.32),
(0, 4, 0.38),
(0, 2, 0.26),
(7, 3, 0.39),
(1, 3, 0.29),
(2, 7, 0.34),
(6, 2, 0.40),
(3, 6, 0.52),
(6, 0, 0.58),
(6, 4, 0.93),
]

class Node(object):
    def __init__(self, id_,):
        self.id = id_
        self.neighbors = []
    
    def add_neighbor(self, id_, weight):
        self.neighbors.append((id_,weight))

    def __str__(self,):
        return "id: %s. neighbors:%s"%(self.id, self.neighbors)

def build_nodes():
    nodes = dict()
    for (l,r,w) in POINTS:
        nodes[r] = nodes.get(r, Node(r))
        nodes[l] = nodes.get(l, Node(l))
        nodes[l].add_neighbor(nodes[r], w) 
    return nodes

def find_shortest_path(graph, start, end):
    end_ = graph[end]
    start_ = graph[start]
    stack = [start_]
    visited = {start_ : 0}
    while True:
        if len(stack) == 0:
            break
        node = stack.pop(0)
        for (ne, w) in node.neighbors:
            if (ne not in visited) or (visited[ne] > + (visited[node] + w)):  
                stack.append(ne)
                visited[ne] = w + visited[node]
    if end_ in visited:
        return visited[end_]
    else:
        return "No Path"

print "Shortest Path:", find_shortest_path(build_nodes(), 0, 6) 
