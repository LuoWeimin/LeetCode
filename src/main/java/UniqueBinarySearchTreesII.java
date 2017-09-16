import java.util.ArrayList;
import java.util.List;

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
public class UniqueBinarySearchTreesII {

    public ArrayList<TreeNode> generateTrees(int n) {
        if (n <= 0) {
            return new ArrayList<TreeNode>();
        }
        return generate(1, n);
    }

    private ArrayList<TreeNode> generate(int start, int end){
        ArrayList<TreeNode> rst = new ArrayList<TreeNode>();

        if(start > end){
            rst.add(null);
            return rst;
        }

        for(int i=start; i<=end; i++){
            ArrayList<TreeNode> left = generate(start, i-1);
            ArrayList<TreeNode> right = generate(i+1, end);
            for(TreeNode l: left){
                for(TreeNode r: right){
                    TreeNode root = new TreeNode(i);
                    root.left = l;
                    root.right = r;
                    rst.add(root);
                }
            }
        }
        return rst;
    }

    public static void main(String[] args) {
        UniqueBinarySearchTreesII uniqueBinarySearchTreesII = new UniqueBinarySearchTreesII();
        List<TreeNode> list = uniqueBinarySearchTreesII.generateTrees(0);
        System.out.println();
    }

}
