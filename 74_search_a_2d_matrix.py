class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first thing is its sorted so i can perform binary seach
        # i can use the fact that last element in the row is greater than last of previous row
        l = 0
        r = len(matrix) - 1
        while l <= r:
            # this is a better way to calculate middle to avoid interger overflow
            m = l + (r - l) // 2
            # the last element > target but it may still not even be in the second one
            #  imagine target 6 and last is 3 and next row beginning is 7 so it should go back
            if matrix[m][0] <= target <= matrix[m][-1]:
                #  this is when i see it and i get the row
                #  i do the binary search on that row
                row = matrix[m]
                left = 0
                right = len(row) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
            elif target < matrix[m][0]: # move up 
                r = m - 1
            else: # move down 
                l = m + 1 
        return False