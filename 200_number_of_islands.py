class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # i just want to get connected islands
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def dfs(r, c):
            # when i see like one i can move 4 times
            if (
                min(r, c) < 0
                or r >= rows
                or c >= cols
                or (r, c) in visited
                or grid[r][c] == "0"
            ):
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # i should only check when i see one
                    dfs(r, c)
                    islands += 1
        return islands