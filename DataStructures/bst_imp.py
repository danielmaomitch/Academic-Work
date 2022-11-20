"""Implementation of a Binary Search Tree

Author: Daniel Mitchell
Student Number: 20239030
Last edited: 2-14-2022
"""

# Node class to be used for Binary Search Tree implementation 
class Node: 
    def __init__(self, elem):
        self.value = elem
        self.left = None
        self.right = None
        self.depth = 0
        self.height = 0

# Binary Search Tree implementation
class BinarySearchTree:

    # Initialize an empty Binary Search Tree
    def __init__(self):
        self.root = None

    # Inserts an element to the tree according to the Binary Search method
    def insert(self, root, elem):
        if root == None:
            return Node(elem)
        elif elem < root.value:
            root.left = self.insert(root.left, elem)
            temp = root.left
            if (temp.left == None) & (temp.right == None):  # Only change the depth of the node that had just been placed
                temp.depth = root.depth + 1
        else:
            root.right = self.insert(root.right, elem)
            temp = root.right
            if (temp.left == None) & (temp.right == None):  
                temp.depth = root.depth + 1 

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        return root

    # Returns the height of a given node or subtree
    def get_height(self, root):
        if root == None:
            return 0
        else:
            return root.height

    # Returns the total sum of the heights of each node in the tree using pre-order traversal
    def get_total_height(self, root):
        if self.root == None:
            return 
        elif root == None:
            return 0

        sum = root.height
        
        sum = sum + self.get_total_height(root.left)
        sum = sum + self.get_total_height(root.right)

        return sum

    # Returns the max depth of a given tree or subtree
    # Primarily in use to assist get_weight_balance_factor(self, root)
    def get_max_depth(self, root):
        if root == None:
            return 0
        elif (root.left == None) & (root.right == None):
            return root.depth

        return max(self.get_max_depth(root.left), self.get_max_depth(root.right))

    # Returns the weight balance factor of a given tree or subtree 
    def get_weight_balance_factor(self, root):
        if root == None:    # An empty tree or subtree cannot have a weight balance factor
            return -1   
        elif (root.left == None) & (root.right == None):    # A leaf node has a weight balance factor of 0
            return 0
        # If a node has one child, its weight balance factor is the longest node path downwards
        elif root.left == None:  
            return abs(0 - self.get_max_depth(root.right) + root.depth)  # Need to adjust to depth relative to current node, not true depth
        elif root.right == None:
            return self.get_max_depth(root.left) - root.depth
        else:
            cur_max = abs(self.get_max_depth(root.left) - self.get_max_depth(root.right))

            cur_max = max(self.get_weight_balance_factor(root.left), cur_max)
            cur_max = max(self.get_weight_balance_factor(root.right), cur_max)

            return cur_max

    # Serializations a given binary search tree or subtree into an array of its nodes' values
    def serialization(self, root, arr):
        if root == None:
            return None  # If the tree is empty
        
        
        arr.append(root.value)
        if not root.left == None:   # Do not append any Null values
            left_order = self.serialization(root.left, arr)
            if not left_order == None:
                arr.append(left_order)
        if not root.right == None:
            right_order = self.serialization(root.right, arr)
            if not right_order == None:
                arr.append(right_order)
        

    # Deserializes a given serialized binary search tree or subtree
    def deserialization(self, arr):
        for i in arr:
            self.root = self.insert(self.root, i)
        return self.root
    
    # Prints the tree in its serialized form
    def print_tree(self, root):
        arr = []
        self.serialization(self.root, arr)

        return arr

def main():
    t = BinarySearchTree()
    val_list = [20, 22, 10, 24, 25, 21]
    for i in val_list:
        t.root = t.insert(t.root, i)
    t_str = t.print_tree(t.root)  # Using print_tree() function tests serialize function
    print("Serialized form of tree: ")
    print(t_str)   
    print("get_total_height() test: ")
    print(t.get_total_height(t.root))
    print("get_weight_balance_factor() test: ")
    print(t.get_weight_balance_factor(t.root))
    t.serialization(t.root, val_list)
    t.root = t.deserialization(val_list)
    print("After serializing, deserializing, and reserializing: ")
    print(t_str)

main()