import numpy as np
import os

class Piece:

    def __init__(self, fileName):
        self.arrFile = fileName
        #self.arr = np.zeros((7, 7), np.short)

        #read the next line from arrFile
        file = open("tiles/" + self.arrFile, 'r')
        height = len(file.readlines())
        file.seek(0,0)
        line = file.readline()
        line = removeSpaceNewline(line)
        width = len(line)

        #read each line of file into 2d array arr
        self.arr = np.zeros((height,width), np.short)
        i = 0
        while(line != ""):
            j = 0
            for c in line:
                self.arr[i][j] = c
                j += 1
            i += 1
            line = file.readline()
            line = removeSpaceNewline(line)
            
        file.close()

    #rotate the shape in arr by 90 degrees right
    def rotateRight(self):
        self.arr = np.rot90(self.arr)

    #rotate the shape in arr by 90 degrees left
    def rotateLeft(self):
        self.arr = np.rot90(self.arr, -1)

    def flip(self):
        self.arr = np.flip(self.arr, 1)

#removes spaces and newlines from a string
def removeSpaceNewline(s):
    s = s.replace(' ', '')
    s = s.replace('\n', '')
    return s

