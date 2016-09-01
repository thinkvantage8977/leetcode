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

    def prcUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].val < self.heapList[i // 2].val:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i //= 2

    def insert(self, val):
        self.heapList.append(val)
        self.prcUp(len(self.heapList) - 1)

    def getMinChild(self, i):
        if i * 2 + 1 > len(self.heapList) - 1:
            return i * 2
        else:
            return i * 2 if self.heapList[i * 2].val < self.heapList[i * 2 + 1].val else i * 2 + 1

    def prcDown(self, i):
        while i * 2 < len(self.heapList) - 1:
            midChild = self.getMinChild(i)
            if self.heapList[i].val > self.heapList[midChild].val:
                self.heapList[i], self.heapList[midChild] = self.heapList[midChild], self.heapList[i]
            i = midChild

    def delMin(self):
        if len(self.heapList) == 1:
            return None

        if len(self.heapList) == 2:
            return self.heapList.pop()
        returnValue = self.heapList[1]
        self.heapList[1] = self.heapList.pop()
        self.prcDown(1)
        return returnValue

    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        dummyhead = ListNode(0)
        h = dummyhead
        self.heapList = [0]

        for i in lists:
            if not i:
                continue
            self.insert(i)

        while 1:
            new = self.delMin()
            if not new:
                return None
            if new.val == float("inf"):
                break
            h.next = new
            if not new.next:
                self.insert(ListNode(float("inf")))
            else:
                self.insert(new.next)
            h = h.next

        return dummyhead.next


testClass = Solution()


Head1 = ListNode(-1)
Head1.next = ListNode(1)
# Head1.next.next = ListNode(5)
# Head1.next.next.next = ListNode(9)
# Head1.next.next.next.next = ListNode(9)


Head2 = ListNode(-3)
Head2.next = ListNode(1)
Head2.next.next = ListNode(4)
# Head2.next.next.next = ListNode(8)
# Head2.next.next.next.next = ListNode(10)


Head3 = ListNode(-2)
Head3.next = ListNode(-1)
Head3.next.next = ListNode(0)
Head3.next.next.next = ListNode(2)


l = [Head1, Head2, Head3]

print(printList(testClass.mergeKLists(l)))
