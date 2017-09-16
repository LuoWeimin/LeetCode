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
public class AddTwoNum {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
//        int size1 = 0;
//        ListNode head = l1;
//        while (head != null) {
//            size1++;
//            head = head.next;
//        }
//        int size2 = 0;
//        head = l2;
//        while (head != null) {
//            size2++;
//            head = head.next;
//        }
//        int max = size1 > size2 ? size1 : size2;
//        max++;
//        int[] num1 = new int[max];
////        Arrays.fill(num1, 0);
//        int[] num2 = new int[max];
////        Arrays.fill(num2, 0);
//        head = l1;
//        int i = 0;
//        while (head != null) {
//            num1[size1 - 1 - i++] = head.val;
//            head = head.next;
//        }
//        i = 0;
//        head = l2;
//        while (head != null) {
//            num2[size2 - 1 - i++] = head.val;
//            head = head.next;
//        }
//        int plus = 0;
//        for (i = 0; i < max; i++) {
//            num1[i] = num1[i] + num2[i] + plus;
//            plus = num1[i] / 10;
//            num1[i] = num1[i] % 10;
//        }
//        if (num1[max - 1] == 0) {
//            i = max - 2;
//        } else {
//            i = max - 1;
//        }
//        head = new ListNode(num1[i]);
//        l1 = head;
//        for (i -= 1; i >= 0 ; i--) {
//            head.next = new ListNode(num1[i]);
//            head = head.next;
//        }
//        return l1;
        ListNode head1 = l1, head2 = l2, head3 = l1;
        int plus = 0;
        while (head1 != null || head2 != null || plus != 0) {
            if (head1 != null) {
                plus += head1.val;
                head1 = head1.next;
            }
            if (head2 != null) {
                plus += head2.val;
                head2 = head2.next;
            }
            if (head3 != null) {
                head3.val = plus % 10;
                plus /= 10;
                if (head3.next == null && (head1 != null || head2 != null || plus != 0)) {
                    head3.next = new ListNode(0);
                }
                head3 = head3.next;
            } else {
                head3 = new ListNode(plus % 10);
                plus /= 10;
                if (head3.next == null && (head2 != null || plus != 0)) {
                    head3.next = new ListNode(0);
                }
                head3 = head3.next;
            }
        }
        return l1;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(0);
//        l1.next = new ListNode(4);
//        l1.next.next = new ListNode(3);
//        l1.next.next.next = new ListNode(9);
//        l1.next.next.next.next = new ListNode(9);
//        l1.next.next.next.next.next = new ListNode(9);
//        l1.next.next.next.next.next.next = new ListNode(9);
//        l1.next.next.next.next.next.next.next = new ListNode(9);
//        l1.next.next.next.next.next.next.next.next = new ListNode(9);
//        l1.next.next.next.next.next.next.next.next.next = new ListNode(9);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(7);
        AddTwoNum add = new AddTwoNum();
        ListNode result = add.addTwoNumbers(l1, l2);
        System.out.println(result.toString());
    }
}


