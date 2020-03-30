# Assuming all labels are numbered from 0 through n
visited = []
def read_graph(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()

    adjacency_list = {}

    for line in lines:
        line = list(map(int, line.split()))
        adjacency_list[line[0]] = line[1:]

    global visited
    visited = [False] * (len(adjacency_list) + 1)

    return adjacency_list

def dfs(graph, source):
    stack = []
    stack.append(source)

    while stack:
        s = stack[-1]
        stack.pop()

        if not visited[s]:
            print("Visiting Node", s)
            visited[s] = True

        for node in graph[s]:
            if not visited[node]:
                stack.append(node)


graph = read_graph("dfs_input.txt")
dfs(graph, 1)

