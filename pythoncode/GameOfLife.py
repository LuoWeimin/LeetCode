#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                neighbors = self.neighbor(i, j, board)
                print neighbors
                if board[i][j] & 1 == 1:
                    if neighbors == 2 or neighbors == 3:
                        board[i][j] = 3
                    else:
                        board[i][j] = 1
                else:
                    if neighbors == 3:
                        board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] >>= 1

    def neighbor(self, x, y, board):
        sum = 0
        for i in range(max(x - 1, 0), min(x + 2, len(board))):
            for j in range(max(y - 1, 0), min(y + 2, len(board[i]))):
                sum += board[i][j] & 1
        sum -= board[x][y] & 1
        return sum

s = Solution()
board = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
s.gameOfLife(board)
print board