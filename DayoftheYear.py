'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.

'''


class Solution:
    def dayOfYear(self, date: str) -> int:
        year,mon,day=int(date[:4]),int(date[5:7]),int(date[8:])
        ans=0
        d=[31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(1,mon):
            if i&1: #odd
                ans+=d[i-1]
            else:
                if i==2 and ((year%4==0) and (year%100!=0 or year%400==0)):
                    ans+=29
                elif i==2:
                    ans+=d[i-1]
                else:
                    ans+=d[i-1]
            #print(ans)
        return ans+day