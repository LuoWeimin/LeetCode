/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   1/18/17
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   1/18/17
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class SpiralMatrix {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int direct = 1;
        int x = 0;
        int y = 0;
        int count = 0;
        int total = n * n;
        while (++count <= total) {
            if (x >= 0 && x < n && y >= 0 && y < n && matrix[x][y] == 0) {
                matrix[x][y] = count;
                switch (direct) {
                    case 1://right
                        y++;
                        break;
                    case 2://left
                        y--;
                        break;
                    case 3:
                        x++; //down
                        break;
                    case 4: //up
                        x--;
                        break;
                }
            } else if (y == n && direct == 1){
                y--;
                x++;
                matrix[x][y] = count;
                x++;
                direct = 3;
            } else if (x == n && direct == 3) {
                x--;
                y--;
                matrix[x][y] = count;
                y--;
                direct = 2;
            } else if (y < 0 && direct == 2) {
                y++;
                x--;
                matrix[x][y] = count;
                x--;
                direct = 4;
            } else if (matrix[x][y] != 0) {
                switch (direct) {
                    case 1:
                        direct = 3;
                        x++;
                        y--;
                        matrix[x][y] = count;
                        x++;
                        break;
                    case 2:
                        direct = 4;
                        x--;
                        y++;
                        matrix[x][y] = count;
                        x--;
                        break;
                    case 3:
                        direct = 2;
                        x--;
                        y--;
                        matrix[x][y] = count;
                        y--;
                        break;
                    case 4:
                        direct = 1;
                        x++;
                        y++;
                        matrix[x][y] = count;
                        y++;
                        break;
                }
            }
        }
        return matrix;
    }

    public static void main(String[] args) {
        SpiralMatrix spiralMatrix = new SpiralMatrix();
        int[][] matrix = spiralMatrix.generateMatrix(5);
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.printf(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
