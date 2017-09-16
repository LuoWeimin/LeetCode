import java.util.ArrayList;
import java.util.List;

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
public class Permutations {
    public List<List<Integer>> permute(int[] nums) {
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        for (Integer i : nums) {
            arrayList.add(i);
        }
        return generate(arrayList);
    }

    public List<List<Integer>> generate(ArrayList<Integer> integers) {
        if (integers.size() == 1) {
            List<List<Integer>> lists = new ArrayList<List<Integer>>();
            lists.add(integers);
            return lists;
        } else {
            List<List<Integer>> lists = new ArrayList<List<Integer>>();
            for (Integer i : integers) {
                ArrayList<Integer> left = new ArrayList<Integer>();
                left.addAll(integers);
                left.remove(i);
                List<List<Integer>> result = generate(left);
                for (List<Integer> list : result) {
                    list.add(i);
                }
                lists.addAll(result);
            }
            return lists;
        }
    }

    public static void main(String[] args) {
        Permutations permutations = new Permutations();
        System.out.println(permutations.permute(new int[]{1,2}));
    }
}
