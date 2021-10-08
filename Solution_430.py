class Solution_430:
    def flatten(self, head: 'Node') -> 'Node':
        sentinel = Node(0, None, head, None)
        while head:
            if head.child:
                currentNext = head.next
                flattenChild = self.flatten(head.child)
                head.child = None
                head.next = flattenChild
                flattenChild.prev = head
                while head.next:
                    head = head.next
                head.next = currentNext
                if currentNext:
                    currentNext.prev = head
            head = head.next
        return sentinel.next