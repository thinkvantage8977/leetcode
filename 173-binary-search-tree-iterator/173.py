# Definition for a  binary tree node
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def inOrderTraversal(self, root):
        if not root:
            return
        self.inOrderTraversal(root.left)
        self.arr.append(root.val)
        self.inOrderTraversal(root.right)

    def __init__(self, root):
        self.arr = []
        self.pointer = 0
        self.inOrderTraversal(root)

    def hasNext(self):
        if self.pointer < len(self.arr):
            return True
        else:
            return False

    def next(self):
        if self.arr:
            val = self.arr[self.pointer]
            self.pointer += 1
            return val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
