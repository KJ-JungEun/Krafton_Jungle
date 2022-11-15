from collections import deque

def bfs_topology():
    result = []
    queue = deque()
    for i in range(1,n+1):
        if indgree[i] == 0:
            queue.append(i)

    while queue:
        
        q = queue.popleft()
        result.append(q)

        for i in graph[q]:
            indgree[i] -= 1
            if indgree[i] == 0:
                queue.append(i)

    return result

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indgree = [0] * (n+1)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    indgree[end] += 1

for out in bfs_topology():
    print(out)