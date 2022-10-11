
def romanToInt(self, s: str) -> int:
        maps = {'I' : 1,'V' : 5,'X' : 10,
        'L' : 50,'C' : 100,'D' : 500,'M' : 1000}
        sums = 0
        i = 0
        while i < len(s)-1:
            if maps[s[i]] < maps[s[i+1]]:
                sums += maps[s[i+1]]-maps[s[i]]
                i += 1
            else:
                sums += maps[s[i]]
            i += 1
        if i != len(s):
            sums += maps[s[-1]]
        return sums
