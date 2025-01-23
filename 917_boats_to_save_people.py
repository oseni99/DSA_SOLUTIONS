class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = []
        curr_res = []
        for i in range(len(people)):
            if len(curr_res) > 0:
                rem_capacity = limit - sum(curr_res)
            else:
                rem_capacity = limit

            if people[i] <= rem_capacity:
                curr_res.append(people[i])
            else:
                res.append(curr_res)
                curr_res = [people[i]]
        if curr_res:
            res.append(curr_res)
        print(res)
        return len(res)