class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def countHelper(word):
            t = set(sorted(word))
            for i in t:
                if not chars.count(i) >= word.count(i):
                    return 0
            
            return len(word)

        cnt = 0
        for i in words:
            cnt += countHelper(i)
            
        return cnt
