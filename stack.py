from collections import deque
class MyQueue(object):
    def __init__(self):
        self.front = deque()
        self.end = deque()

    def peek(self):
        if not self.end:
            self.move()
        return self.end[0];


    def pop(self):
        if not self.end:
            self.move()
        self.end.popleft()

    def put(self, value):
        self.front.appendleft(value)

    def move(self):
        while self.front:
            self.end.appendleft(self.front.popleft())

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
