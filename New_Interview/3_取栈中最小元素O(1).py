"""实现一个特殊的栈，在实现栈的基本功能的基础上，再实现用O（1）的时间复杂度取栈的最小元素
            pop（弹栈）、push（入栈）、getMin操作的时间复杂度都是O(1)
在算法的设计当中，经常采用空间换时间的方式来提高时间复杂度，也就是用额外的存储空间来降低操作的时间复杂度。
"""
'''解题思路：
    1. 首先准备两个栈，一个是elemStack栈（存储元素），一个是minStack栈(存储当前最小值）
    2. 如果当前入栈的元素比原来栈中的元素最小值还要小，则把这个值压入保存最小值元素的栈中；在出栈的时候，如果当前的
元素恰好等于当前栈中的那个最小值，保存最先值得栈顶元素也出栈，使当前最小值变为当前最小值入栈之前的那个最小值。
        若：5 6 3依次入栈，elemStack栈中 栈底到栈顶分别为5 6 3，minStack栈中栈底到栈顶分别为5 3
'''
class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        """判断栈是否为空"""
        return len(self.items) == 0

    def size(self):
        """栈的大小"""
        return len(self.items)

    def peek(self):
        """返回栈顶元素"""
        if not self.empty():
            return self.items[len(self.items) - 1]
        else:
            return None

    def pop(self):
        """弹栈"""
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈空")

    def push(self, items):
        """压栈"""
        self.items.append(items)


class MyStack:
    def __init__(self):
        self.elemStack = Stack()        # 用来存储栈中元素
        self.minStack = Stack()         # 栈顶永远存储当前elemStack中最小的值

    def push(self, data):
        self.elemStack.push(data)
        # 更新保存最小元素的栈
        if self.minStack.empty():       # 当入第一个数入两个空栈的时候，该数同时压入两个栈
            self.minStack.push(data)
        else:                           # 当minStack不为空的时候
            if data < self.minStack.peek():     # 新入栈的数小于当前最小栈minStack的栈顶最小值，压栈
                self.minStack.push(data)

    def pop(self):
        topData = self.elemStack.peek()     # 弹出栈顶元素
        self.elemStack.pop()
        if topData == self.mins():  # 若elemStack栈顶元素与minStack栈顶元素（当前最小值）一样，则将minStack的栈顶也弹出
            self.minStack.pop()
        return topData

    def mins(self):
        if self.minStack.empty():
            return 2 ** 32
        else:
            return self.minStack.peek()     # 返回栈顶元素，不弹出


if __name__ == "__main__":
    stack = MyStack()
    stack.push(7)
    print("栈中最小值为：" + str(stack.mins()))
    stack.push(5)
    print("栈中最小值为：" + str(stack.mins()))
    stack.push(6)
    print("栈中最小值为：" + str(stack.mins()))
    stack.push(2)
    print("栈中最小值为：" + str(stack.mins()))
