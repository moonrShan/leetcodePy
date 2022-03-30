import collections

from Solution_1628 import Node


class Solution_138:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map_new = collections.defaultdict(lambda: Node(0, None, None))
        map_new[None] = None

        nd_old = head
        while nd_old:
            map_new[nd_old].val = nd_old.val
            map_new[nd_old].next = map_new[nd_old.next]
            map_new[nd_old].random = map_new[nd_old.random]
            nd_old = nd_old.next
        return map_new[head]