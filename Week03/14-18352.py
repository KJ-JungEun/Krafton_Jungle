from collections import deque

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
far = [0 for _ in range(n+1)]
flag = False

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] += 1

    while len(queue) > 0:

        p = queue.popleft()

        for i in graph[p]:

            if not visited[i]:
                visited[i] = True
                far[i] = far[p] + 1
                queue.append(i)
    
    return

bfs(x)

for i in range(1,len(far)):
    if far[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)