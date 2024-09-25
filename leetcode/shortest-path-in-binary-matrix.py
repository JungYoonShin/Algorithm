from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        dx = [-1, 0, 1, 0, -1, 1, -1, 1]
        dy = [0, -1, 0, 1, -1, -1, 1, 1]

        new_grid = grid[:]

        def bfs(x, y):
            queue = deque([(x, y)])
            while queue:
                now_x, now_y = queue.popleft()
                if grid[0][0] == 1:
                    return -1

                if now_x == n-1 and now_y == n-1:
                    return new_grid[n-1][n-1]+1

                for i in range(8):
                    new_x = now_x + dx[i]
                    new_y = now_y + dy[i]

                    if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                        new_grid[new_x][new_y] = new_grid[now_x][now_y] + 1
                        queue.append((new_x, new_y))

            return -1

        return bfs(0, 0)
