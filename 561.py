class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        for n, i in enumerate(sorted(nums), 1):
            if not n % 2 == 0:
                res += i
                
        return res
