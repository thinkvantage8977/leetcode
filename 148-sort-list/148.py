# Definition for singly-linked list.
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

    def mergeListSort(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        list1 = self.sortList(slow.next)
        slow.next = None
        list2 = self.sortList(head)

        return self.mergeListSort(list2, list1)


testClass = Solution()

Head = ListNode(1)
# Head.next = ListNode(2)
# Head.next.next = ListNode(1)
# Head.next.next.next = ListNode(4)
# Head.next.next.next.next = ListNode(5)
# Head.next.next.next.next.next = ListNode(3)
# Head.next.next.next.next.next.next = ListNode(7)
# Head.next.next.next.next.next.next.next = ListNode(8)

result = testClass.sortList(Head)

printList(result)
