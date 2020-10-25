#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs
import pygame
import os

#Dimension variables
sizeNode = 48
size = 14
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

def create_surface():
    board = pygame.Surface((sizeNode*size, sizeNode*size)) # size of surface
    # colour the nodes black and white 
    black = False 
    for y in range(size):
        for x in range(size):
            rect = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
            pygame.draw.rect(board, pygame.Color('black' if black else 'white'), rect) # draw a black or white node
            black = not black
        black = not black
    return board

def create_gamepad_top():
    # the piece window
    board = pygame.Surface((gamepadSizeX, gamepadSizeY)) # size of surface
    pieceWindow = pygame.Rect(sizeNode*3, 0, gamepadSizeX-sizeNode*3, gamepadSizeY) # size and location of gamepad
    pygame.draw.rect(board, pygame.Color('black'), pieceWindow) # draw top gamepad
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

def create_gamepad_bottom():
    # the piece window
    board = pygame.Surface((gamepadSizeX, gamepadSizeY)) # size of surface
    pieceWindow = pygame.Rect(sizeNode*3, 0, gamepadSizeX-sizeNode*3, gamepadSizeY) # size and location of gamepad
    pygame.draw.rect(board, pygame.Color('black'), pieceWindow) # draw top gamepad
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

def create_board():
    # creates a empty board array
    board = []
    # creates a sizexsize with each node having None
    for y in range(size):
        board.append([])
        for x in range(size):
            board[y].append(None)
    return board

def main():
    pygame.init()
    
    # basic mxn window
    window = pygame.display.set_mode((widthWindow, heightWindow))
    board = create_board() # creates empty board
    surface = create_surface() #creates surface of board
    gamepadTop = create_gamepad_top() # creates top gamepad
    gamepadBottom = create_gamepad_bottom() # creates bottom gamepad 
    clock = pygame.time.Clock()
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
                    print('1 previouspiece')
                #Next Piece Button P1
                if (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*3 and mousePos[1] < sizeNode*4):
                    print('1 nextpiece')
                #Rotate Left Button P1
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*4 and mousePos[1] < sizeNode*5):
                    print('1 rotateleft')
                #Rotate Right Button P1
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*5 and mousePos[1] < sizeNode*6):
                    print('1 rotateright')
                #Flip Button P1
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*6 and mousePos[1] < sizeNode*7):
                    print('1 flip')
                #Previous Piece Button P2
                if (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*9 and mousePos[1] < sizeNode*10):
                    print('2 previouspiece')
                #Next Piece Button P2
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*10 and mousePos[1] < sizeNode*11):
                    print('2 nextpiece')
                #Rotate Left Button P2
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*11 and mousePos[1] < sizeNode*12):
                    print('2 rotateleft')
                #Rotate Right Button P2
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*12 and mousePos[1] < sizeNode*13):
                    print('2 rotateright')
                #Flip Button P2
                elif (mousePos[0] > heightWindow and mousePos[0] < heightWindow + sizeNode*3 and mousePos[1] > sizeNode*13 and mousePos[1] < sizeNode*14):
                    print('2 flip')
                
        window.fill(pygame.Color('grey')) # gives window a grey background
        window.blit(surface, (0, 0)) # draws the window
        window.blit(gamepadTop, (heightWindow, 0)) # draws the gamepad
        window.blit(gamepadBottom, (heightWindow, heightWindow/2)) # draws the gamepad
        pygame.display.flip() # updates window
        clock.tick(60)    
    
if __name__ == '__main__':
    main()
    
    
