class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        if len(s) == 2:
            return s[0] == s[1]
        elif len(s) == 3:
            return s[0] == s[1] or s[2] == s[0] or s[2] == s[1] or s[2] == s[0]
        
        start = 0
        end = len(s) - 1
        delete = False
        
        while end > start:
            if s[start] == s[end]:
                start += 1
                end -=  1
            else:
                if not delete:
                    end -= 1
                else:
                    end -= 1
                    return False
        return True
        