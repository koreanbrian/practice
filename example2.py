def dfs(graph,v,visited):
    visited[v]=True
    print(v, end=' ')

    for i in graph[v]:
        