import numpy as np

class Piece:
    arrFile = ""
    arr = np.zeros((7, 7), np.short)

    def __init__(self, fileName):
        self.arrFile = fileName

        #read the next line from arrFile
        file = open("tiles/" + self.arrFile, 'r')
        line = file.readline()
        line = removeSpaceNewline(line)

        #read each line of file into 2d array arr
        i = 0
        while(line != ""):
            j = 0
            for c in line:
                self.arr[i][j] = c
                j += 1
            i += 1
            line = file.readline()
            line = removeSpaceNewline(line)

    #rotate the shape in arr by 90 degrees
    def rotate(self):
        self.arr = np.rot90(self.arr)

#removes spaces and newlines from a string
def removeSpaceNewline(s):
    s = s.replace(' ', '')
    s = s.replace('\n', '')
    return s

x = Piece("i5p1.txt")
print(x.arr)
x.rotate()
print(x.arr)
