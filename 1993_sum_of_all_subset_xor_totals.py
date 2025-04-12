class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #  i now understand what the xor means and it just means that when we get the subset we do the xor and we sum it together
        # now in python to get the xor we just have to do the num ^ the other number
        # it makes sense to now do it in this sense that as im going through the recursion stack/backtracking
        # im just adding the xor together so its pretty easy for me

        def dfs(i, total):
            # base case
            if i == len(nums):
                return total

            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)

        return dfs(0, 0)