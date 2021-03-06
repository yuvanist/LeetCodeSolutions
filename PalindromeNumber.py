'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        if x<0:
            return False
        else:
            if x%10==0 and x!=0:
                return False
            else:
                num=0
                i=0
                while(x):
                    num=num*10+x%10
                    i+=1
                    x//=10
                if num==temp:
                    #print(num,temp)
                    return True
                else:
                    return False
                
                    
 #Time Complexity : O(log10 n)
 #Space Complexity: O(1)
                
                
                
                
