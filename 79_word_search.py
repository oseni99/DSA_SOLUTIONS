class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # this is basically a situation where i treat it as a point where i can go either 4 ways
        # either up down left right
        # if i dont see the letter and im moving already i just backtrack
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            # where it goes out of bounds and not equal to it
            if r < 0 or r >= rows or c >= cols or c < 0 or board[r][c] != word[i]:
                return False

            # if i find the word
            letter = board[r][c]
            # mark it as visited
            board[r][c] = "#"
            # i can move 4 points from that to do my next dfs
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1)
            )
            # if im at the end or i cant now see it i backtrack change that point back to its letter
            board[r][c] = letter
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False