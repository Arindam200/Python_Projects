class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        if(st == st[::-1]):
            return True
        else:
            return False
