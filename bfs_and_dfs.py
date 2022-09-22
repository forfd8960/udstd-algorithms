# Depth first search

# use adjacent list to represent the graph
from linked_list import Node, LinkedList

class Vertex:
    """Graph Vertex"""
    def __init__(self, ll: LinkedList) -> None:
        self.adjacents = ll
        
    def get_node(self) -> Node:
        return self.adjacents.head
    
    def get_adjacents(self) -> list[Node]:
        return self.adjacents.iterate()
    
    def add_adjacent(self, n: Node):
        self.adjacents.add(n)


class Graph:
    def __init__(self) -> None:
        self.vertices = []
        self.vertex_dict = {}
    
    def add_edge(self, src: Node, adj: Node):
        idx = self.vertex_dict.get(src.get_value())
        if idx != None:
            vertex = self.vertices[idx]
            vertex.add_adjacent(adj)
        else:
            vtex = Vertex(LinkedList(src, 1))
            vtex.add_adjacent(adj)
            
            self.vertices.append(vtex)
            self.vertex_dict[src.get_value()] = len(self.vertices) - 1


def DFS(g: Graph) -> list[int]:
    if g is None:
        return None
    
    visited = {}
    dfs_result = []
    
    for vertex in g.vertices:
        node = vertex.get_node()
        if visited.get(node.get_value()) is None:
            dfs(g, node, visited, dfs_result)

    return dfs_result


def dfs(g: Graph, node: Node, visited, result: list[int]):
    value = node.get_value()
    if visited.get(value) is None:
        visited[value] = True
        result.append(value)
    
    idx = g.vertex_dict.get(value)
    if idx == None:
        return

    vertex = g.vertices[idx]
    for adj in vertex.get_adjacents():
        dfs(g, adj, visited, result)


"""
In [1]: from linked_list import Node

In [2]: from bfs_and_dfs import Graph, BFS

In [3]: g = Graph()

In [4]: a, c, d, e, f, b = 1,2,3,5,6,9

In [5]: g.add_edge(Node(a, None), Node(c, None))

In [6]: g.add_edge(Node(a, None), Node(d, None))

In [7]: g.add_edge(Node(a, None), Node(e, None))

In [8]: g.add_edge(Node(e, None), Node(f, None))

In [9]: g.add_edge(Node(e, None), Node(b, None))

In [10]: g.vertex_dict
Out[10]: {1: 0, 5: 1}

In [11]: g.vertices
Out[11]: [<bfs_and_dfs.Vertex at 0x1078919f0>, <bfs_and_dfs.Vertex at 0x1078933d0>]

In [12]: 

In [12]: BFS(g)
Out[12]: [1, 2, 3, 5, 6, 9]
"""
def BFS(graph: Graph) -> list[int]:
    if graph is None:
        return None
    
    visited = {}
    bfs_result = []
    queue = []
    
    for vertex in graph.vertices:
        node = vertex.get_node()
        node_id = node.get_value()
        
        if visited.get(node_id) is None:
            add_to_bfs_list(visited, node_id, queue, bfs_result)
            
            while len(queue) > 0:
                n = queue[0]
                queue = queue[1:]
                idx = graph.vertex_dict.get(n)
                if idx == None:
                    continue
                
                vertex = graph.vertices[idx]
                for adj in vertex.get_adjacents():
                    adj_id = adj.get_value()
                    if visited.get(adj_id) is None:
                        add_to_bfs_list(visited, adj_id, queue, bfs_result)

    return bfs_result


def add_to_bfs_list(visited, node_id, queue, bfs_result):
    visited[node_id] = True
    queue.append(node_id)
    bfs_result.append(node_id)


def bfs(g: Graph, node: Node, visited, result: list[int], queue: list[int]):
    node_id = node.get_value()
    if visited.get(node_id) is None:
        visited[node_id] = True
        queue.append(node_id)
        result.append(node_id)
    
    idx = g.vertex_dict.get(node_id)
    if idx == None:
        return
    
    while len(queue) > 0:
        vertex = g.vertices[idx]
        for adj in vertex.get_adjacents():
            bfs(g, adj, visited, result, queue)
        
        queue = queue[1:]

