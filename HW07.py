class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            name, domain = email.split("@")
            print("name="+name+"/n/n")
            print("domain="+domain)
            
            name = name.split("+")[0].replace(".", "")
            print("name="+name)
            res.add(name + "@" + domain)
            print(res)
        return len(res)
f=Solution()
re=f.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(re)
