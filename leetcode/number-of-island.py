from collections import deque
class Solution(object):
        
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        dx = [0, -1, 1, 0]
        dy = [1, 0, 0, -1]

        def bfs(grid, x, y):
            queue = deque([(x, y)])
            while queue:
                cur_x, cur_y = queue.popleft()
            for i in range(4):
                new_x = cur_x + dx[i]
                new_y = cur_y + dy[i]
                if  (0 <= new_x < m  and 0 <= new_y < n) and grid[new_x][new_y] == "1":
                    grid[new_x][new_y] = "0"
                    queue.append((new_x, new_y))
                    bfs(grid, new_x, new_y)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    bfs(grid, i, j)
        
        return cnt



        
        
