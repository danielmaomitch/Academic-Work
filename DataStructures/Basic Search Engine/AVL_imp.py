from logging import NullHandler
from sre_constants import NOT_LITERAL
from turtle import done

# Node implementation for AVLTReeMap class
class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        self.height = 1

# Implementation of AVLTreeMap
class AVLTree:
    def __init__(self):
        self.root = None

    # Searches for a given key in the binary tree; returns non if it is not found
    def get(self, key):
        cur = self.root
        while not cur == None:
            if cur.key == key:
                return cur.value
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return None

    # Returns the height of a given node
    def get_height(self, root):
        if root == None:
            return 0
        else:
            return root.height

    # Returns the blaance factor of a given node
    def get_balance(self, root):
        if root == None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # Rotates a given node or subtree to the right
    def right_rotate(self, B):
        A = B.left
        beta = A.right
        A.right = B
        B.left = beta

        B.height = 1 + max(self.get_height(B.left),self.get_height(B.right))
        A.height = 1 + max(self.get_height(A.left),self.get_height(A.right))

        return A

    # Rotates a given node or subtree to the left
    def left_rotate(self, A):
        B = A.right
        beta = B.left
        B.left = A
        A.right = beta

        A.height = 1 + max(self.get_height(A.left),self.get_height(A.right))
        B.height = 1 + max(self.get_height(B.left),self.get_height(B.right))

        return B

    # Inserts a new node onto the binary tree with the given key and value pair
    def put(self, root, key, value):
        if root == None:
            return Node(key, value)
        elif key < root.key:
            root.left = self.put(root.left, key, value)
        else:
            root.right = self.put(root.right, key, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        
        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
 
        return root
     

def main():
    t = AVLTree()
    key_list = [15, 20, 24, 10, 13, 7, 30, 36 ,25]
    val_list = ["bob", "anna", "tom", "david", "david", "ben", "karen", "erin", "david"]

    for i in range(len(key_list)):
        print(i)
        t.root = t.put(t.root, key_list[i], val_list[i])

    for i in key_list:
        print(t.get(i))
        
main()
