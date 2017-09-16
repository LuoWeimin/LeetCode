import java.util.Stack;

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
public class BasicCalculator {
    public int calculate(String s) {
        s = s.replaceAll(" ", "");
        Stack<Integer> num = new Stack<Integer>();
        Stack<Character> op = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ('(' == c) {
                op.push(c);
            } else if ('0' <= c && c <= '9') {
                int number = 0;
                while ('0' <= c && c <= '9') {
                    number *= 10;
                    number += c - '0';
                    i++;
                    if (i == s.length()) {
                        break;
                    }
                    c = s.charAt(i);
                }
                i--;
                num.push(number);
            } else if ('+' == c || '-' == c) {
                if (!op.empty() && (op.peek() == '+' || op.peek() == '-')) {
                    num.push(cal(num.pop(), num.pop(), op.pop()));
                }
                op.push(c);
            } else if (')' == c) {
                if (op.peek() == '(') {
                    op.pop();
                } else {
                    num.push(cal(num.pop(), num.pop(), op.pop()));
                    op.pop();
                }
            }
        }
        while (!num.empty() && !op.empty()) {
            num.push(cal(num.pop(), num.pop(), op.pop()));
        }
        return num.peek();
    }

    public int cal(int a, int b, char c) {
        if (c == '+') {
            return a + b;
        } else if (c == '-') {
            return b - a;
        }
        return 0;
    }



    public static void main(String[] args) {
        BasicCalculator basicCalculator = new BasicCalculator();
        System.out.println(basicCalculator.calculate("(1)"));
    }
}
