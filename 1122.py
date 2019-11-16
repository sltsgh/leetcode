class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lst = []
        for i in arr1:
            if not i in arr2:
                lst.append(i)
                
        res = []
        for l in arr2:
            for i in range(arr1.count(l)):
               res.append(l)
                
        res.extend(sorted(lst))
        return res
