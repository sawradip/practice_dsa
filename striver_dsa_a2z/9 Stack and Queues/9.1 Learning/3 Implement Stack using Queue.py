
class Queue:
    def __init__(self):
        self.arr = []

    def push(self, x):
         self.arr.append(x)

    def top(self):
        return self.arr[0]
    
    def pop(self):
        if self.empty():
            return None
        temp =  self.arr[0]
        self.arr = self.arr[1:]
        return temp

    def size(self):
        return len(self.arr)
    
    def empty(self):
        return len(self.arr) == 0
    

class StackwithQueue:
    def __init__(self):
        self.queues = [Queue(), Queue()]
        self.current = 0
        self.other = 1



    def push(self, x):
        self.queues[self.other].push(x)

        while not self.queues[self.current].empty():
            self.queues[self.other].push(self.queues[self.current].pop())
            
        self.current, self.other = self.other, self.current


    def top(self):
        return self.queues[self.current].top()
    
    def pop(self):
        if self.empty():
            return None
        return self.queues[self.current].pop()

    def size(self):
        return self.queues[self.current].size()
    
    def empty(self):
        return self.size() == 0
    
if __name__ == "__main__":
    s = StackwithQueue()
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.top())
    print("Size of stack before deleting any element", s.size())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.size())
    print("Top of stack after deleting an element", s.top())