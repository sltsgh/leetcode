class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            if i in dct.keys():
                dct[i] += 1
            else:
                dct[i] = 1
                
        for i in dct:
            if dct[i] == 1:
                return i
            