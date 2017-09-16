import java.util.HashMap;

/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   11/11/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   11/11/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class ArithmeticSlices {


    public int numberOfArithmeticSlices(int[] A) {
        if (A.length < 3) {
            return 0;
        }
        int size = A.length;
        int ans = 0;
        HashMap[] dp = new HashMap[size];
        for (int i = 0; i < size; i++) {
            dp[i] = new HashMap<Long, Integer>();
        }
        for (int x = 0; x < size; x++) {
            for (int y = 0; y < x; y++) {
                long delta = (long)A[x] - (long)A[y];
                if (dp[x].containsKey(delta)) {
                    dp[x].put(delta, Integer.valueOf(dp[x].get(delta).toString()) + 1);
                } else {
                    dp[x].put(delta, 1);
                }
                if (dp[y].containsKey(delta)) {
                    int dpy = Integer.valueOf(dp[y].get(delta).toString());
                    dp[x].put(delta, Integer.valueOf(dp[x].get(delta).toString()) + dpy);
                    ans += dpy;
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(System.currentTimeMillis());
        ArithmeticSlices arithmeticSlices = new ArithmeticSlices();
        int [] A = new int[100];
        for (int i = 0; i < A.length; i++) {
            A[i] = 1;
        }
        System.out.println(arithmeticSlices.numberOfArithmeticSlices(new int[]{2,4,6,8,10}));
        System.out.println(System.currentTimeMillis());
    }


}
