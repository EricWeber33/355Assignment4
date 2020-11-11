#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs
import pygame
import os
import copy
from piece import Piece

#Dimension variables
sizeNode = 48
size = 14
gamepadGridSize = 7
heightWindow = sizeNode*size
widthWindow = heightWindow + 10*sizeNode
gamepadSizeX = widthWindow - (sizeNode*size)
gamepadSizeY = (sizeNode*size)/2

#Image surfaces
currentPath = os.path.dirname(__file__)
imagesPath = os.path.join(currentPath, 'images')
player1Image = pygame.image.load(os.path.join(imagesPath, 'p1.png'))
player2Image = pygame.image.load(os.path.join(imagesPath, 'p2.png'))
previousPieceImage = pygame.image.load(os.path.join(imagesPath, 'previous.png'))
nextPieceImage = pygame.image.load(os.path.join(imagesPath, 'next.png'))
rotateLeftImage = pygame.image.load(os.path.join(imagesPath, 'rotateRight.png'))
rotateRightImage = pygame.image.load(os.path.join(imagesPath, 'rotateLeft.png'))
flipImage = pygame.image.load(os.path.join(imagesPath, 'flip.png'))

#Colors
player1Color = 'dodgerblue4'
player2Color = 'firebrick4'
player1Ghost = 'dodgerblue1'
player2Ghost = 'firebrick1'

class Board:

    def __init__(self):
        # index of pieceArray
        self.p1Index = 0
        self.p2Index = 0
        
        # array of 2D arrays representing pieces
        self.p1Array = []
        self.p2Array = []

        # fill with pieces
        pieceFileArray = os.listdir('./tiles')
        pieceFileArray.sort()
        for p in pieceFileArray:
            if ('p1' in p):
                self.p1Array.append(Piece(p))

        for p in pieceFileArray:
            if ('p2' in p):
                self.p2Array.append(Piece(p))
        
        # board array
        self.boardArray = []
        # board surface object
        self.boardSurf = self.create_surface()

        # top gamepad array
        self.topArray = []
        # top gamepad surface object
        self.topSurf = self.create_gamepad_top()
        drawPiece(sizeNode*3,0,self.p1Array[self.p1Index], self.topSurf)
        
        # bottom gamepad array
        self.bottomArray = []
        # bottom gamepad surface object
        self.bottomSurf = self.create_gamepad_bottom()
        drawPiece(sizeNode*3,0,self.p2Array[self.p2Index], self.bottomSurf)

        #initialize board array
        for y in range(size + 2):
            self.boardArray.append([])
            for x in range(size + 2):
                self.boardArray[y].append(0)

        #initialize guard rows/cols in board array
        for i in range(size + 2):
            self.boardArray[-1][i] = 7

        for i in range(size + 2):
            self.boardArray[i][-1] = 7

        for i in range(size + 2):
            self.boardArray[size][i] = 7

        for i in range(size + 2):
            self.boardArray[i][size] = 7

        #add guard pieces to be able to start game
        self.boardArray[-1][-1] = 1
        self.boardArray[size][-1] = 1
        self.boardArray[size][size] = 3
        self.boardArray[-1][size] = 3

        # previous ghost piece
        self.pGhost = copy.deepcopy(self.boardArray)

        #initialize gamepad arrays
        for y in range(gamepadGridSize):
            self.topArray.append([])
            self.bottomArray.append([])
            for x in range(gamepadGridSize):
                self.topArray[y].append(0)
                self.bottomArray[y].append(0)

    def create_surface(self):
        board = pygame.Surface((sizeNode*size, sizeNode*size)) # size of surface
        
        # colour the nodes black and white 
        black = False
        for y in range(size):
            for x in range(size):
                rect = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
                pygame.draw.rect(board, pygame.Color('light gray' if black else 'gray'), rect) # draw a black or white node
                black = not black
            black = not black
            
        return board

    def create_gamepad_top(self):
        # the piece window
        board = pygame.Surface((gamepadSizeX, gamepadSizeY)) # size of surface
        pieceWindow = pygame.Rect(sizeNode*3, 0, gamepadSizeX-sizeNode*3, gamepadSizeY) # size and location of gamepad
        
        # Player Label
        board.blit(player1Image, (0,0))
        # Previous Piece Button
        board.blit(previousPieceImage, (0,sizeNode*2))
        # Next Piece Button
        board.blit(nextPieceImage, (0,sizeNode*3))
        # Rotate Right Button
        board.blit(rotateRightImage, (0,sizeNode*4))
        # Rotate Left Button
        board.blit(rotateLeftImage, (0,sizeNode*5))
        # Flip Button
        board.blit(flipImage, (0,sizeNode*6))

        return board

    def create_gamepad_bottom(self):
        # the piece window
        board = pygame.Surface((gamepadSizeX, gamepadSizeY)) # size of surface
        pieceWindow = pygame.Rect(sizeNode*3, 0, gamepadSizeX-sizeNode*3, gamepadSizeY) # size and location of gamepad

        # Player Label
        board.blit(player2Image, (0,0))
        # Previous Piece Button
        board.blit(previousPieceImage, (0,sizeNode*2))
        # Next Piece Button
        board.blit(nextPieceImage, (0,sizeNode*3))
        # Rotate Right Button
        board.blit(rotateRightImage, (0,sizeNode*4))
        # Rotate Left Button
        board.blit(rotateLeftImage, (0,sizeNode*5))
        # Flip Button
        board.blit(flipImage, (0,sizeNode*6))    

        return board

    def drawBoard(self):
        for x in range(size):
            for y in range(size):
                rect = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
                if (self.boardArray[x][y] == 1):
                    color = player1Color
                elif (self.boardArray[x][y] == 3):
                    color = player2Color
                elif (self.boardArray[x][y] == 8):
                    color = player1Ghost
                elif (self.boardArray[x][y] == 9):
                    color = player2Ghost
                elif ((x % 2 == 0) and (y % 2 == 1) or (x % 2 == 1) and (y % 2 == 0)):
                    color = 'light grey'
                else:
                    color = 'grey'
                pygame.draw.rect(self.boardSurf, pygame.Color(color), rect) # draw a black or white node

    def drawGhostPiece(self, x, y, piece, surf):
        #initialize offset depending on parity of piece array rows/cols
        pieceOffsetXL = len(piece.arr) // 2
        pieceOffsetXR = len(piece.arr) // 2
        if (len(piece.arr) % 2 == 0):
            pieceOffsetXR = (len(piece.arr) - 1) // 2
        pieceOffsetYT = len(piece.arr[0]) // 2
        pieceOffsetYB = len(piece.arr[0]) // 2
        if (len(piece.arr[0]) % 2 == 0):
            pieceOffsetYB = (len(piece.arr[0]) - 1) // 2
        
        # erase the previous ghost piece
        for i in range(len(self.pGhost)):
            for j in range(len(self.pGhost[0])):
                if ((self.pGhost[i][j] == 8 or self.pGhost[i][j] == 9) and (self.boardArray[i][j] == 8 or self.boardArray[i][j] == 9) and i < size and j < size):
                    self.boardArray[i][j] = 0
                    self.pGhost[i][j] = 0

        # check if we should draw the new ghost piece
        drawGhost = True
        for i in range(x, x + len(piece.arr)):
            for j in range(y, y + len(piece.arr[0])):
                temp = piece.arr[i - x][j - y]
                if ((x - (pieceOffsetXL - 1)) < 0 or (x + pieceOffsetXR) > size or (y - (pieceOffsetYT - 1)) < 0 or (y + pieceOffsetYB) > size):
                    drawGhost = False
                    break
                if ((self.boardArray[i-pieceOffsetXL][j-pieceOffsetYT] == 1 or self.boardArray[i-pieceOffsetXL][j-pieceOffsetYT] == 3) and (temp == 1 or temp == 3)):
                    drawGhost = False
                    break

        #draw the new ghost piece
        if (drawGhost):
            for i in range(x, x + len(piece.arr)):
                for j in range(y, y + len(piece.arr[0])):
                    temp = piece.arr[i - x][j - y]
                    if (temp == 1 and i - pieceOffsetXL < size and j - pieceOffsetYT < size):
                        self.boardArray[i-pieceOffsetXL][j-pieceOffsetYT] = 8
                        self.pGhost[i-pieceOffsetXL][j-pieceOffsetYT] = 8
                    elif (temp == 3 and i - pieceOffsetXL < size and j - pieceOffsetYT < size):
                        self.boardArray[i-pieceOffsetXL][j-pieceOffsetYT] = 9
                        self.pGhost[i-pieceOffsetXL][j-pieceOffsetYT] = 9

        self.drawBoard()            

#reset the gamepad grid to empty
def clearGamepad(surf):
    rect = pygame.Rect(sizeNode*3, 0, sizeNode*gamepadGridSize, sizeNode*gamepadGridSize)
    pygame.draw.rect(surf, pygame.Color('black'), rect)
                    
#draws a piece 'piece' on surface 'surf' in the color of player 'player'
def drawPiece(x, y, piece, surf):
    for i in range(len(piece.arr)):
        for j in range(len(piece.arr[0])):
            if (piece.arr[i][j] == 1 or piece.arr[i][j] == 3):
                rect = pygame.Rect(x + i*sizeNode, y + j*sizeNode, sizeNode, sizeNode)
                pygame.draw.rect(surf, pygame.Color(player1Color if (piece.arr[i][j] == 1) else player2Color), rect)                    
