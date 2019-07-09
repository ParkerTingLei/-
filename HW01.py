class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num=0
        for x in S:
            if x in J:
              num = num+1  
        
        return num
        
        
f=Solution()


print(f.numJewelsInStones("z","ZZ"))