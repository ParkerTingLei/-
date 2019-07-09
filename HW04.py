class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 > 0]
                              
        
f=Solution()
re=f.sortArrayByParity([3,1,2,4])
print(re)



