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
public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        if (s == null) {
            return false;
        }
        int i = 0;
        int j = s.length() - 1;
        while (i <= j) {
            char c = s.charAt(i);
            while (!alpha(c)) {
                i++;
                if (i == s.length()) {
                    return true;
                }
                c = s.charAt(i);
            }
            char h = s.charAt(j);
            while (!alpha(h)) {
                j--;
                h = s.charAt(j);
            }
            if (!(c == h || (Math.abs(c - h) == 'a' - 'A') && (c >= 'A' && h >= 'A'))) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public boolean alpha(char c) {
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        ValidPalindrome validPalindrome = new ValidPalindrome();
        System.out.println(validPalindrome.isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(validPalindrome.isPalindrome("A a"));
        System.out.println(validPalindrome.isPalindrome(" "));
        System.out.println(validPalindrome.isPalindrome("0P"));
    }
}
