import pygame
from piece_classes.piece import Piece

class Rook(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.name = 'r'
        self.image = pygame.image.load(f"piece_images/{colour}_rook.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)

    def get_legal_moves(self, piece, positionX, positionY, board):
        legal_moves = []
        cross = super().get_rook_cross(positionX, positionY)
        for direction in cross:
            for move in direction:
                if type(board[move[1]][move[0]]) == str:
                    legal_moves.append(tuple(move))
                else:
                    if board[move[1]][move[0]].colour != piece.colour:
                        legal_moves.append(tuple(move))
                        break
                    else:
                        break
        return legal_moves