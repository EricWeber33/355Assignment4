def class Piece:
    arrFile = ""
    arr = [][]

    def init(fileName):
        self.arrFile = fileName

        #read each line of file into 2d array arr
        file = open(self.arrFile, 'r')
        line = file.readline()
        i = 0
        while(line != ""):
            j = 0
            for c in line:
                arr[i][j] = c
                j++
            i++
                
        
