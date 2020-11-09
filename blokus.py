import pygame
from board import *

def main():
    pygame.init()
    
    # basic mxn window
    window = pygame.display.set_mode((widthWindow, heightWindow))
    b = Board()
    clock = pygame.time.Clock()
    p = True # True: player 1, False: player 2
    placedCoords = [-1,-1]
    while True:
        # checks if user closed window
        events = pygame.event.get()
        for x in events:
            if x.type == pygame.QUIT:
                print('Thank You for Playing')
                return
            if x.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                #Previous Piece Button P1
                if (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*2 and mousePos[1] < sizeNode*3):
                    clearGamepad(b.topSurf)
                    b.p1Index = (b.p1Index - 1) % 21
                    drawPiece(sizeNode*3,0,b.p1Array[b.p1Index], b.topSurf)
                #Next Piece Button P1
                if (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*3 and mousePos[1] < sizeNode*4):
                    clearGamepad(b.topSurf)
                    b.p1Index = (b.p1Index + 1) % 21
                    drawPiece(sizeNode*3,0,b.p1Array[b.p1Index], b.topSurf)
                #Rotate Left Button P1
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*4 and mousePos[1] < sizeNode*5):
                    clearGamepad(b.topSurf)
                    b.p1Array[b.p1Index].rotateLeft()
                    drawPiece(sizeNode*3,0,b.p1Array[b.p1Index], b.topSurf)
                #Rotate Right Button P1
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*5 and mousePos[1] < sizeNode*6):
                    clearGamepad(b.topSurf)
                    b.p1Array[b.p1Index].rotateRight()
                    drawPiece(sizeNode*3,0,b.p1Array[b.p1Index], b.topSurf)
                #Flip Button P1
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*6 and mousePos[1] < sizeNode*7):
                    clearGamepad(b.topSurf)
                    b.p1Array[b.p1Index].flip()
                    drawPiece(sizeNode*3,0,b.p1Array[b.p1Index], b.topSurf)
                #Previous Piece Button P2
                if (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*9 and mousePos[1] < sizeNode*10):
                    clearGamepad(b.bottomSurf)
                    b.p2Index = (b.p2Index - 1) % 21
                    drawPiece(sizeNode*3,0,b.p2Array[b.p2Index], b.bottomSurf)
                #Next Piece Button P2
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*10 and mousePos[1] < sizeNode*11):
                    clearGamepad(b.bottomSurf)
                    b.p2Index = (b.p2Index + 1) % 21
                    drawPiece(sizeNode*3,0,b.p2Array[b.p2Index], b.bottomSurf)
                #Rotate Left Button P2
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*11 and mousePos[1] < sizeNode*12):
                    clearGamepad(b.bottomSurf)
                    b.p2Array[b.p2Index].rotateLeft()
                    drawPiece(sizeNode*3,0,b.p2Array[b.p2Index], b.bottomSurf)
                #Rotate Right Button P2
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*12 and mousePos[1] < sizeNode*13):
                    clearGamepad(b.bottomSurf)
                    b.p2Array[b.p2Index].rotateRight()
                    drawPiece(sizeNode*3,0,b.p2Array[b.p2Index], b.bottomSurf)
                #Flip Button P2
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*13 and mousePos[1] < sizeNode*14):
                    clearGamepad(b.bottomSurf)
                    b.p2Array[b.p2Index].flip()
                    drawPiece(sizeNode*3,0,b.p2Array[b.p2Index], b.bottomSurf)
                #Place piece on grid
                elif (mousePos[0] < heightWindow):
                    makeMove(b, mousePos[0], mousePos[1], p)
                    p = not p
                    placedCoords = [mousePos[0]//sizeNode, mousePos[1]//sizeNode]
                    
        #piece shows up on mouse if in grid
        mousePos = pygame.mouse.get_pos()
        if (mousePos[0]//sizeNode != placedCoords[0] and mousePos[1]//sizeNode != placedCoords[1]):
            placedCoords = [-1,-1]
            if (mousePos[0] < heightWindow and mousePos[0] > 0 and mousePos[1] < heightWindow and mousePos[1] > 0):
                ix = mousePos[0] // sizeNode
                iy = mousePos[1] // sizeNode
                if (p):
                    b.drawGhostPiece(ix, iy, b.p1Array[b.p1Index], b.boardSurf)
                else:
                    b.drawGhostPiece(ix, iy, b.p2Array[b.p2Index], b.boardSurf)

        window.fill(pygame.Color('grey')) # gives window a grey background
        window.blit(b.boardSurf, (0, 0)) # draws the window
        window.blit(b.topSurf, (heightWindow, 0)) # draws the gamepad
        window.blit(b.bottomSurf, (heightWindow, heightWindow/2)) # draws the gamepad
        pygame.display.flip() # updates window
        clock.tick(22)

# given mouse coordinates x, y, and player p (True = 1, False = 2), make move if legal
def makeMove(b, x, y, p):
    # initialize placeholder variables
    if (p):
        occ = 1
        corner = 2
        side = 5
        piece = b.p1Array[b.p1Index]
    else:
        occ = 3
        corner = 4
        side = 6
        piece = b.p2Array[b.p2Index]

    x = x // sizeNode
    y = y // sizeNode

    pieceOffsetXL = len(piece.arr) // 2
    pieceOffsetXR = len(piece.arr) // 2
    if (len(piece.arr) % 2 == 0):
        pieceOffsetXR = (len(piece.arr) - 1) // 2
    pieceOffsetYT = len(piece.arr[0]) // 2
    pieceOffsetYB = len(piece.arr[0]) // 2
    if (len(piece.arr[0]) % 2 == 0):
        pieceOffsetYB = (len(piece.arr[0]) - 1) // 2

    # check if move is legal
    inBounds = True
    
    # check bounds
    for i in range(x, x + len(piece.arr)):
        for j in range(y, y + len(piece.arr[0])):
            temp = piece.arr[i - x][j - y]
            if ((x - (pieceOffsetXL - 1)) < 0 or (x + pieceOffsetXR) > size or (y - (pieceOffsetYT - 1)) < 0 or (y + pieceOffsetYB) > size):
                inBounds = False
                break

    # check if touching any sides
    touchingSides = False
    for i in range(x, x + len(piece.arr)):
        for j in range(y, y + len(piece.arr[0])):
            if (piece.arr[i - x][j - y] == side and b.boardArray[i-pieceOffsetXL][j-pieceOffsetYT] == occ):
                return
            
    # check if touching corner
    touchingCorner = False
    for i in range(x, x + len(piece.arr)):
        for j in range(y, y + len(piece.arr[0])):
            if (piece.arr[i - x][j - y] == corner and b.boardArray[i-pieceOffsetXL][j-pieceOffsetYT] == occ):
                touchingCorner = True
                break

    # place piece
    if (inBounds and touchingCorner and not touchingSides):
        for i in range(x, x + len(piece.arr)):
            for j in range(y, y + len(piece.arr[0])):
                if (piece.arr[i - x][j - y] == occ):
                    b.boardArray[i-pieceOffsetXL][j-pieceOffsetYT] = occ
        b.drawBoard()
        
if __name__ == '__main__':
    main()
    
