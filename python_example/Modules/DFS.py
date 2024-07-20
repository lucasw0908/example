# DFS.py
visited = [False] * 1000
def dfs(graph: list[list[int]], cur: int=1, deep: int=1) -> int:
    if visited[cur]:
        return deep
    visited[cur] = True
    deeps = [deep]
    for i in graph[cur]:
        deeps.append(dfs(graph, i, deep + 1))
    return max(deeps)