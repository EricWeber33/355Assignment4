import pygame
from board import *

def main():
    pygame.init()
    
    # basic mxn window
    window = pygame.display.set_mode((widthWindow, heightWindow))
    b = Board()
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
                
        window.fill(pygame.Color('grey')) # gives window a grey background
        window.blit(b.boardSurf, (0, 0)) # draws the window
        window.blit(b.topSurf, (heightWindow, 0)) # draws the gamepad
        window.blit(b.bottomSurf, (heightWindow, heightWindow/2)) # draws the gamepad
        pygame.display.flip() # updates window
        clock.tick(60)    
    
if __name__ == '__main__':
    main()
    
