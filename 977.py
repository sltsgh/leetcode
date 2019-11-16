class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        lst = []
        for i in A:
            lst.append(i ** 2)
            
        lst.sort()
        return lst
        