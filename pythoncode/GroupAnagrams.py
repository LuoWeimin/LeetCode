class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashcode = {}
	for s in strs:
		l = list(s)
		l.sort()
		code = ''.join(l)
		if code in hashcode:
			hashcode[code].append(s);
		else:
			hashcode[code] = [s]
	rs = []
	for hc in hashcode:
		rs.append(hashcode[hc])
	return rs

s = Solution()
print s.groupAnagrams(["huh","tit"])
