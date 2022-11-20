"""Creates index representation of a wep page using AVL tree

Author: Daniel Mitchell
Student Number: 20239030
Last edited: 03-14-2022
"""
import os

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

class WebPageIndex:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tree = AVLTree()

        fileread = open(self.filepath, "r")
        data = fileread.read()

        # Divide string into words and remove special characters
        data = data.replace('\n', ' ').replace('(', ' ').replace(')', ' ').replace('.', ' ').replace(',', ' ').replace('/', ' ')
        data = data.split(' ')
        fileread.close()

        # Find unique words in file to create AVL tree from
        unique_data = []
        for word in data:
            if word not in unique_data:
                unique_data.append(word)
        for i in range(len(unique_data)):
            occ_list = []
            unique_data[i] = unique_data[i].lower()
            for j in range(len(data)):
                if unique_data[i] in data[j].lower():   # Keep track of the indices of the occurence of each word
                    occ_list.append(j)

            self.tree.root = self.tree.put(self.tree.root, unique_data[i], occ_list)

    # Returns the number of occurences of a given word in a file, -1 if it is not in the file
    def getCount(self, root, s):
        if root == None:
            return -1
        elif root.key == s:
            return len(root.value)
        
        else:
            count = self.getCount(root.left, s)
            if not count == -1:
                return count
            return self.getCount(root.right, s)
        
    def printtree(self, root):
        if root == None:
            return
        print(root.key)
        self.printtree(root.left)
        self.printtree(root.right)


"""
def main():
    fileapth = os.path.dirname(__file__) + "\data\doc3-binarysearchtree.txt"
    t = WebPageIndex(fileapth)
    x = t.getCount(t.tree.root, 'tree')
    print(x)
   # t.printtree(t.tree.root)

main()
"""