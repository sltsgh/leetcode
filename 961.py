class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        rep = len(A) / 2
        dct = {}
        for i in A:
            if i in dct.keys():
                dct[i] = dct[i] + 1
            else:
                dct[i] = 1
        
        for l in dct.keys():
            if dct[l] == rep:
                return l
                