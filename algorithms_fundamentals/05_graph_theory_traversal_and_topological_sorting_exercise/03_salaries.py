# https://judge.softuni.org/Contests/Practice/Index/3463#2

def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if not graph[node]:
        salaries[node] = 1
        return salaries[node]

    salary = 0
    for child in graph[node]:
        salary += dfs(child, graph, salaries)

    salaries[node] = salary
    return salary


nodes = int(input())

graph = []
for i in range(nodes):
    node = []
    for child, symbol in enumerate(input()):
        if symbol == "Y":
            node.append(child)
    graph.append(node)

salaries = [None] * nodes
total_salary = 0
for node in range(nodes):
    salary = dfs(node, graph, salaries)
    total_salary += salary
print(total_salary)
