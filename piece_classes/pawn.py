import pygame
from piece_classes.piece import Piece

class Pawn(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.name = 'p'
        self.image = pygame.image.load(f"piece_images/{colour}_pawn.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)

    def get_legal_moves(self, piece, positionX, positionY, board):
        legal_moves = []
        if piece.colour == "w":
            movement_in_y = -1
        else:
            movement_in_y = 1
        if type(board[positionY+movement_in_y][positionX]) == str:
            legal_moves.append((positionX, positionY+movement_in_y))
            if (piece.colour == "w" and positionY == 6) or (piece.colour == "b" and positionY == 1):
                if type(board[positionY+(2*movement_in_y)][positionX]) == str :
                    legal_moves.append((positionX, (2*movement_in_y)+positionY))
        if positionX == 0:
            adjacentLeft = ""
        else:
            adjacentLeft = board[positionY + movement_in_y][positionX - 1]
        if positionX == 7:
            adjacentRight = ""
        else:
            adjacentRight = board[positionY+movement_in_y][positionX+1]
        if type(adjacentLeft) != str and adjacentLeft.colour != piece.colour:
            legal_moves.append((positionX-1,positionY+movement_in_y))
        if type(adjacentRight) != str and adjacentRight.colour != piece.colour:
            legal_moves.append((positionX+1,positionY+movement_in_y))
        return legal_moves