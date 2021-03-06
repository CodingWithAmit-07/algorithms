#!/usr/bin/python

# Date: 2017-12-25
#
# Description:
# Program creates a directed graph, adds few nodes to it and performs breadth
# first traversal(BFS) of graph.
#
# Approach:
# Use a queue to store adjacent nodes, loop until queue becomes empty and keep
# on adding adjacent nodes to queue while traversing.
#
# Reference:
# https://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/
#
# Complexity:
# O(V + E)
# V = number of vertexes/nodes
# E = number of edges

import collections


class Graph:

  def __init__(self):
    """
    Creates a dictionary having each node as key and list of adjacent nodes
    corresponding to each node as value.

    Example: {0:[1, 2], 1:[0], 2: [0, 3]...}
    """
    self.graph = collections.defaultdict(list)

  def add_edge(self, start, end):
    """
    Adds an edge to the adjacency list depending on start and end values.
    If start is a new value inserted in graph, it adds a key to dictionary
    otherwise it updates existing node's adjacency list.
    Adds directed edge to graph.

    Args:
      start: Start node of edge.
      end: End node of edge.
    """
    self.graph[start].append(end)

  def bfs(self, start_node):
    """
    Prints node values in breadth first search pattern.
    Initially marks all nodes as not visited(marked false) then starts with
    current node, traverses its adjacency list and goes in the same fashion.

    Args:
      start_node: Start node for BFS traversal.
    """

    visited = set()
    queue = collections.deque()
    queue.append(start_node)

    while queue:
      current_node = queue.popleft()
      print(current_node)

      visited.add(current_node)

      for node in self.graph[current_node]:
        if node not in visited:
            queue.append(node)
            visited.add(node)


g = Graph()

g.add_edge(10, 11)
g.add_edge(10, 12)
g.add_edge(11, 12)
g.add_edge(12, 10)
g.add_edge(12, 13)
g.add_edge(13, 12)
g.add_edge(13, 14)

g.bfs(10)


# Output:
# -------
# 10
# 11
# 12
# 13
# 14 - do not have any outgoing adjacent node
