# Hayden Michael
# 11/4/19
# CSC 310
# Simulates tree traversal with inorder and postorder traversal


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class YourSolution(object):
def inorderTraversal(a, root):
    if root:
        # recur with left child
        inorderTraversal(a, root.left)

        # then add the data of node
        if root.val is not None:
            a.append(root.val)

        # recur with right child
        inorderTraversal(a, root.right)
    return a


def preorderTraversal(a, root):
    if root:
        # First add the data of node
        if root.val is not None:
            a.append(root.val)

        # recur with left child
        preorderTraversal(a, root.left)

        # recur with right child
        preorderTraversal(a, root.right)
        return a


# recursively populates the tree with values from arr1
def populateTree(arr1, root1, i, n):
    if i < n:
        temp = TreeNode(arr1[i])
        root1 = temp

        # insert left child
        root1.left = populateTree(arr1, root1.left, 2 * i + 1, n)

        # insert right child
        root1.right = populateTree(arr1, root1.right, 2 * i + 2, n)
    return root1


# testing for both traversal methods
arr = [1, None, 2, None, None, 3]
n = len(arr)
root2 = None
root2 = populateTree(arr, root2, 0, n)

a = []
a = inorderTraversal(a, root2)
print("In order Traversal")
for x in a:
    print(x)
print(" ")
b = []
b = preorderTraversal(b, root2)
print("Pre-order Traversal")
for x in b:
    print(x)
print(" ")

arr2 = [1, 2, 3, 4, 5, 6, None]
n1 = len(arr2)
root3 = None
root3 = populateTree(arr2, root3, 0, n1)

a1 = []
a1 = inorderTraversal(a1, root3)
print("In Order Traversal")
for x in a1:
    print(x)
print(" ")

b1 = []
b1 = preorderTraversal(b1, root3)
print("Pre-order Traversal")
for x in b1:
    print(x)

arr3 = [1, 2, 3]
n2 = len(arr3)
root4 = None
root4 = populateTree(arr3, root4, 0, n2)

a2 = []
a2 = inorderTraversal(a2, root4)
print("In Order Traversal")
for x in a2:
    print(x)
print(" ")

b2 = []
b2 = preorderTraversal(b2, root4)
print("Pre-order Traversal")
for x in b2:
    print(x)