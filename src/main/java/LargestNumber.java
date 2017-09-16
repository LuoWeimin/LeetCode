import java.util.Arrays;
import java.util.Comparator;

/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   2/15/17
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   2/15/17
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class LargestNumber {

    public String largestNumber(int[] nums) {
        String[] strings = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strings[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(strings, new SelfComparator());
        StringBuilder stringBuilder = new StringBuilder();
        for (String s : strings) {
            stringBuilder.append(s);
        }
        String result = stringBuilder.toString();
        while (result.startsWith("0") && result.length() > 1) {
            result = result.substring(1);
            if (result.length() == 1) {
                return result;
            }
        }
        return result;
    }

    private class SelfComparator implements Comparator {
        public int compare(Object o1, Object o2) {
            String c1 = (String) o1 + (String)o2;
            String c2 = (String) o2 + (String) o1;

            return 0 - c1.compareTo(c2);
        }

        public boolean equals(Object obj) {
            return false;
        }
    }

    public static void main(String[] args) {
        LargestNumber largestNumber = new LargestNumber();
        int[] nums = {2, 256};
        System.out.println(largestNumber.largestNumber(nums));
    }
}
