"""用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:                 # if self.stack2 == None 是错的 ，应该是 == []
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:                               # 注意还有不为空的时候        【注意在class中要有self】
            return self.stack2.pop()
