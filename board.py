#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs
import pygame
import os
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
player1Color = 'dodgerblue1'
player2Color = 'firebrick1'

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
        for y in range(size):
            self.boardArray.append([])
            for x in range(size):
                self.boardArray[y].append(0)

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

    #draws rects on surface 'dest' based on array 'arr'
    #dest is 0 for board, 1 for top gamepad, 2 for bottom gamepad
    def arrayToBoard(self, arr, dest):
        if (dest == 0):
            dimensions = size
            surf = self.boardSurf
        elif (dest == 1):
            dimensions = gamepadGridSize
            surf = self.topSurf
        else:
            dimensions = gamepadGridSize
            surf = self.bottomSurf

        #draw rects on surface
        #player 1 is dodgerblue1, player 2 is firebrick1
        for x in range(dimensions):
            for y in range(dimensions):
                if (arr[x][y] == 1 or arr[x][y] == 3):
                    rect = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode)
                    pygame.draw.rect(surf, pygame.Color(player1Color if (arr[x][y] == 1) else player2Color), rect)

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
