from typing import Optional
from Solution_206 import ListNode


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        needReverse = False
        groupLength = 1
        groupCount = 0
        sentinal = ListNode(0, head)
        while head:
            prev = head
            head = head.next
            groupCount += 1
            if groupCount == groupLength:
                groupLength += 1
                groupCount = 0
                needReverse = ~needReverse
                if needReverse:
                    prev.next = self.reverseList(head, groupLength)
                    needReverse = False
        return sentinal.next

    def reverseList(self, head, k):
        prev = None
        curr = head
        while head and k:
            k -= 1
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        sentinal = ListNode(0, curr)

        while curr.next:
            curr = curr.next
        curr.next = head
        return sentinal.next


def main():
    testObject = Solution()
    print(testObject.findPosLength(["O","O","","X","O",""]))
    print(testObject.findPosLength(["X","","O","O","","X","O",""]))

if __name__ == "__main__":
    main()