'''
 A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:

Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.

'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        final=[]
        for i in range(left,right+1):
            i=str(i)
            if '0' not in i:
                for j in i:
                    if int(i)%int(j):
                        break
                else:
                    final.append(int(i))
        return final
        
 #Time Complexity : O(n*m)
 #Space Complexity: O(n)
