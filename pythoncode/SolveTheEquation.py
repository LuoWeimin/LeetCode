#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        xcount = 0
        res = 0
        stack = []
        p = True
        e = False
        equation += '$'
        for s in equation:
            if s == '+' or s == '-' or s == '=' or s == 'x' or s == '$':
                ex = ''

                while stack:
                    ex += stack[0]
                    stack.remove(stack[0])
                if s == 'x':
                    factor = 1
                    if ex != '':
                        factor = int(ex)
                    if p:
                        xcount += factor
                    else:
                        xcount -= factor
                else:
                    if ex != '':
                        if p:
                            res += int(ex)
                        else:
                            res -= int(ex)
                if s == '=':
                    e = True
                if s == '-':
                    p = False
                else:
                    p = True
                if e:
                    p = not p
            else:
                stack.append(s)
        if xcount == 0 and res == 0:
            return "Infinite solutions"
        elif xcount == 0:
            return "No solution"
        else:
            return 'x=' + str(-res / xcount)

s = Solution()
# print s.solveEquation("x+5-3+x=6+x-2")
# print s.solveEquation("x=x")
# print s.solveEquation("2x=x")
# print s.solveEquation("2x+3x-6x=x+2")
# print s.solveEquation("x=x+2")
print s.solveEquation("x=100")


