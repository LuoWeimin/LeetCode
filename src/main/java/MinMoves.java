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
public class MinMoves {
    public int minMoves(int[] nums) {
        if (nums.length == 0) return 0;
        int min = nums[0];
        int sum = 0;
        for (int n : nums) {
            min = Math.min(min, n);
            sum += n;
        }
        return sum - nums.length*min;

    }

    public static void main(String[] args) {
        MinMoves minMoves = new MinMoves();
        System.out.println(minMoves.minMoves(new int[]{}));
    }
}
