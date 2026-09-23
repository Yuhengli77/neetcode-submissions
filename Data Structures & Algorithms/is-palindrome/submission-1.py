class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        # now s is an array
        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


