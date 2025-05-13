class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # if we are looking at the shortest path it makes sense to use a bfs
        # and 8 directionally means we can move diagonally
        # we start from the left
        visited = set()
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [1, -1],
            [1, 1],
            [-1, 1],
            [-1, -1],
        ]
        # im going t
        queue = deque([(0, 0, 1)])

        while queue:
            r, c, length = queue.popleft()
            if r == n - 1 and c == n - 1:
                return length
            for dr, dc in directions:
                if (
                    min(dr + r, dc + c) < 0
                    or max(dr + r, dc + c) >= n
                    or grid[dr + r][dc + c] == 1
                    or (dr + r, dc + c) in visited
                ):
                    continue
                queue.append((dr + r, dc + c, length + 1))
                visited.add((dr + r, dc + c))
        return -1