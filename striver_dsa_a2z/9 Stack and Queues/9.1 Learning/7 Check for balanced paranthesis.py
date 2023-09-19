
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
        temp =  self.arr.pop(-1)
        # self.arr = self.arr[:-1]
        return temp

    def size(self):
        return len(self.arr)
    
    def empty(self):
        return len(self.arr) == 0
    
    
def isValid(s):

    if len(s) % 2: 
        return False

    st = Stack()
    bracket_dict = {"(": ")", "{": "}", "[": "]"}
    bra_keys = bracket_dict.keys()
    for char in s:
        if char in bra_keys:
            st.push(bracket_dict[char])
        elif st.top() == char:
            st.pop()
        else:
            return False

    return st.empty()
if __name__ == "__main__":
    s = "()"
    print(isValid(s))
