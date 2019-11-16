class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for i in emails:
            lst = i.split('@')
            res.add('{}@{}'.format(lst[0].split('+')[0].replace('.', ''), lst[1]))
            
        return len(res)
