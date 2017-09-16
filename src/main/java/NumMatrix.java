/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   12/9/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   12/9/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class NumMatrix {

    int[][] sums;

    public NumMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }
        sums = new int[matrix.length][matrix[0].length];
        sums[0][0] = matrix[0][0];
        for (int i = 1; i < matrix[0].length; i++) {
            sums[0][i] = sums[0][i - 1] + matrix[0][i];
        }
        for (int i = 1; i < matrix.length; i++) {
            sums[i][0] = sums[i - 1][0] + matrix[i][0];
        }
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[i].length; j++) {
                sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + matrix[i][j];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        if (row2 > sums.length || col2 > sums[0].length) {
            return 0;
        }
        if (row1 > 0 && col1 > 0) {
            return sums[row2][col2] - sums[row1 - 1][col2] - sums[row2][col1 - 1] + sums[row1 - 1][col1 - 1];
        } else if (row1 == 0 && col1 > 0) {
            return sums[row2][col2] - sums[row2][col1 - 1];
        } else if (col1 == 0 && row1 > 0) {
            return sums[row2][col2] - sums[row1 - 1][col2];
        } else {
            return sums[row2][col2];
        }
    }

    public static void main(String[] args) {
//        int[][] matrix = {
//                {3, 0, 1, 4, 2},
//                {5, 6, 3, 2, 1},
//                {1, 2, 0, 1, 5},
//                {4, 1, 0, 1, 7},
//                {1, 0, 3, 0, 5}
//        };
        int[][] matrix = {
                {1},
                {-7}
        };
        NumMatrix numMatrix = new NumMatrix(matrix);
//        System.out.println(numMatrix.sumRegion(2,1,4,3));
//        System.out.println(numMatrix.sumRegion(1,1,2,2));
//        System.out.println(numMatrix.sumRegion(1,2,2,4));
        System.out.println(numMatrix.sumRegion(0,0,0,0));
        System.out.println(numMatrix.sumRegion(0,0,1,0));
        System.out.println(numMatrix.sumRegion(1,0,1,0));
//        System.out.println(numMatrix.sumRegion(1,1,1,1));
//        System.out.println(numMatrix.sumRegion(0,0,0,1));
    }
}
