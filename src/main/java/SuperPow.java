/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   1/18/17
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   1/18/17
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class SuperPow {
    public int superPow(int a, int[] b) {
        if (b.length == 1) {
            int result = 1;
            for (int i = 0; i < b[0]; i++) {
                result = result * (a % 1337) % 1337;
            }
            return result;
        } else {
            int result = 1;
            for (int i = 0; i < 10; i++) {
                result = result * (a % 1337) % 1337;
            }

            int[] tenM = new int[b.length - 1];
            tenM[0] = result;
            for (int i = 1; i < tenM.length; i++) {
                tenM[i] = 1;
                for (int j = 0; j < 10; j++) {
                    tenM[i] = tenM[i] * tenM[i - 1] % 1337;
                }
            }

            int finalResult = 1;
            for (int i = 0; i < b.length - 1; i++) {
                finalResult = finalResult * ((pow(tenM[b.length - i - 2], b[i])) % 1337);
            }
            for (int i = 0; i < b[b.length - 1]; i++) {
                finalResult = finalResult * (a % 1337) % 1337;
            }
            return finalResult;
        }
    }

    public int pow(int a, int b) {
        int result = 1;
        for (int i = 0; i < b; i++) {
            result = result * (a % 1337) % 1337;
        }
        return result;
    }

    public static void main(String[] args) {
        SuperPow superPow = new SuperPow();
        System.out.println(superPow.superPow(2147483647, new int[]{2,0,0}));
    }
}
