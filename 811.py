class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}
        for i in cpdomains:
            row = i.split(' ')
            fqdn = row[1].split('.')
            for i in range(len(fqdn)):
                domain = ".".join(fqdn[i:])
                if domain in res.keys():
                    res[domain] += int(row[0])
                else:
                    res[domain] = int(row[0])
            
        return ['{} {}'.format(str(res[i]), i) for i in res.keys()]
