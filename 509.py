class Solution:
    def fib(self, N: int) -> int:
        lst = [0, 1]
        for i in range(1, N):
            lst.append(lst[-2] + lst[-1])

        return lst[N]
