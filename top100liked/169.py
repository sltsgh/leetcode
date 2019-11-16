class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        l = len(nums)
        for i in s:
            if nums.count(i) > (l / 2):
                return i
                