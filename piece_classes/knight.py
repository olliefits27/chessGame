import pygame
from piece_classes.piece import Piece

class Knight(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.name = 'kn'
        self.image = pygame.image.load(f"piece_images/{colour}_knight.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)

    def on_board(self, move):
        return super().on_board(move)

    def get_legal_moves(self, piece, positionX, positionY, board):
        legal_moves = []
        for x in range(-2, 3):
            for y in range(-2, 3):
                if x**2 + y**2 == 5:
                    move = [positionX + x, positionY + y]
                    if self.on_board([positionX+x, positionY+y]):
                        if type(board[move[1]][move[0]]) == str:
                            legal_moves.append(tuple(move))
                        else:
                            if board[move[1]][move[0]].colour != piece.colour:
                                legal_moves.append(tuple(move))
        return legal_moves