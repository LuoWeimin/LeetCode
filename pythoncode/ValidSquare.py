import math

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        point = [p1, p2, p3, p4]
        i = 0
        edge = []
        other = []
        while i < len(point):
            j = i + 1
            while j < len(point):
                dis = self.distance(point[i], point[j])
                if len(edge) == 0 or dis == edge[0]:
                    edge.append(dis)
                else:
                    other.append(dis)
                j += 1
            i += 1
        if len(edge) == 4:
            if other[0] == other[1] and int(other[0] - math.sqrt(2) * edge[0]) == 0:
                return True
            else:
                return False
        elif len(edge) == 2:
            if other[0] == other[1] and other[0] == other[2] and other[0] == other[3] and int(other[0] * math.sqrt(2) - edge[0]) == 0:
                return True
            else:
                return False
        else:
            return False

    def distance(self, p1, p2):
        return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))


s = Solution()
p1 = [1, 1]
p2 = [-1, 1]
p3 = [1, -1]
p4 = [-1, -1]
print s.validSquare(p1, p3, p2, p4)
