class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for i in arr:
            if i in dict.keys():
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
        
        lst = []
        for i in dict.values():
            if i in lst:
                return False
            else:
                lst.append(i)
                
        return True
    