import java.util.*;

/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   11/9/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   11/9/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        if (n == 0) {
            return null;
        }
        ArrayList<String> result = new ArrayList<String>();
        build("", n, n, result);
        return result;
    }

    public void build(String current, int left, int right, ArrayList<String> result) {
        if (left != 0) {
            if (left < right) {
                build(current + "(", left - 1, right, result);
                build(current + ")", left, right - 1, result);
            } else if (left == right){
                build(current + "(", left - 1, right, result);
            } else {
                build(current + ")", left, right - 1, result);
            }
        } else {
            for (int i = 0; i < right; i++) {
                current += ")";
            }
            result.add(current);
        }
    }

    public static void main(String[] args) {
        GenerateParentheses generateParentheses = new GenerateParentheses();
        System.out.println(System.currentTimeMillis());
        System.out.println(generateParentheses.generateParenthesis(15));
//        generateParentheses.generateParenthesis(15);
        System.out.println(System.currentTimeMillis());
    }
}
