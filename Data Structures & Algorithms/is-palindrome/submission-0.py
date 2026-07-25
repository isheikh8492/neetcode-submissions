import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True
        