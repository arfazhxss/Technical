class Solution:
    # Cheating Solution
    # def isPalindrome (self, s: str) -> bool:
    #     newStr = ""

    #     for c in s:
    #         if c.isalnum():
    #             newStr += c.lower()
        
    #     return newStr == newStr[::-1]
    
    # Memory Efficient Solution
    def isPalindrome (self, s: str) -> bool:
        l, r = 0, len(s) - 1

        # case when there's a non-alphaneumeric
        while l < r and not self.alphaNum(s[l]):
            l += 1

        # case when there's a non-alphaneumeric
        while r > 1 and not self.alphaNum(s[r]):
            r -= 1

        while l < r:
            if s[l].lower() != s[r].lower():
                return False
        
        l, r = l + 1, r - 1

        return True

    def alphaNum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord(0) <= ord(c) <= ord(9)))