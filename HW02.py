class Solution(object):
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)
        res = 0
        for v1,v2 in zip(heights,sorted_heights):
            res += 1 if v1 != v2 else  0
        return res
f=Solution()

print(f.heightChecker([1,1,4,2,1,3]))