class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            flg = True
            for l in str(i):
                if int(l) == 0 or not i % int(l) == 0:
                    flg = False
                
            if flg:
                res.append(i)
                
        return res
