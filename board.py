#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs

# Meaning of boardArray values
# 0: empty space
# 1: player 1 occupied
# 2: player 1 corner
# 5: player 1 side
# 3: player 2 occupied
# 4: player 2 corner
# 6: player 2 side
# 7: guard cell
# 8: player 1 ghost
# 9: player 2 ghost

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
gamepadSizeY = (sizeNode*size)//2

#Image surfaces
currentPath = os.path.dirname(__file__)
imagesPath = os.path.join(currentPath, 'images')
player1Image = pygame.image.load(os.path.join(imagesPath, 'p1.png'))
player2Image = pygame.image.load(os.path.join(imagesPath, 'p2.png'))
passImage = pygame.image.load(os.path.join(imagesPath, 'pass.png'))
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
endgameColor = 'dark orange'

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

        # initialize diagnostics
        self.p1Score = 0
        self.p2Score = 0
        self.p1Pieces = len(self.p1Array)
        self.p2Pieces = len(self.p2Array)

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

    def create_endgame(self):
        # erase the previous ghost piece
        for i in range(len(self.pGhost)):
            for j in range(len(self.pGhost[0])):
                if ((self.pGhost[i][j] == 8 or self.pGhost[i][j] == 9) and (self.boardArray[i][j] == 8 or self.boardArray[i][j] == 9) and i < size and j < size):
                    self.boardArray[i][j] = 0
                    self.pGhost[i][j] = 0
        self.drawBoard()
        
        # set up steps
        pygame.font.init()
        titleFont = pygame.font.SysFont('arial', 50)
        myFont = pygame.font.SysFont('arial', 30)
        
        # the endgame surface
        endGameSurf = pygame.Surface((gamepadSizeX, gamepadSizeY * 2))

        # the title text surface
        titleSurf = titleFont.render('GAME OVER', False, pygame.Color(endgameColor))

        # the score text surfaces
        p1ScoreSurf = myFont.render("Player 1 Score: " + str(self.p1Score), False, pygame.Color(endgameColor))
        p2ScoreSurf = myFont.render("Player 2 Score: " + str(self.p2Score), False, pygame.Color(endgameColor))

        # the pieces left text surfaces
        p1PiecesSurf = myFont.render("Player 1 Pieces remaining: " + str(self.p1Pieces), False, pygame.Color(endgameColor))
        p2PiecesSurf = myFont.render("Player 2 Pieces remaining: " + str(self.p2Pieces), False, pygame.Color(endgameColor))

        # calculate empty tiles and void tiles
        empties = 0
        p1Voids = 0
        p2Voids = 0
        for i in range(len(self.boardArray)):
            for j in range(len(self.boardArray[i])):
                if (self.boardArray[i][j] == 0):
                    # increment empties
                    empties += 1

                    # increment voids
                    p1Increment = False
                    p2Increment = False
                    if (i > 0):
                        if (self.boardArray[i-1][j] == 1):
                            p1Increment = True
                        elif (self.boardArray[i-1][j] == 3):
                            p2Increment = True
                    if (i < (size - 1)):
                        if (self.boardArray[i+1][j] == 1):
                            p1Increment = True
                        elif (self.boardArray[i+1][j] == 3):
                            p2Increment = True
                    if (j > 0):
                        if (self.boardArray[i][j-1] == 1):
                            p1Increment = True
                        elif (self.boardArray[i][j-1] == 3):
                            p2Increment = True
                    if(j < (size - 1)):
                        if (self.boardArray[i][j+1] == 1):
                            p1Increment = True
                        elif (self.boardArray[i][j+1] == 3):
                            p2Increment = True
                    if(p1Increment): p1Voids += 1
                    if(p2Increment): p2Voids += 1
        
        # the empties text surface
        emptiesSurf = myFont.render("Empty Tiles: " + str(empties), False, pygame.Color(endgameColor))

        # the voids text surfaces
        p1VoidsSurf = myFont.render("Player 1 Void tiles: " + str(p1Voids), False, pygame.Color(endgameColor))
        p2VoidsSurf = myFont.render("Player 2 Void tiles: " + str(p2Voids), False, pygame.Color(endgameColor))

        # winning player surface
        if (self.p1Score > self.p2Score):
            winnerSurf = titleFont.render("Player 1 Wins!", False, pygame.Color(player1Color))
        elif (self.p1Score < self.p2Score):
            winnerSurf = titleFont.render("Player 2 Wins!", False, pygame.Color(player2Color))
        else:
            winnerSurf = titleFont.render("Draw!", False, pygame.Color('magenta'))            

        # blit diagnostics onto endgame surface
        endGameSurf.blit(titleSurf, (sizeNode*2,0))
        endGameSurf.blit(p1ScoreSurf, (sizeNode,sizeNode*2))
        endGameSurf.blit(p2ScoreSurf, (sizeNode,sizeNode*3))
        endGameSurf.blit(p1PiecesSurf, (sizeNode,sizeNode*4))
        endGameSurf.blit(p2PiecesSurf, (sizeNode,sizeNode*5))
        endGameSurf.blit(p1VoidsSurf, (sizeNode,sizeNode*6))
        endGameSurf.blit(p2VoidsSurf, (sizeNode,sizeNode*7))
        endGameSurf.blit(emptiesSurf, (sizeNode,sizeNode*8))
        endGameSurf.blit(winnerSurf, (sizeNode,sizeNode*10))

        return endGameSurf

    def create_gamepad_top(self):
        # the piece window
        board = pygame.Surface((gamepadSizeX, gamepadSizeY)) # size of surface
        pieceWindow = pygame.Rect(sizeNode*3, 0, gamepadSizeX-sizeNode*3, gamepadSizeY) # size and location of gamepad
        
        # Player Label
        board.blit(player1Image, (0,0))
        # Pass Button
        board.blit(passImage, (0,sizeNode))
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
        pieceWindow = pygame.Rect(sizeNode*3, 0, gamepadSizeX-sizeNode*3, gamepadSizeY) # location and size of gamepad

        # Player Label
        board.blit(player2Image, (0,0))
        # Pass Button
        board.blit(passImage, (0,sizeNode))
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

    def calc_score(self, p):
        score = -2
        for r in self.boardArray:
            for c in r:
                if (p and c == 1):
                    score += 1
                elif (not p and c == 3):
                    score += 1
        return score

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

def calcDiagnostics(b):
    # diagnostic calculations
    b.p1Score = b.calc_score(True)
    b.p2Score = b.calc_score(False)
    b.p1Pieces = len(b.p1Array)
    b.p2Pieces = len(b.p2Array)

def drawDiagnostics(b):
    # set up steps
    pygame.font.init()
    myFont = pygame.font.SysFont('arial', 20)

    # the score text surfaces
    p1ScoreSurf = myFont.render("Score: " + str(b.p1Score), False, pygame.Color(player1Color))
    p2ScoreSurf = myFont.render("Score: " + str(b.p2Score), False, pygame.Color(player2Color))
    b.topSurf.blit(p1ScoreSurf, (sizeNode * 6, sizeNode * 5.5))
    b.bottomSurf.blit(p2ScoreSurf, (sizeNode * 6, sizeNode * 5.5))

    # the pieces left text surfaces
    p1PiecesSurf = myFont.render("Pieces remaining: " + str(b.p1Pieces), False, pygame.Color(player1Color))
    p2PiecesSurf = myFont.render("Pieces remaining: " + str(b.p2Pieces), False, pygame.Color(player2Color))
    b.topSurf.blit(p1PiecesSurf, (sizeNode * 6, sizeNode * 6))
    b.bottomSurf.blit(p2PiecesSurf, (sizeNode * 6, sizeNode * 6))
    
