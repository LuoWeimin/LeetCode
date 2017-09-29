#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preCourse = [[] for i in range(numCourses)]
        nextCourse = [[] for i in range(numCourses)]

        for pair in prerequisites:
            source = pair[0]
            target = pair[1]
            preCourse[source].append(target)
            nextCourse[target].append(source)
        alreadyList = list([])

        while True:
            flag = False
            for i in range(numCourses):
                if len(preCourse[i]) == 0 and not alreadyList.__contains__(i):
                    flag = True
                    alreadyList.append(i)
                    self.unlimit(preCourse, nextCourse, i, alreadyList)

            if not flag:
                break
        for i in range(numCourses):
            if len(preCourse[i]) != 0:
                return []
        return (alreadyList)

    def unlimit(self, preCourse, nextCourse, i, alreadyList):
        for course in nextCourse[i]:
            preCourse[course].remove(i)
            if len(preCourse[course]) == 0 and not alreadyList.__contains__(course):
                alreadyList.append(course)
                self.unlimit(preCourse, nextCourse, course, alreadyList)

s = Solution()
print s.findOrder(2, [[0, 1]])