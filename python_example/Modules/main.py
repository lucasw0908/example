import DFS # 匯入DFS.py

graph = [[], [2, 3], [4, 5], [6, 7], [], [], [], []]
print(DFS.dfs(graph)) # 使用DFS底下的dfs函數

# ================================
from DFS import dfs # 匯入DFS.py的dfs函數

graph = [[], [2, 3], [4, 5], [6, 7], [], [], [], []]
print(dfs(graph)) # 直接使用dfs函數