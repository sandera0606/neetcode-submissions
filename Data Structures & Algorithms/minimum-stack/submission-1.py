class Node:
    def __init__(self, val, my_min, prev):
        self.val = val
        self.my_min = my_min
        self.prev = prev

class MinStack:

    def __init__(self):
        self.min_thus_far = None
        self.my_top = None

    def push(self, val: int) -> None:
        if self.my_top is None:
            self.min_thus_far = val
        else:
            self.min_thus_far = min(val, self.my_top.my_min)
        self.my_top = Node(val, self.min_thus_far, self.my_top)

    def pop(self) -> None:
        temp = self.my_top
        self.my_top = self.my_top.prev
        if self.my_top is None:
            self.min_thus_far = None
        else:
            self.min_thus_far = self.my_top.my_min

    def top(self) -> int:
        return self.my_top.val

    def getMin(self) -> int:
        return self.my_top.my_min
        
# consider each value in the stack having a corresponding minimum value