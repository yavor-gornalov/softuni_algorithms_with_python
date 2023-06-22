# https://judge.softuni.org/Contests/Practice/Index/3464#0
"""
In unweighted graphs finding the shortest path can be done
with BFS
"""
from collections import deque

nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count + 1)]

for _ in range(edges_count):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
end_node = int(input())

visited = [False] * (nodes_count + 1)
parent = [None] * (nodes_count + 1)

queue = deque([start_node])
visited[start_node] = True

# BFS
while queue:
    node = queue.popleft()
    if node == end_node:
        continue
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            queue.append(child)
            parent[child] = node

path = deque()
node = end_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(f"Shortest path length is: {len(path) - 1}")
print(*path, sep=" ")
