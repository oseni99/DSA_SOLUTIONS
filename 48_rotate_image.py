class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose the matrix
        for i in range(n):
            for j in range(i, n):
                # swapping the value in the both positions in place together
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for x in matrix:
            # numpy doesnt work with reverse but it works here cux it would have to be matrix[:,::-1]
            x.reverse()