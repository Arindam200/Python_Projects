class Solution:
    def romanToInt(self, s: str) -> int:
        lst = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        cal = 0
        for i in range(len(s)):
            if i > 0 and lst[s[i]] > lst[s[i - 1]]:
                cal += lst[s[i]] - 2 * lst[s[i - 1]]
            else:
                cal += lst[s[i]]
        return cal
