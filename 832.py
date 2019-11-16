class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        tmp = []
        for i in A:
            lst = [n for n in A]
            num = len(i)
            for n, l in enumerate(i):
                lst[num - n - 1] = l
                
            tmp.append(lst)
        
        res = []
        for i in tmp:
            for n, l in enumerate(i):
                if l == 1:
                    i[n] = 0
                else:
                    i[n] = 1
                    
            res.append(i)
            
        return res
