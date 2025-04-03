class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # looking right at this im thinking of having a window slide across and i get the max everytime but  i know this will be super slow
        # i can also use a heap and it will always be a max heap and ill always get the max heap so  just add it to the rres

        l = 0
        r = k - 1
        res = []
        max_heap = []
        while r < len(nums):
            for i in range(l, r + 1):
                heapq.heappush(max_heap, -(nums[i]))
            res.append(-(max_heap[0]))
            if max_heap[0] == -nums[l]:
                heapq.heappop(max_heap)
            l += 1
            r += 1
        return res