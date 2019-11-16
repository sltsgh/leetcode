class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        p = None
        res = []
        for s in S:
            if s == '(' and (not p or p == ')'):
                    p = s
                    
            elif s == ')' and (res.count('(') == res.count(')')):
                    p = s

            else:
                res.append(s)
                    
        return ''.join(res)
