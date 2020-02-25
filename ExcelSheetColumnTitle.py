class Solution:
    def convertToTitle(self, n: int) -> str:
        fi=''
        while n:
            n-=1
            div,mod=divmod(n,26)
            fi+=chr(ord('A')+mod)
            n//=26
        return fi[::-1]
        
