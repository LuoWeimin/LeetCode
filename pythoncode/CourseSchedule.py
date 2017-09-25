#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import sys

sys.setrecursionlimit(100000)

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preCourse = [[] for i in range(numCourses)]
        nextCourse = [[] for i in range(numCourses)]

        for pair in prerequisites:
            source = pair[0]
            target = pair[1]
            preCourse[source].append(target)
            nextCourse[target].append(source)
        alreadyList = set([])

        while True:
            flag = False
            for i in range(numCourses):
                if len(preCourse[i]) == 0 and not alreadyList.__contains__(i):
                    flag = True
                    alreadyList.add(i)
                    self.unlimit(preCourse, nextCourse, i, alreadyList)

            if not flag:
                break
        for i in range(numCourses):
            if len(preCourse[i]) != 0:
                return False
        return True

    def unlimit(self, preCourse, nextCourse, i, alreadyList):
        for course in nextCourse[i]:
            preCourse[course].remove(i)
            if len(preCourse[course]) == 0 and not alreadyList.__contains__(course):
                alreadyList.add(course)
                self.unlimit(preCourse, nextCourse, course, alreadyList)


s = Solution()
print time.time()
print s.canFinish(10001, [[i,i+1] for i in range(10000)])
print time.time()