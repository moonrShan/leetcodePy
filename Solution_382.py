from random import random

from Solution_206 import ListNode


class Solution_382:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            if random.random() * scope < 1 :
                chosen_value = curr.val
            curr = curr.next
            scope += 1
        return chosen_value