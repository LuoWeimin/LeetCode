import java.util.Stack;

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
public class ImplementQueueUsingStacks {

    Stack<Integer> temp = new Stack<Integer>();
    Stack<Integer> value = new Stack<Integer>();

    // Push element x to the back of queue.
    public void push(int x) {
        if(value.isEmpty()){
            value.push(x);
        }else{
            while(!value.isEmpty()){
                temp.push(value.pop());
            }

            value.push(x);

            while(!temp.isEmpty()){
                value.push(temp.pop());
            }
        }
    }

    // Removes the element from in front of queue.
    public void pop() {
        value.pop();
    }

    // Get the front element.
    public int peek() {
        return value.peek();
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return value.isEmpty();
    }
}
