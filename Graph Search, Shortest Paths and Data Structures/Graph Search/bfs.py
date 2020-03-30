def bfs(graph, source):
    queue = []
    visited = [source]
    queue.append(source)
    while queue:
        current_node = queue.pop(0)
        for i in graph[current_node]:
            if i not in visited:
                print("Exploring node", i)
                visited.append(i)
                queue.append(i)


def bfs_paths(graph, source):
    queue = []
    visited = [source]
    distance = {}
    distance[source] = 0
    queue.append(source)
    while queue:
        current_node = queue.pop(0)
        for i in graph[current_node]:
            if i not in visited:
                distance_from_source = distance[current_node] + 1
                distance[i] = distance_from_source
                print("Exploring node", i)
                print("distance from source: ", distance_from_source)
                visited.append(i)
                queue.append(i)



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

graph = read_graph('bfs_input.txt')
bfs(graph,1)
