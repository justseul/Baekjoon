n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

d_visited = [False] * (n+1)
def dfs(graph, v, d_visited):
    d_visited[v] = True    
    print(v, end = ' ')
    for i in sorted(graph[v]):
        if d_visited[i] == False:
            dfs(graph, i, d_visited)
            
b_visited = [False] * (n+1)

def bfs(graph, v, b_visited):
    b_list = [v]
    b_visited[v] = True
    while(b_list):
        a = b_list.pop(0)
        print(a, end = ' ')
        for i in sorted(graph[a]):
            if b_visited[i] == False:
                b_list.append(i)
                b_visited[i] = True

dfs(graph, v, d_visited)
print()
bfs(graph, v, b_visited)     