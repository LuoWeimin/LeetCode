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
public class ExcelSheetColumnTitle {
    public String convertToTitle(int n) {
        if (n <= 0) {
            return "";
        }
        StringBuilder stringBuilder = new StringBuilder();
        while (n != 0) {
            n -= 1;
            char c = (char)('A' + (n % 26));
            stringBuilder.append(c);
            n /= 26;
        }
        return stringBuilder.reverse().toString();
    }

    public static void main(String[] args) {
        ExcelSheetColumnTitle excelSheetColumnTitle = new ExcelSheetColumnTitle();
        System.out.println(excelSheetColumnTitle.convertToTitle(28));
    }
}
