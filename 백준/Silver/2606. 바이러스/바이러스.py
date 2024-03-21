def bfs(x, graph):
    b_list = [x]
    while b_list:
        v = b_list.pop(0)
        infected[v] = True
        for i in sorted(graph[v]):
            if infected[i] == False:
                infected[i] = True
                b_list.append(i)

    return infected.count(True)-1
                
                

n = int(input())
pair = int(input())
graph = list([] for _ in range(n+1))
infected = [0] * (n+1)
for i in range(pair):
    c1, c2 = map(int, input().split())
    graph[c2].append(c1)
    graph[c1].append(c2)


print(bfs(1, graph))