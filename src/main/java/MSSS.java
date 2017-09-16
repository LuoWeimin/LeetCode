/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   12/13/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   12/13/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class MSSS {
    public int minSubArrayLen(int s, int[] nums) {
        int start = 0;
        int minLength = Integer.MAX_VALUE;
        int sum = 0;
        boolean flag = false;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sum >= s) {
                flag = true;
                int length = i - start + 1;
                if (length < minLength) {
                    minLength = length;
                }
                while (sum >= s) {
                    sum -= nums[start++];
                    length = i - start + 1;
                    if (length < minLength && sum >= s) {
                        minLength = length;
                    }
                }
            }
        }
        if (flag) {
            return minLength;
        } else {
            return 0;
        }
    }

    public static void main(String[] args) {
        int[] array = new int[]{2,3,1,2,4,3};
        MSSS msss = new MSSS();
        System.out.println(msss.minSubArrayLen(4, array));
    }
}
