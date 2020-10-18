#https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs
import pygame

sizeNode = 32
size = 14

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
    window = pygame.display.set_mode((640, 480))
    board = create_board() # creates empty board
    surface = create_surface() #creates surface of board
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
        pygame.display.flip() # updates window
        clock.tick(60)    
    
if __name__ == '__main__':
    main()
    
    