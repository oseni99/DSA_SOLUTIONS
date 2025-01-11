class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # basically allows us to simulate remove the left and check if its a palindrome
                # or remove to right and check if its a palindrome
                # if both returns fasle means we remove two and palindrome doesnt exist
                skipLeft = isPalindrome(s, l + 1, r)
                skipRight = isPalindrome(s, l, r - 1)
                return skipLeft or skipRight
            l += 1
            r -= 1
        return True