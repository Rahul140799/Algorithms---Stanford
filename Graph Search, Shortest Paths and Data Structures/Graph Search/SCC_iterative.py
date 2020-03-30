num_nodes = 875715

def read_graph(filename='SCC.txt'):
    with open(filename,'r') as file:
        lines = file.readlines()
    
    graph = [[] for i in range(num_nodes)]
    rev_graph = [[] for i in range(num_nodes)]

    for line in lines:
        nodes = line.split()
        graph[int(nodes[0])] += [int(nodes[1])]
        rev_graph[int(nodes[1])] += [int(nodes[0])]
    
    return graph,rev_graph

graph, rev_graph = read_graph()

scc = [0] * num_nodes



# DFS on reverse graph to obtain order
visited = [False] * num_nodes
stack = []
order = []
for node in range(num_nodes):
    stack.append(node)
    while stack:
        s = stack[-1]
        stack.pop()

        if not visited[s]:
            order.append(s)
            visited[s] = True

        for node in rev_graph[s]:
            if not visited[node]:
                stack.append(node)

# DFS on original graph to obtain SCCs
stack = []
visited = [False] * num_nodes
for node in reversed(order):
    stack.append(node)
    leader = node
    
    while stack:
        s = stack[-1]
        stack.pop()
        

        if not visited[s]:
            visited[s] = True
            scc[leader] += 1
        
        for node in graph[s]:
            if not visited[node]:
                stack.append(node)


for i in range(num_nodes):
    if scc[i] == 969:
        print(i)

scc.sort(reverse=True)
print(scc[:5])



