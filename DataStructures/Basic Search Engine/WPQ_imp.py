"""Implementation of a heap-based Priority Queue 

Author: Daniel Mitchell
Student Number: 20239030
Last edited: 03-15-2022
"""

from queue import Empty
import WPI_imp

class WebpagePriorityQueue:
    def __init__(self, query, wpi_list):
        self.heap = []
        self.query = query.split(' ')   # Split query into a list of its words
        
        # Add items to the maxheap according to heap rules
        for wpi in wpi_list:
            self.heap.append(wpi)
            cur = len(self.heap) - 1
            while self.compare_wpi(self.heap[cur], self.heap[(int)((cur-1)/2)]):
            #    print('switched')
                temp = self.heap[cur]
                self.heap[cur] = self.heap[(int)((cur-1)/2)]
                self.heap[(int)((cur-1)/2)] = temp
                cur = (int) ((cur - 1) / 2)

    # Compares two WebPageIndex objects. If wpi_new has a higher priority return True, False otherwise
    def compare_wpi(self, wpi_new, wpi_parent):
        sum_new = 0
        sum_parent = 0
    #    print(self.query)
    #    print(wpi_new.filepath)
     #   print(wpi_parent.filepath)
        for word in self.query:
            sum_new += wpi_new.getCount(wpi_new.tree.root, word)
            sum_parent += wpi_parent.getCount(wpi_parent.tree.root, word)
    #    print(sum_new)
    #    print(sum_parent)
        if sum_new > sum_parent:
            return True
        else:
            return False
        
    # Returns the item with the current highest priority in the queue
    def peek(self):
        return self.heap[0]
    
    # Extracts an item from the priority queue
    def poll(self):
        # Raise an exception if the queue is empty
        if len(self.heap) == 0:
            raise Empty("Queue is empty.")
        val = self.heap[0]
        if len(self.heap) == 1:
            del self.heap[0]
            return val
        
        # If queue is not empty and has more than one item, extract highest priority item and heapify heap array
        else:
            self.heap[0] = self.heap[-1]
            del self.heap[-1]

            cur = 0
            while cur < len(self.heap):
                # Stop if reach node with no children
                if (2*cur+1) > len(self.heap):
                    break
                # If current node has only one child check if needs to be switched
                elif (2*cur+2) > len(self.heap):
                    if self.compare_wpi(self.heap[2*cur+1], self.heap[cur]):
                        temp = self.heap[cur]
                        self.heap[cur] = self.heap[2*cur+1]
                        self.heap[2*cur+1] = temp
                    else:
                        break
                # Stop if current node is greater or equal to children nodes
                elif self.compare_wpi(self.heap[cur], self.heap[2*cur+1]) and self.compare_wpi(self.heap[cur], self.heap[2*cur+2]):
                    break
                # If left node is larger of the two children, switch with current node
                elif self.compare_wpi(self.heap[2*cur+1], self.heap[2*cur+2]):
                    temp = self.heap[cur]
                    self.heap[cur] = self.heap[2*cur+1]
                    self.heap[2*cur+1] = temp
                    cur = 2*cur + 1
                # If right node is larger of the two children, switch with current node
                else:
                    temp = self.heap[cur]
                    self.heap[cur] = self.heap[2*cur+2]
                    self.heap[2*cur+1] = temp
                    cur = 2*cur + 2
            return val
        
    # Reheapify the heap array once the priority definition is changed
    def reheap(self, query):
        wpi_list = []
        for wpi in self.heap:
            wpi_list.append(wpi)
        self.heap = []
        self.query = query
        for wpi in wpi_list:
            self.heap.append(wpi)
            cur = len(self.heap) - 1
            while self.compare_wpi(self.heap[cur], self.heap[(int)((cur-1)/2)]):
                temp = self.heap[cur]
                self.heap[cur] = self.heap[(int)((cur-1)/2)]
                self.heap[(int)((cur-1)/2)] = temp
                cur = (int) ((cur - 1) / 2)

                    