import java.util.ArrayList;

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
public class ValidNumber {
    public boolean isNumber(String s) {
        if (s == null || s.length() == 0 || s.trim().length() == 0
                || s.endsWith("e") || s.endsWith("E")) {
            return false;
        } else {
            s = s.trim();
            String[] sci;
            if (s.contains("e")) {
                sci = s.split("e");
            } else if (s.contains("E")) {
                sci = s.split("E");
            } else {
                sci = new String[]{s};
            }
            if (sci.length > 2 || sci.length == 0) {
                return false;
            } else {
                if (sci.length == 2 && (sci[0].length() == 0)) {
                    return false;
                }
                boolean flag = true;
                for (int i = 0; i < sci.length; i++) {
                    String[] poi;
                    if (sci[i].contains(".")) {
                        poi = sci[i].split("\\.");
                    } else {
                        poi = new String[]{sci[i]};
                    }
                    if (poi.length > 2 || poi.length == 0) {
                        return false;
                    } else if (poi.length == 1){
                        flag &= (isPositiveNum(poi[0]) || isNegativeNum(poi[0]));
                    } else if (poi.length == 2) {
                        flag &= (isPositiveNum(poi[0]) || isNegativeNum(poi[0]));
                        flag &= isPositiveNum(poi[1]);
                    }
                }
                return flag;
            }
        }
    }

    public boolean isPositiveNum(String s) {
        for (int i = 0; i < s.length(); i++) {
            int temp = s.charAt(i) - '0';
            if (temp > 9 || temp < 0) {
                return false;
            }
        }
        return true;
    }

    public boolean isNegativeNum(String s) {
        if (s.startsWith("-")) {
            for (int i = 1; i < s.length(); i++) {
                int temp = s.charAt(i) - '0';
                if (temp > 9 || temp < 0) {
                    return false;
                }
            }
            return true;
        } else {
            return false;
        }
    }

    public String[] split(String s, String delimiter) {
        if (s == null) {
            return null;
        } else {
            ArrayList<String> result = new ArrayList<String>();
            while (s.contains(delimiter)) {
                if (s.startsWith(delimiter)) {
                    result.add("");
                    s = s.substring(1);
                } else {
                    result.add(s.substring(0, s.indexOf(delimiter)));
                    s = s.substring(s.indexOf(delimiter));
                }
            }
            if (!"".equals(s)) {
                result.add(s);
            }
            return result.toArray(new String[]{});
        }
    }

    public static void main(String[] args) {
        ValidNumber validNumber = new ValidNumber();
//        System.out.println(validNumber.isNumber("2e10"));
//        System.out.println(validNumber.isNumber("1 a"));
//        System.out.println(validNumber.isNumber(" 0.1 "));
//        System.out.println(validNumber.isNumber("0.1e-100"));
//        System.out.println(validNumber.isNumber("e100"));
//        System.out.println(validNumber.isNumber("2e"));
//        System.out.println(validNumber.isNumber("0..0"));
//        System.out.println(validNumber.isNumber(".1."));
        System.out.println(validNumber.split(" 0.1 ", "."));
    }
}
