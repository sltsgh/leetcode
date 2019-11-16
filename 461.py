class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x > y:
            n_1 = y
            n_2 = x
        else:
            n_1 = x
            n_2 = y
            
        x_s = str(bin(n_1))[2:]
        y_s = str(bin(n_2))[2:]
        x_s_d = '{}{}'.format('0' * (len(y_s) - len(x_s)), x_s)
        res = 0
        for n, i in enumerate(x_s_d):
            if not y_s[n] == i:
                res += 1
                
        return res
    