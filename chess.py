import pygame, sys
from pygame.locals import *

FPS = 30

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BROWN = (75, 57, 41)
LIGHT_BROWN = (154, 132, 104)
DARK_GRAY = (52, 52, 52)
LIGHT_GRAY = (92, 92, 92)
BLUE = (0 , 0, 255)

SCALE = 0.18

SQUARE_SIDE = 80

def rescale(img):
    w, h = img.get_size()
    return pygame.transform.smoothscale(img, (int(w * SCALE), int(h * SCALE)))


class Board():
    def __init__(self):
        self.WHITE_PAWN = rescale(pygame.image.load("white-pawn.png"))
        self.WHITE_ROOK = rescale(pygame.image.load("white-rook.png"))
        self.WHITE_BISHOP = rescale(pygame.image.load("white-bishop.png"))
        self.WHITE_KNIGHT = rescale(pygame.image.load("white-knight.png"))
        self.WHITE_QUEEN = rescale(pygame.image.load("white-queen.png"))
        self.WHITE_KING = rescale(pygame.image.load("white-king.png"))
        self.BLACK_PAWN = rescale(pygame.image.load("black-pawn.png"))
        self.BLACK_ROOK = rescale(pygame.image.load("black-rook.png"))
        self.BLACK_BISHOP = rescale(pygame.image.load("black-bishop.png"))
        self.BLACK_KNIGHT = rescale(pygame.image.load("black-knight.png"))
        self.BLACK_QUEEN = rescale(pygame.image.load("black-queen.png"))
        self.BLACK_KING = rescale(pygame.image.load("black-king.png"))

        self.whitePawnRect = self.WHITE_PAWN.get_rect()
        self.whiteRookRect = self.WHITE_ROOK.get_rect()
        self.whiteBishopRect = self.WHITE_BISHOP.get_rect()
        self.whiteKnightRect = self.WHITE_KNIGHT.get_rect()
        self.whiteQueenRect = self.WHITE_QUEEN.get_rect()
        self.whiteKingRect = self.WHITE_KING.get_rect()
        self.blackPawnRect = self.BLACK_PAWN.get_rect()
        self.blackRookRect = self.BLACK_ROOK.get_rect()
        self.blackBishopRect = self.BLACK_BISHOP.get_rect()
        self.blackKnightRect = self.BLACK_KNIGHT.get_rect()
        self.blackQueenRect = self.BLACK_QUEEN.get_rect()
        self.blackKingRect = self.BLACK_KING.get_rect()
        
        self.BOARD = [
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
            ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
        ]

        self.sprites = {
            "WP" : (self.WHITE_PAWN, self.whitePawnRect),
            "WR" : (self.WHITE_ROOK, self.whiteRookRect),
            "WB" : (self.WHITE_BISHOP, self.whiteBishopRect),
            "WN" : (self.WHITE_KNIGHT, self.whiteKnightRect),
            "WQ" : (self.WHITE_QUEEN, self.whiteQueenRect),
            "WK" : (self.WHITE_KING, self.whiteKingRect),
            "BP" : (self.BLACK_PAWN, self.blackPawnRect),
            "BR" : (self.BLACK_ROOK, self.blackRookRect),
            "BB" : (self.BLACK_BISHOP, self.blackBishopRect),
            "BN" : (self.BLACK_KNIGHT, self.blackKnightRect),
            "BQ" : (self.BLACK_QUEEN, self.blackQueenRect),
            "BK" : (self.BLACK_KING, self.blackKingRect)
        }

    def drawGrid(self, lightColor, darkColor):
        color = darkColor
        for sqrY in range(0, 640, 80):
            if color == lightColor:
                color = darkColor
            else:
                color = lightColor
            for sqrX in range(0, 640, 80):
                pygame.draw.rect(SCREEN_SURF, color, (sqrX, sqrY, SQUARE_SIDE, SQUARE_SIDE))
                if color == lightColor:
                    color = darkColor
                else:
                    color = lightColor

    def drawBoard(self):
        self.drawGrid(LIGHT_GRAY, DARK_GRAY)

        for i in range(8):
            for j in range(8):
                if self.BOARD[i][j] != -1:
                    self.sprites[self.BOARD[i][j]][1].center = ((j*SQUARE_SIDE)+40, (i*SQUARE_SIDE)+40)
                    SCREEN_SURF.blit(self.sprites[self.BOARD[i][j]][0], self.sprites[self.BOARD[i][j]][1])


    def highlightSquare(self, coordX, coordY):
        squareIndexX = coordX // 80
        squareIndexY = coordY // 80
        pygame.draw.rect(SCREEN_SURF, BLUE, (squareIndexX*80, squareIndexY*80, SQUARE_SIDE, SQUARE_SIDE), 6)


    def movePiece(self, startCoords, endCoords):
        startIndexX = startCoords[0] // 80
        startIndexY = startCoords[1] // 80
        endIndexX = endCoords[0] // 80
        endIndexY = endCoords[1] // 80

        self.BOARD[endIndexY][endIndexX] = self.BOARD[startIndexY][startIndexX]
        self.BOARD[startIndexY][startIndexX] = -1

class Chess():
    def main(self):
        global FPS_CLOCK, SCREEN_SURF
        pygame.display.set_caption("Chess")
        SCREEN_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        FPS_CLOCK = pygame.time.Clock()

        BOARD = Board()

        mouseX = 0
        mouseY = 0

        firstSelection = None

        while True:
            mouseClicked = False

            BOARD.drawBoard()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mouseX, mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mouseX, mouseY = event.pos
                    mouseClicked = True
            
            BOARD.highlightSquare(mouseX, mouseY)

            if mouseClicked:
                if firstSelection == None:
                    firstSelection = (mouseX, mouseY)
                else:
                    BOARD.movePiece(firstSelection, (mouseX, mouseY))
                    firstSelection = None

            pygame.display.update()
            FPS_CLOCK.tick(FPS)


if __name__ == "__main__":
    pygame.init()

    game = Chess()
    game.main()