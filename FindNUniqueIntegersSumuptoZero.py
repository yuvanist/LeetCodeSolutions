'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000

'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        final=[]
        if n&1:
            cnt=0
            for i in range(1,n+1):
                if i&1:
                    final.append(-1*cnt)
                    cnt+=1
                else:
                    final.append(cnt)
        else:
            cnt=1
            for i in range(1,n+1):
                if i&1:
                    final.append(cnt)
                else:
                    final.append(-1*cnt)
                    cnt+=1
        return final
                
            
#Time Complexity: O(n)
#Space Complexity: O(n)
            
            
            
