class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # find the max number whoch is the peak
        # find the index
        # now split the array into strictly increasing
        # strictly decreasing the other side
        peak_idx = arr.index(max(arr))
        ct = 0
        # this means if theres peak at beginning or end no mountain
        if peak_idx == len(arr) - 1 or peak_idx == 0:
            return False
        if len(arr) < 3:
            return False
        # strictly increasing is left array
        for i in range(1, peak_idx + 1):
            if arr[i] <= arr[i - 1]:
                ct += 1
        # stritly decreasing is right array
        for i in range(peak_idx + 1, len(arr)):
            if arr[i] >= arr[i - 1]:
                ct += 1
        return True if ct == 0 else False