class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return False
        l = len(s)
        for i in range(1, l):
            if s[i] == s[0]:
                if l % i == 0:
                    if self.checkIfRepeat(s, i):
                        return True
        return False

    def checkIfRepeat(self, s, l):
        r = len(s) / l
        for i in range(l):
            for j in range(r):
                if s[i] != s[j * l + i]:
                    return False
        return True

s = Solution()
print s.repeatedSubstringPattern("abcabcabc")
print s.repeatedSubstringPattern("aaaaaaa")
print s.repeatedSubstringPattern("abababab")
print s.repeatedSubstringPattern("abccbaabcaa")
print s.repeatedSubstringPattern("asdasfqwdasdsadqwdasd")