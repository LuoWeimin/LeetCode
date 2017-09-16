import java.util.ArrayList;
import java.util.List;

/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   11/19/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   11/19/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class SummaryRanges {
    public List<String> summaryRanges(int[] nums) {
        List<String> list = new ArrayList<String>();
        int start = 0;
        int end = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i + 1] - nums[i] != 1) {
                end = i;
                StringBuilder stringBuilder = new StringBuilder();
                if (end - start == 0) {
                    stringBuilder.append(nums[start]);
                } else {
                    stringBuilder.append(nums[start]).append("->").append(nums[end]);
                }
                list.add(stringBuilder.toString());
                start = i + 1;
            }
        }
        if (start < nums.length - 1) {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append(nums[start]).append("->").append(nums[nums.length - 1]);
            list.add(stringBuilder.toString());
        } else if (start == nums.length - 1) {
            list.add(String.valueOf(nums[nums.length - 1]));
        }
        return list;
    }

    public static void main(String[] args) {
        SummaryRanges summaryRanges = new SummaryRanges();
        int[] array = new int[1000000];
        for (int i = 0; i < array.length; i++) {
            array[i] = 2 * i;
        }
        System.out.println(summaryRanges.summaryRanges(array));
    }
}
