from collections import deque

mtx =[]

def bfs(x = 0,y = 0):
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx<0 or ny<0 or n<=nx or m<=ny :
                continue

            if mtx[nx][ny] == 0:
                continue

            if mtx[nx][ny] == 1:
                mtx[nx][ny] = mtx[x][y] + 1
                queue.append((nx,ny))

    return mtx[n - 1][m - 1]


n, m = map(int, input().split())

for i in range(n):
    mtx.append(list(map(int,input())))

print(bfs())