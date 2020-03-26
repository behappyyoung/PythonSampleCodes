"""
BFS implementation in python

"""

import collections
class graph:
    def __init__(self,adjacency=None):
        if adjacency is None:
            adjacency = {}
        self.adjacency = adjacency

def bfs(graph, startnode):
# Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for node in graph[vertex]:
                if node not in seen:        #checking if not visited
                    seen.add(node)
                    queue.append(node)



# The graph dictionary
adjacency = {
          "a" : set(["b","c"]),
          "b" : set(["a", "d"]),
          "c" : set(["a", "d"]),
          "d" : set(["e"]),
          "e" : set(["a"])
        }

bfs(adjacency, "a")