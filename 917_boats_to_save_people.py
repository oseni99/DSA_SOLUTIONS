class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # its like if the smallest person and that max person can fit a boat of max two people then its good to go
        people.sort()
        l = 0
        r = len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            # the boats will take someone regardless
            # the right will move anytime also as the heaviest can be inside a boat
            boats += 1
            r -= 1
        return boats