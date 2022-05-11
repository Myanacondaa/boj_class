import sys
from collections import deque
input = sys.stdin.readline

class Deque:
    def __init__(self):
        self.d = deque()

    def size(self):
        return len(self.d)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def push(self, n):
        self.d.append(n)

    def pop(self):
        if not self.empty():
            return self.d.popleft()
        else:
            return -1

    def front(self):
        if not self.empty():
            return self.d[0]
        else:
            return -1

    def back(self):
        if not self.empty():
            return self.d[-1]
        else:
            return -1

if __name__ == "__main__":
    N = int(input())
    queue = Deque()
    for i in range(N):
        command = input().split()
        if command[0] == "push":
            queue.push(command[1])

        elif command[0] == "pop":
            print(queue.pop())

        elif command[0] == "size":
            print(queue.size())

        elif command[0] == "empty":
            print(queue.empty())

        elif command[0] == "front":
            print(queue.front())

        elif command[0] == "back":
            print(queue.back())


