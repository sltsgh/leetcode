class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        o = []
        e = []
        res = []
        for i in A:
            if i % 2 == 0:
                e.append(i)
            else:
                o.append(i)
                
        for i1, i2 in zip(e, o):
            res.append(i1)
            res.append(i2)
            
        return res
