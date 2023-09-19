
class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
         self.arr.append(x)

    def top(self):
        if self.empty():
            return None
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
    
if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.top())
    print("Size of stack before deleting any element", s.size())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.size())
    print("Top of stack after deleting an element", s.top())