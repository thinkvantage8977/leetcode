class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def printList(l):
    while l != None:
        print(l.val, end="")
        if l.next:
            print('->', end="")
        l = l.next
    print()


class Solution(object):

    def recur(self, node):
        if not node.next:
            node.val+=1
            c=node.val //10
            node.val %=10
            return c
        else:
            c = self.recur(node.next)
            node.val+=c
            c = node.val // 10
            node.val %=10
            return c

    def plusOne(self, head):
        if not head:
            return None
        r = self.recur(head)
        if r == 1:
            dummy = ListNode(1)
            dummy.next = head
            return dummy
        else:
            return head


Head = ListNode(1)
Head.next = ListNode(2)
Head.next.next = ListNode(3)



testClass = Solution()

print(printList(testClass.plusOne(None)))
