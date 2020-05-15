import pygame, sys
from pygame.locals import *

FPS = 30

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCALE = 0.4

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


    def draw_board(self):
        self.draw_grid()

        aux = {
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
            "BK" : (self.WHITE_KING, self.blackKingRect)
        }

        for i in range(8):
            for j in range(8):
                if self.BOARD[i][j] != -1:
                    aux[self.BOARD[i][j]][1].center = ((j*80)+40, (i*80)+40)
                    SCREEN_SURF.blit(aux[self.BOARD[i][j]][0], aux[self.BOARD[i][j]][1])


    def draw_grid(self):
        color = BLACK
        for sqr_y in range(0, 640, 80):
            if color == WHITE:
                color = BLACK
            else:
                color = WHITE
            for sqr_x in range(0, 640, 80):
                pygame.draw.rect(SCREEN_SURF, color, (sqr_x, sqr_y, 80, 80))
                if color == WHITE:
                    color = BLACK
                else:
                    color = WHITE

class Chess():
    def main(self):
        global FPS_CLOCK, SCREEN_SURF

        pygame.display.set_caption("Chess")
        SCREEN_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        FPS_CLOCK = pygame.time.Clock()

        BOARD = Board()
        BOARD.draw_board()
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            FPS_CLOCK.tick(FPS)


if __name__ == "__main__":
    pygame.init()

    game = Chess()
    game.main()