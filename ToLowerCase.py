'''

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
'''

class Solution:
    def toLowerCase(self, str: str) -> str:
        s=list(str)
        for i in range(len(s)):
            if 65<=ord(s[i])<=90:
                s[i]=chr(ord(s[i])+32)
        return ''.join(s)
        
        
#Time Complexity : O(n)
#Space Complexity : O(n)
