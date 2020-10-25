#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs
import pygame

#Dimension variables
sizeNode = 48
size = 14
heightWindow = sizeNode*size
widthWindow = heightWindow + 10*sizeNode
gamepadSizeX = widthWindow - (sizeNode*size)
gamepadSizeY = (sizeNode*size)/2

#Image surfaces
player1Image = pygame.image.load('player1.png')
player2Image = pygame.image.load('player2.png')
nextPieceImage = pygame.image.load('nextPiece.png')
rotateRightImage = pygame.image.load('rotateRight.png')
rotateLeftImage = pygame.image.load('rotateLeft.png')
flipImage = pygame.image.load('flip.png')

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
    pygame.draw.rect(board, pygame.Color('red'), pieceWindow) # draw top gamepad
    # Player Label
    board.blit(player1Image, (0,0))
    # Next Piece Button
    board.blit(nextPieceImage, (sizeNode*3,0))
    # Rotate Right Button
    board.blit(rotateRightImage, (sizeNode*4,0))
    # Rotate Left Button
    board.blit(rotateLeftImage, (sizeNode*5,0))
    # Flip Button
    board.blit(flipImage, (sizeNode*6,0))
#    myFont = pygame.font.Font('freesansbold.ttf', 36)
#    playerLabel = myFont.render('Player 1', True, pygame.Color('blue'), pygame.Color('gray'))
#    playerLabelRect = playerLabel.get_rect(top=0, left=0, width=sizeNode*3, height=sizeNode*3)
#    board.blit(playerLabel, (0,0))
    """# left arrow
    leftArrow = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('blue'), leftArrow) # draw a black or white node     
    # right arrow
    rightArrow = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('red'), rightArrow) # draw a black or white node     
    # rotate button
    rotateButton = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('orange'), rotateButton) # draw a black or white node     
    # play button
    playButton = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('pink'), playButton) # draw a black or white node
    """
    return board

def create_gamepad_bottom():
    # the piece window
    board = pygame.Surface((gamepadSizeX, gamepadSizeY)) # size of surface
    pieceWindow = pygame.Rect(sizeNode*3, 0, gamepadSizeX-sizeNode*3, gamepadSizeY) # size and location of gamepad
    pygame.draw.rect(board, pygame.Color('green'), pieceWindow) # draw top gamepad
    # Player Label
    board.blit(player1Image, (0,0))
    # Next Piece Button
    board.blit(nextPieceImage, (sizeNode*3,0))
    # Rotate Right Button
    board.blit(rotateRightImage, (sizeNode*4,0))
    # Rotate Left Button
    board.blit(rotateLeftImage, (sizeNode*5,0))
    # Flip Button
    board.blit(flipImage, (sizeNode*6,0))
    """# left arrow
    leftArrow = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('blue'), leftArrow) # draw a black or white node     
    # right arrow
    rightArrow = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('red'), rightArrow) # draw a black or white node     
    # rotate button
    rotateButton = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('orange'), rotateButton) # draw a black or white node     
    # play button
    playButton = pygame.Rect(x*sizeNode, y*sizeNode, sizeNode, sizeNode) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('pink'), playButton) # draw a black or white node
    """
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
        window.fill(pygame.Color('grey')) # gives window a grey background
        window.blit(surface, (0, 0)) # draws the window
        window.blit(gamepadTop, (heightWindow, 0)) # draws the gamepad
        window.blit(gamepadBottom, (heightWindow, heightWindow/2)) # draws the gamepad
        pygame.display.flip() # updates window
        clock.tick(60)    
    
if __name__ == '__main__':
    main()
    
    
