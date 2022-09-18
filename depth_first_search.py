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
        self.vertices = list[Vertex]
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
        dfs(g, node, visited, dfs_result)

    return dfs_result


def dfs(g: Graph, node: Node, visited: dict[int, bool], result: list[int]):
    value = node.get_value()
    if visited.get(value) is False:
        visited[value] = True
        result.append(value)
    
    idx = g.vertex_dict.get(value)
    if idx == None:
        return

    vertex = g.vertices[idx]
    for adj in vertex.get_adjacents():
        dfs(g, adj, visited, result)
