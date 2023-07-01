# https://judge.softuni.org/Contests/Practice/Index/3592#2
from collections import deque


class Edge:
    def __init__(self, first_currency, second_currency, exchange):
        self.first_currency = first_currency
        self.second_currency = second_currency
        self.exchange = float(exchange)


nodes_count = int(input())

graph = []
for _ in range(nodes_count):
    first, second, course = input().split()
    graph.append(Edge(first, second, course))

target_currency = input()

distance = {target_currency: 1}
parent = {target_currency: None}

for _ in range(nodes_count - 1):
    updated = False
    for edge in graph:
        if edge.first_currency not in distance:
            continue
        new_distance = distance[edge.first_currency] * edge.exchange
        if edge.second_currency not in distance:
            distance[edge.second_currency] = new_distance
            parent[edge.second_currency] = edge.first_currency
        elif new_distance > distance[edge.second_currency]:
            distance[edge.second_currency] = new_distance
            parent[edge.second_currency] = edge.first_currency
        updated = True
    if not updated:
        break

arbitrage_possible = False
for edge in graph:
    new_distance = distance[edge.first_currency] * edge.exchange
    if new_distance > distance[edge.second_currency]:
        arbitrage_possible = True
        break

print(arbitrage_possible)
if arbitrage_possible:
    path = deque([target_currency])
    node = target_currency
    while parent[node] != target_currency:
        path.appendleft(parent[node])
        node = parent[node]
    path.appendleft(target_currency)
    print(*path)
else:
    for currency, course in distance.items():
        print(f"{currency}: {course:.3f}")
