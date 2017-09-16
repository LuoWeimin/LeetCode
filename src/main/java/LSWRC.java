import java.util.Arrays;

/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   10/31/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   10/31/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class LSWRC {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        int start = -1, end = 0, max = 0;
        int[] lastIndex = new int[256];
        Arrays.fill(lastIndex, -1);
        for ( ; end < s.length(); end++) {
            char c = s.charAt(end);
            start = start > lastIndex[c] ? start : lastIndex[c];
            max = max > end - start ? max : end - start;
            lastIndex[c] = end;
        }
        return max;
    }

    public static void main(String[] args) {
        LSWRC lswrc = new LSWRC();
        System.out.println(System.currentTimeMillis());
        System.out.println(lswrc.lengthOfLongestSubstring("abcabcbb"));
        System.out.println(lswrc.lengthOfLongestSubstring("bbbbb"));
        System.out.println(lswrc.lengthOfLongestSubstring("pwwkew"));
        System.out.println(lswrc.lengthOfLongestSubstring("abcdefg"));
        System.out.println(lswrc.lengthOfLongestSubstring("abacadae"));
        System.out.println(lswrc.lengthOfLongestSubstring("aaaabbbbccc"));
        System.out.println(lswrc.lengthOfLongestSubstring("asdzxcaghjkfsdf"));
        System.out.println(lswrc.lengthOfLongestSubstring("a"));
        System.out.println(lswrc.lengthOfLongestSubstring("qwe"));
        System.out.println(lswrc.lengthOfLongestSubstring("asjrgapa"));
        System.out.println(System.currentTimeMillis());
    }
}
