# Implement a program that provides the following operations on a binary tree.
# insert adds an integer x into a binary tree T to give a binary tree R.
# search returns true if x is contained in the binary tree T.
# preorder lists the nodes of the binary tree T using preorder traversal.
# inorder lists the nodes of the binary tree T using inorder traversal.
# postorder lists the nodes of the binary tree T using postorder traversal.


class Node:
# first of all, let's tell it what it is:
# A node in a BST may have left and right subtrees.
    def __init__(self, node, left = None, right = None):
        self.node = node
        self.left = left
        self.right = right

# Insert Method to create the tree:
    def insert(self, node):
        if self.node:
            if node < self.node:
                if self.left is None:
                    self.left = Node(node)
                else:
                    self.left.insert(node)
            elif node > self.node:
                if self.right is None:
                    self.right = Node(node)
                else:
                    self.right.insert(node)
        else:
            self.node = node

# Search Method:
    def search(self, lookfor):
        if lookfor < self.node:
            if self.left is None:
                return "Sorry! I couldn't find {} anywhere !".format(lookfor)
            return self.left.search(lookfor)
        elif lookfor > self.node:
            if self.right is None:
                return "Sorry! I couldn't find {} anywhere !".format(lookfor)
            return self.right.search(lookfor)
        else:
            return "YAY! I found {} !".format(self.node)

# Let's print it out!
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.node),
        if self.right:
            self.right.PrintTree()

# Traversal Methods:

# Preorder Traversal Method:
# preorder: go from the root, to left, to right
    def preorder(self, root):
        return_list = []
        if root:
            return_list.append(root.node)
            return_list = return_list + self.preorder(root.left)
            return_list = return_list + self.preorder(root.right)
        return return_list

# Inorder Traversal Method:
# inorder: go from left, to root, to right
    def inorder(self, root):
        return_list = []
        if root:
            return_list = self.inorder(root.left)
            return_list.append(root.node)
            return_list = return_list + self.inorder(root.right)
        return return_list

# Postorder Traversal Method:
# postorder: go from left, to right, to root
    def postorder(self, root):
        return_list = []
        if root:
            return_list = self.postorder(root.left)
            return_list = return_list + self.postorder(root.right)
            return_list.append(root.node)
        return return_list

print("creating tree..")
root = Node(25)
root.insert(16)
root.insert(8)
root.insert(92)

print("searching tree: ")
print(root.search(8))
print(root.search(29))
# # results we're looking for:
# # YAY! I found 8 !
# # Sorry! I couldn't find 29 anywhere !


root = Node(25)
root.insert(16)
root.insert(44)
root.insert(8)
root.insert(20)
root.insert(32)
root.insert(53)
print("preorder: ")
print(root.preorder(root))
# With preorder traversal, we're looking for this answer:
# [25, 16, 8, 20, 44, 32, 53]


root = Node(25)
root.insert(16)
root.insert(44)
root.insert(8)
root.insert(20)
root.insert(32)
root.insert(53)
print("inorder: ")
print(root.inorder(root))
# With inorder traversal, we're looking for this answer:
# [8, 16, 20, 25, 32, 44, 53]

root = Node(25)
root.insert(16)
root.insert(44)
root.insert(8)
root.insert(20)
root.insert(32)
root.insert(53)
print("postorder: ")
print(root.postorder(root))
# With postorder traversal, we're looking for this answer:
# [8, 20, 16, 32, 53, 44, 25]


# my sample tree:
#
#          25
#        /    \
#       /      \
#      16      44
#     / \      / \
#    8   20   32  53

# Here are the return_lists we should get from this tree:

# preorder:    [25, 16, 8, 20, 44, 32, 53]
# inorder:     [8, 16, 20, 25, 32, 44, 53]
# postorder:   [8, 20, 16, 32, 53, 44, 25]
