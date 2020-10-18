#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs
import pygame

sizeNode = 48
size = 14
widthWindow = 1100
heightWindow = 672
gamepadSizeX = widthWindow - (sizeNode*size)
gamepadSizeY = (sizeNode*size)/2

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

def create_gamepad():
    board = pygame.Surface((gamepadSizeX, gamepadSizeY)) # size of surface
    # the piece window
    pieceWindow = pygame.Rect(heightWindow*1.1, 0, gamepadSizeX-heightWindow*0.2, gamepadSizeY-heightWindow*0.2) # size and location of nodes
    pygame.draw.rect(board, pygame.Color('black'), pieceWindow) # draw a black or white node     
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
    # basic mxn window
    window = pygame.display.set_mode((widthWindow, heightWindow))
    board = create_board() # creates empty board
    surface = create_surface() #creates surface of board
    gamepad = create_gamepad() # creates player gamepad 
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
        window.blit(gamepad, (heightWindow*1.1, 0)) # draws the window
        pygame.display.flip() # updates window
        clock.tick(60)    
    
if __name__ == '__main__':
    main()
    
    