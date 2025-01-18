class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # i can now take a number and do 3sum on it
        #  now add everything inside the result
        new_nums = sorted(nums)
        def three_sum(arr, new_target):
            three_sum_res = []
            for i in range(len(arr)):
                #  checking for unique should be here i +1 and i
                if i > 0 and arr[i] == arr[i - 1]:
                    continue
                l = i + 1
                r = len(arr) - 1
                while l < r:
                    total = arr[i] + arr[l] + arr[r]
                    if total == new_target:
                        three_sum_res.append([arr[i], arr[l], arr[r]])
                        l += 1
                        r -= 1 

                        while l < r and arr[l] == arr[l - 1]:
                            l += 1
                        while l < r and arr[r] == arr[r + 1]:
                            r -= 1
                    elif total < new_target:
                        l += 1
                    else:
                        r -= 1
            return three_sum_res

        total_res = []
        for i in range(len(new_nums)):
            if i > 0 and new_nums[i] == new_nums[i - 1]:
                continue
            # print(target - new_nums[i])
            new_target = target - new_nums[i]
            a = three_sum(new_nums[i + 1 :], new_target)
            for s in a:
                if len(s) > 0:
                    s.append(new_nums[i])
                    total_res.append(s)
        return total_res