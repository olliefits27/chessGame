from piece_classes.pawn import Pawn
from piece_classes.rook import Rook
from piece_classes.knight import Knight
from piece_classes.bishop import Bishop
from piece_classes.queen import Queen
from piece_classes.king import King
from tile import Tile
import pygame

DIMENSION = 800
ADDITIONAL_WIDTH = 200
ROWS = 8
BLACK = (0, 0, 0)
DARK = (184,139,74)
LIGHT = (227,193,111)
ADDITIONAL_HEIGHT = 200

class Board:
    def __init__(self, window):
        self.board = [[' ' for i in range(8)] for i in range(8)]
        self.turn = 'w'
        self.turnCount = 0
        self.piece_selected = False
        self.white_pieces_taken = []
        self.black_pieces_taken = []

        #create minor and major white pieces
        self.white_rookL = Rook('w')
        self.white_knightL = Knight('w')
        self.white_bishopL = Bishop('w')
        self.white_queen = Queen('w')
        self.white_king = King('w')
        self.white_bishopR = Bishop('w')
        self.white_knightR = Knight('w')
        self.white_rookR = Rook('w')

        #create minor and major black pieces
        self.black_rookL = Rook('b')
        self.black_knightL = Knight('b')
        self.black_bishopL = Bishop('b')
        self.black_queen = Queen('b')
        self.black_king = King('b')
        self.black_bishopR = Bishop('b')
        self.black_knightR = Knight('b')
        self.black_rookR = Rook('b')
        self.kings = [self.white_king, self.black_king]

        #add minor and major pieces to board
        self.board[7] = [self.white_rookL, self.white_knightL, self.white_bishopL, self.white_queen, self.white_king,
                         self.white_bishopR, self.white_knightR, self.white_rookR]
        self.board[0] = [self.black_rookL, self.black_knightL, self.black_bishopL, self.black_queen, self.black_king,
                         self.black_bishopR, self.black_knightR, self.black_rookR]

        #create pawns and add to board
        self.white_pawns = []
        self.black_pawns = []
        for i in range(8):
            white_pawn = Pawn('w')
            black_pawn = Pawn('b')
            self.white_pawns.append(white_pawn)
            self.board[6][i] = white_pawn
            self.black_pawns.append(black_pawn)
            self.board[1][i] = black_pawn

        #build board
        self.grid = []
        self.gap = DIMENSION / ROWS
        for i in range(ROWS):
            self.grid.append([])
            for j in range(ROWS):
                tile = Tile(j, i, self.gap)
                self.grid[i].append(tile)
                if (i+j) % 2 == 1:
                    self.grid[i][j].colour = DARK
                else:
                    self.grid[i][j].colour = LIGHT

    def update_display(self, window):
        for row in self.grid:
            for tile in row:
                tile.draw(window)
        self.draw_gridlines(window)
        self.show_taken_pieces(window)

    def draw_gridlines(self, window):
        for i in range(ROWS):
            pygame.draw.line(window, BLACK, (0+ADDITIONAL_WIDTH, i*self.gap+ADDITIONAL_WIDTH), (DIMENSION+ADDITIONAL_WIDTH, i*self.gap+ADDITIONAL_HEIGHT))
            pygame.draw.line(window, BLACK, (i*self.gap+ADDITIONAL_WIDTH, ADDITIONAL_HEIGHT), (i*self.gap+ADDITIONAL_WIDTH, DIMENSION+ADDITIONAL_HEIGHT))

    def show_pieces(self, window):
        for xPosition, row in enumerate(self.board):
            for yPosition, piece in enumerate(row):
                if type(piece) != str:
                    window.blit(piece.image, (yPosition * self.gap + ADDITIONAL_WIDTH, xPosition * self.gap + ADDITIONAL_HEIGHT))

    def show_taken_pieces(self, window):
        for index, piece in enumerate(self.white_pieces_taken):
            if index <= 7:
                window.blit(piece.image, (0, index * self.gap + ADDITIONAL_HEIGHT))
            else:
                window.blit(piece.image, (self.gap, (index-8) * self.gap + ADDITIONAL_HEIGHT))
        for index, piece in enumerate(self.black_pieces_taken):
            if index <= 7:
                window.blit(piece.image, (1000, index * self.gap + ADDITIONAL_HEIGHT))
            else:
                window.blit(piece.image, (self.gap + 1000, (index-8) * self.gap + ADDITIONAL_HEIGHT))

    def get_board_position(self, position):
        x, y = position
        xItem = int(x // self.gap) - 2
        yItem = int(y // self.gap) - 2
        return xItem, yItem

    def find_board_item(self, position):
        xItem, yItem = self.get_board_position(position)
        piece = self.board[yItem][xItem]
        tile = self.grid[yItem][xItem]
        if type(piece) != str:
            return piece, tile
        return False

    def get_legal_moves(self, piece, position_coords):
        positionX, positionY = self.get_board_position(position_coords)
        self.currentX, self.currentY = positionX, positionY
        return piece.get_legal_moves(piece, positionX, positionY, self.board)

    def move_selected_piece(self, piece, position_coords):
        new_xItem, new_yItem = self.get_board_position(position_coords)
        if self.board[new_yItem][new_xItem] != ' ':
            if self.board[new_yItem][new_xItem].colour == 'w':
                self.white_pieces_taken.append(self.board[new_yItem][new_xItem])
            else:
                self.black_pieces_taken.append(self.board[new_yItem][new_xItem])
        self.board[new_yItem][new_xItem] = piece
        prev_yItem, prev_xItem = self.currentY, self.currentX
        self.board[prev_yItem][prev_xItem] = ' '

    def move_is_legal(self, legal_moves, new_position_coords):
        new_move = self.get_board_position(new_position_coords)
        for move in legal_moves:
            if move == new_move:
                return True

    def change_turn(self):
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'
        self.turnCount += 1

    def get_winner(self):
        for piece in self.white_pieces_taken:
            if piece == self.white_king:
                return "b"
        for piece in self.black_pieces_taken:
            if piece == self.black_king:
                return "w"
        return False