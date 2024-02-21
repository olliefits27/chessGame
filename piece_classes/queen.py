import pygame
from piece_classes.piece import Piece

class Queen(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.name = 'q'
        self.image = pygame.image.load(f"piece_images/{colour}_queen.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)

    def on_board(self, move):
        return super().on_board(move)

    def get_legal_moves(self, piece, positionX, positionY, board):
        legal_moves = []
        cross = [
            [[positionX, i] for i in range(positionY - 1, -1, -1)],
            [[positionX, i] for i in range(positionY + 1, 8)],
            [[i, positionY] for i in range(positionX + 1, 8)],
            [[i, positionY] for i in range(positionX - 1, -1, -1)],
            [[positionX + i, positionY - i] for i in range(1, 8)],
            [[positionX + i, positionY + i] for i in range(1, 8)],
            [[positionX - i, positionY - i] for i in range(1, 8)],
            [[positionX - i, positionY + i] for i in range(1, 8)]
        ]
        for direction in cross:
            for move in direction:
                if self.on_board(move):
                    if type(board[move[1]][move[0]]) == str:
                        legal_moves.append(tuple(move))
                    else:
                        if board[move[1]][move[0]].colour != piece.colour:
                            legal_moves.append(tuple(move))
                            break
                        else:
                            break
        return legal_moves