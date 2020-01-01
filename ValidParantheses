'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                try:
                    if i=='}' and stack[-1]=='{':
                        stack=stack[:-1]
                    elif i==']' and stack[-1]=='[':
                        stack=stack[:-1]
                    elif i==')' and stack[-1]=='(':
                        stack=stack[:-1]
                    else:
                        return False
                except:
                    return False
        if not len(stack):
            return True
            
 #Time Complexity : O(n)
 #Space Complexty: O(n)
            
            
