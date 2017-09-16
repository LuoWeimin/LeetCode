import java.util.HashMap;

/**
 * Simple to Introduction
 * Description:  一句话描述该类的功能
 * Author:       Luo WeiMin
 * CreateDate:   11/1/16
 * UpdateUser:   Luo WeiMin
 * UpdateDate:   11/1/16
 * UpdateRemark: 说明本次修改内容
 * Version:      v1.0
 * Copyright:    2015 www.ebigdata.org Inc. All rights reserved.
 */
public class LRUCache {

    class Node{
        int key;
        int value;
        Node pre;
        Node next;
        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    int capacity;
    HashMap<Integer, Node> hashMap;
    Node head;
    Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.hashMap = new HashMap<Integer, Node>();
    }

    public int get(int key) {
        if (hashMap.containsKey(key)) {
            Node move = hashMap.get(key);
            if (move.equals(tail)) {
            } else if (move.equals(head)) {
                head = head.next;
                move.pre = tail;
                tail.next = move;
                tail = tail.next;
            } else {
                Node pre = move.pre;
                pre.next = move.next;
                move.next.pre = pre;
                move.pre = tail;
                tail.next = move;
                tail = tail.next;
            }
            return move.value;
        } else {
            return -1;
        }
    }

    public void set(int key, int value) {
        if (hashMap.containsKey(key)) {
            Node move = hashMap.get(key);
            move.value = value;
            if (move.equals(tail)) {
            } else if (move.equals(head)) {
                head = head.next;
                move.pre = tail;
                tail.next = move;
                tail = tail.next;
            } else {
                Node pre = move.pre;
                pre.next = move.next;
                move.next.pre = pre;
                move.pre = tail;
                tail.next = move;
                tail = tail.next;
            }
        } else {
            if (hashMap.size() < capacity) {
                Node node = new Node(key, value);
                if (head == null) {
                    head = node;
                    tail = node;
                } else {
                    node.pre = tail;
                    tail.next = node;
                    tail = tail.next;
                }
                hashMap.put(key, node);
            } else {
                hashMap.remove(head.key);
                Node node = new Node(key, value);
                node.pre = tail;
                if (head.next != null) {
                    head = head.next;
                } else {
                    head = node;
                }
                tail.next = node;
                tail = tail.next;
                hashMap.put(key, node);
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(System.currentTimeMillis());
        LRUCache lruCache = new LRUCache(4);
        lruCache.set(2, 1);
        System.out.println(lruCache.get(2));
        lruCache.set(3, 2);
        lruCache.set(2, 5);
        System.out.println(lruCache.get(3));
        lruCache.set(4, 6);
        System.out.println(lruCache.get(2));
        lruCache.set(9, 10);
        lruCache.set(7, 11);
        lruCache.set(3, 2);
        lruCache.set(3, 2);
        lruCache.set(3, 2);
        lruCache.set(3, 2);
        lruCache.set(3, 2);

        System.out.println(lruCache.get(2));
        System.out.println(lruCache.get(3));


        System.out.println(System.currentTimeMillis());
    }
}
