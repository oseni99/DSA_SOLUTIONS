class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # max capacity is the sum of all the weights i can add 
        #  minimum is the max of the weights 
        #  each capacity has to be in some sort of equal to that days 
        l = max(weights)
        r = sum(weights)
        while l < r:
            curr_days = 1 
            curr = 0 
            m = (l+r) // 2 
            for i in weights: 
                if curr + i > m:
                    curr_days += 1 
                    curr = 0 
                curr += i 
            if curr_days > days:
                l = m + 1 
            else:
                r = m 
        return l