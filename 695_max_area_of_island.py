class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # i think this is basically just like the number of islands
        # im looking for ones that are connected which is island
        # i need a visited to mark what ive visited so i dont check it also

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            # base case if not island
            if (
                min(r, c) < 0
                or r >= rows
                or c >= cols
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            # move 4 places
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    max_area = max(area, max_area)
        return max_area