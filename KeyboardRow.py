'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

 



 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r=['qwertyuiopQWERTYUIOP','ASDFGHJKLasdfghjkl','ZXCVBNMzxcvbnm']
        final=[]
        for i in words:
            for j in r:
                if len(set(i)-set(j))==0:
                    final.append(i)
        return final
            
#Time Complexity: O(n)
#Space Complexity : O(n)
            
        
