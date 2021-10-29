##DFS 정답 필사

N, M =map(int, input().split())

graph =[]

for i in range(N):
    graph.append(list(map(int, input())))




def dfs(graph, i, j):
    if i < 0 or j < 0 or i > N -1 or j > M -1:
        return False
        
    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(graph, i-1, j)
        dfs(graph, i+1, j)
        dfs(graph, i, j - 1)
        dfs(graph, i, j + 1)
        return True
    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(graph, i ,j) == True:
            count += 1
print(count)

