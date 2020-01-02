'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Note:

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.


'''

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i,j=0,0
        final=[]
        while i<len(A) and A[i]<0:
            i+=1
        j=i-1
        while(i<len(A) and j>=0):
            if A[i]<-1*A[j]:
                final.append(A[i]*A[i])
                i+=1
            else:
                final.append(A[j]*A[j])
                j-=1
        while(i<len(A)):
            final.append(A[i]*A[i]);i+=1
        while(j>=0):
            final.append(A[j]*A[j]);j-=1
        return final
        
        
        
        
#Two Pointers
#Time Complexity : O(n)
#Space Complexity : O(1)

        
