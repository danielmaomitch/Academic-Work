"""Implementation of a small scale web search engine

Author: Daniel Mitchell
Student Number: 20239030
Last edited: 03-16-2022
"""
import os
import WPI_imp
import WPQ_imp


def readFiles(folderpath):
    # Make a arraylist of files in the specified directory
    folder = os.listdir(folderpath)
    wpi_list = []

    # Create WebPageIndexes for each file
    for file in folder:
        file = folderpath + "\\" + file
        wpi = WPI_imp.WebPageIndex(file)
        wpi_list.append(wpi)
    return wpi_list

def main():
    
    folder = os.path.dirname(__file__) + "\data"
    arr = readFiles(folder)
    file = os.path.dirname(__file__) + "\queries.txt"

    fileread = open(file, 'r')
    
    first = True # Initiate WebpagePriorityQueue object on first runthrough and use reheap function other times
    for line in fileread:
        if first:
            line = line.replace('\n', '')
            wpq = WPQ_imp.WebpagePriorityQueue(line, arr)
            print("Query: " + line)
            for wpi in wpq.heap:
                print(wpi.filepath)
        else:
            line = line.replace('\n', '')
            wpq.reheap(line)
            print("Query: " + line)
            for wpi in wpq.heap:
                print(wpi.filepath)
        print('------------------------------------------')

    fileread.close()


main()