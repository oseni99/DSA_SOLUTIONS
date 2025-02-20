class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # this is the base case
        if len(t) > len(s):
            return ""
        #  im still thinking throw it into a hashmap after each slide
        #  check if t is in there
        # turn it into a list
        new_s, new_t = list(s), list(t)
        n = len(new_t)
        res = s
        l, r = 0, n

        # define the helper function to check it in a hashmap
        def checker(hash_char):
            for i in new_t:
                if i not in hash_char.keys():
                    return False
            return True

        while r < len(new_s):
            # throw it inside the hashmap
            a = Counter(new_s[l : r + 1])
            if checker(a):
                c = "".join(new_s[l : r + 1])
                res = min(c,res,key=len)
                l += n 
                r = l + n
            else:
                r += 1
        return res