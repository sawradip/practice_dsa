
class Queue:
    def __init__(self):
        self.arr = []

    def push(self, x):
         self.arr.append(x)

    def top(self):
        if self.empty():
            return None
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
    
if __name__ == "__main__":
    s = Queue()
    s.push(4)
    s.push(14)
    s.push(24)
    s.push(34)
    s.top()
    s.size()
    s.pop()
