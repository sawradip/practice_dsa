
class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
         self.arr.append(x)

    def top(self):
        return self.arr[-1]
    
    def pop(self):
        if self.empty():
            return None
        temp =  self.arr[-1]
        self.arr = self.arr[:-1]
        return temp

    def size(self):
        return len(self.arr)
    
    def empty(self):
        return len(self.arr) == 0
    


class QueuewithStack:
    def __init__(self):
        self.stacks = [Stack(), Stack()]
        self.current = 0
        self.other = 1

    def push(self, x):
        while not self.stacks[self.current].empty():
            self.stacks[self.other].push(self.stacks[self.current].pop())
        self.stacks[self.current].push(x)
        while not self.stacks[self.other].empty():
            self.stacks[self.current].push(self.stacks[self.other].pop())


    def top(self):
        return self.stacks[self.current].top()
    
    def pop(self):
        if self.empty():
            return None
        return self.stacks[self.current].pop()

    def size(self):
        return self.stacks[self.current].size()
    
    def empty(self):
        return self.size() == 0
    