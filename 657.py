class Solution:
    def judgeCircle(self, moves: str) -> bool:
        p = [0, 0]
        for i in moves:
            if i == 'U':
                p[0] += 1
            elif i == 'D':
                p[0] -= 1
            elif i == 'L':
                p[1] += 1
            else:
                 p[1] -= 1
            
        return p == [0, 0]
