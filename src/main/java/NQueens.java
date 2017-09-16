import java.util.ArrayList;
import java.util.List;

/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   11/10/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   11/10/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class NQueens {


    public List<List<String>> solveNQueens(int n) {
        int[][] board = new int[n][n];
        List<List<String>> result = new ArrayList<List<String>>();
        nqueens(board, 0, result);
        return result;
    }

    public void nqueens(int[][] board, int line, List<List<String>> result) {
        int n = board.length;
        if (line == n) {
            addBoard(board, result);
            return;
        }
        boolean flag = false;
        for (int j = 0; j < board[line].length; j++) {
            if (board[line][j] == 0) {
                flag = true;
                int[][] newBoard = new int[n][n];
                for (int k = 0; k < n; k++) {
                    for (int l = 0; l < n; l++) {
                        newBoard[k][l] = board[k][l];
                    }
                }
                newBoard[line][j] = 1;
                update(newBoard, line, j);
                nqueens(newBoard, line + 1, result);
            }
        }
        if (!flag) {
            return;
        }
    }

    public void addBoard(int[][] board, List<List<String>> result) {
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < board.length; i++) {
            StringBuilder stringBuilder = new StringBuilder();
            for (int j = 0; j <  board[i].length; j++) {
                if (board[i][j] == 1) {
                    stringBuilder.append("Q");
                } else {
                    stringBuilder.append(".");
                }
            }
            list.add(stringBuilder.toString());
        }
        result.add(list);
    }

    public void update(int[][] board, int x, int y) {
        for (int i = x + 1; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (j == y) {
                    board[i][j] = -1;
                } else if (Math.abs(x - i) == Math.abs(y - j)) {
                    board[i][j] = -1;
                }
            }
        }
    }

    public static void main(String[] args) {
        NQueens nQueens = new NQueens();
        List<List<String>> result = nQueens.solveNQueens(11);
        System.out.println(result.size());
    }
}
