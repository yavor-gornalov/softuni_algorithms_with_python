# https://judge.softuni.org/Contests/Practice/Index/3463#2

def find_salaries(node, salaries, graph):
    if salaries[node] is not None:
        return salaries[node]

    if not graph[node]:
        salaries[node] = 1
        return 1

    salary = 0
    for child in graph[node]:
        salary += find_salaries(child, salaries, graph)
    salaries[node] = salary

    return salary


employees_count = int(input())

graph = []
[graph.append([]) for _ in range(employees_count)]
for node in range(employees_count):
    line = input()
    children = [i for i in range(len(line)) if line[i] == "Y"]
    graph[node] = children if children else []

salaries = [None] * employees_count
for node in range(len(graph)):
    find_salaries(node, salaries, graph)

print(sum([x for x in salaries if x is not None]))
