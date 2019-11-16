class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ft = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        number = ord("a") - 97

        res = []
        for i in words:
            lst = [ft[ord(l) - 97] for l in i]
            concat = ''.join(lst)
            if not concat in res:
                res.append(concat)
                
        return len(res)
