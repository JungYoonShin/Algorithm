class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n

        def dfs(v):
            visited[v] = True
            for key in rooms[v]:
                if not visited[key]:
                    dfs(key)
        dfs(0)

        for v in visited:
            if v == False:
                return False
        return True


        
        
