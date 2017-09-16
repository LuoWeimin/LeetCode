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
public class NumberComplement {
    public int findComplement(int num) {
        int m = 0;
        int temp = num;
        while (temp != 0) {
            temp /= 2;
            m++;
        }
        int result =  (int)(Math.pow(2, m) - 1) - num;
        return result;
    }

    public static void main(String[] args) {
        NumberComplement numberComplement = new NumberComplement();
        System.out.println(numberComplement.findComplement(2147483647));
    }
}
