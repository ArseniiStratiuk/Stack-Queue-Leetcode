from collections import deque, defaultdict


class FreqStack:

    def __init__(self):
        self.f_map = defaultdict(int)
        self.f_stacks = defaultdict(deque)
        self.max_f = 0

    def push(self, val: int) -> None:
        self.f_map[val] += 1
        self.f_stacks[self.f_map[val]].appendleft(val)
        self.max_f = max(self.f_map[val], self.max_f)

    def pop(self) -> int:
        item = self.f_stacks[self.max_f].popleft()
        self.f_map[item] -= 1
        if not self.f_stacks[self.max_f]:
            self.max_f -= 1
        return item
