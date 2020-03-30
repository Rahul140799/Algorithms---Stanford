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

def bfs(graph, source):
    queue = []
    visited = [source]
    queue.append(source)
    while queue:
        current_node = queue.pop(0)
        for i in graph[current_node]:
            if i not in visited:
                # print("Can reach node", i)
                visited.append(i)
                queue.append(i)
    return visited

def find_connected_components(graph):
    explored = []
    i = 1
    for key in graph:
        if key not in explored:
            components = bfs(graph,key)
            explored.extend(components)
            print("Component {}: {}" .format(i,components))
            i+=1
        
