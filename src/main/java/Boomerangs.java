import java.util.HashMap;
import java.util.Map;

/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   11/10/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   11/10/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class Boomerangs {
    public int numberOfBoomerangs(int[][] points) {
        int count = 0;
        for (int i = 0; i < points.length; i++) {
            HashMap<Long, Integer> dic = new HashMap<Long, Integer>();
            for (int j = 0; j < points.length; j++) {
                if (i == j) {
                    continue;
                } else {
                    long d = distance(points[i], points[j]);
                    if (dic.containsKey(d)) {
                        dic.put(d, dic.get(d) + 1);
                    } else {
                        dic.put(d, 1);
                    }
                }
            }
            for (Map.Entry<Long, Integer> entry : dic.entrySet()) {
                int value = entry.getValue();
                count += value * (value - 1);
            }
        }
        return count;
    }

    public long distance(int[] x, int[] y) {
        long distance = 0;
        for (int i = 0; i < x.length; i++) {
            distance += Math.pow(x[i] - y[i] , 2);
        }
        return distance;
    }
}
