class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # this is solved using the eculidean theorem of greatest common divisor 
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))
        return str1[:length]