class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        res = []
        L = len(words)
        for i in range(L - 2):
            f, s, t = words[i], words[i + 1], words[i + 2]
            if f == first and s == second:
                res.append(t)
        return res
