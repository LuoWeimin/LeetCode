/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   11/18/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   11/18/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class IntegerBreak {
    public int integerBreak(int n) {
        if (n == 2) {
            return 1;
        }
        int max = Integer.MIN_VALUE;
        for (int i = 2; i < n; i++) {
            if ( n % i == 0) {
                int result = (int)Math.pow(n / i, i);
                if (result > max) {
                    max = result;
                }
            } else {
                int left = n % i;
                int result = (int)Math.pow(n / i, i - left) * (int)Math.pow(n / i + 1, left);
                if (result > max) {
                    max = result;
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        IntegerBreak integerBreak = new IntegerBreak();
        System.out.println(integerBreak.integerBreak(6));
    }
}
