class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        my_s = ""
        for ch in s.lower():
            if ch.isalnum():
                my_s += ch
        
        left = 0
        right = len(my_s) - 1

        while left < right:
            if my_s[left] != my_s[right]:
                return False

            left += 1
            right -= 1

        return True
        