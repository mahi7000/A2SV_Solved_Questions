class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)

        for domain in cpdomains:
            count, acc_domain = domain.split()
            d = acc_domain.split('.')
            domains[acc_domain] += int(count)
            if len(d) == 3:
                domains[d[1] + '.' + d[2]] += int(count)
            domains[d[-1]] += int(count)

        domain = []

        for acc_domain, count in domains.items():
            domain.append(str(count) + " " + acc_domain)

        return domain
