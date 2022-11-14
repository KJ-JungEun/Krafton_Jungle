import sys

sys.setrecursionlimit(10**5)

def dfs(x=1):
    visited[x] = True
    for j in tree[x]:
        if not visited[j]:
            parent[j] = x
            dfs(j)
    return

n = int(input())

tree = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
parent = [False for _ in range(n+1)]

for _ in range(1,n):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

for i in range(n+1):
    tree[i].sort()

dfs(1)
for i in range(2,n+1):
    print(parent[i])
