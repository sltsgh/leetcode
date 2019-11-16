class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mzHelper(pos, cnt):
            if cnt > 0:
                if nums[pos] == 0:
                    del nums[pos]
                    nums.append(0)
                else:
                    pos += 1
                cnt -= 1
                mzHelper(pos, cnt)
            else:
                return
            
        ln = len(nums)
        mzHelper(0, ln)
    