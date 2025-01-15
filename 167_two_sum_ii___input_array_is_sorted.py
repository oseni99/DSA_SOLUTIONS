class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i can use normal two pointers but can be faster with binary search
        for i in range(len(numbers)):
            complement = target - numbers[i]
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                m = (l + r) // 2
                if numbers[m] == complement:
                    return [i + 1, m + 1]
                elif numbers[m] < complement:
                    l = m + 1
                else:
                    r = m - 1