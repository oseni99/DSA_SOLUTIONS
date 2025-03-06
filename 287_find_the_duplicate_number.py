class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #  the hare and tortoise algorithm can work here 
        # the way this will move is different as it depends on the numbers as the index
        # it uses this number to check instead of pointers in LL
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break # this cycle detects here and breaks out of the loop 
        
        # this is where cycle starts and you get duplicate 
        slow = nums[0] 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow