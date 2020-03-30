def read_graph(filename):
    with open(filename,'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    
    adjacency_list = {}

    for line in lines:
        line = list(map(int,line.split()))
        adjacency_list[line[0]] = line[1:]

    return adjacency_list

visited = []
stack = []

def dfs(graph,source):
    if source not in visited:
        visited.append(source)
        print("Visiting",source)
        for neighbour in graph[source]:
            dfs(graph,neighbour)
        stack.append(source)

def topological_sort(graph):
    for node in graph:
        if node not in visited:
            dfs(graph,node)