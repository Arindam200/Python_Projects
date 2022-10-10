class Solution:
    def isHappy(self, n: int) -> bool:
        pst = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in pst:
                return False
            pst.add(n)
        return True
