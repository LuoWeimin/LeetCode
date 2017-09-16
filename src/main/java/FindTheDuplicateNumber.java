/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   2/14/17
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   2/14/17
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class FindTheDuplicateNumber {

    public int findDuplicate(int[] nums) {
        for (int i=0; i< nums.length; i++) {
            if (nums[i] == i + 1) {
                continue;
            } else if (nums[nums[i] - 1] != nums[i]) {
                int t =nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = t;
                i--;
            }
        }
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                res = nums[i];
                break;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1,3,5,5,5,5};
        FindTheDuplicateNumber findTheDuplicateNumber = new FindTheDuplicateNumber();
        System.out.println(findTheDuplicateNumber.findDuplicate(nums));

    }
}
