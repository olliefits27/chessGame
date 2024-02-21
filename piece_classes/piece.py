class Piece:
    def highlight(self):
        print("HIGHLIGHT")

    def on_board(self, move):
        if move[0] > -1 and move[1] > -1 and move[0] < 8 and move[1] < 8:
            return True
        else:
            return False

    def get_rook_cross(self, positionX, positionY):
        cross = [
            [[positionX, i] for i in range(positionY - 1, -1, -1)],
            [[positionX, i] for i in range(positionY + 1, 8)],
            [[i, positionY] for i in range(positionX + 1, 8)],
            [[i, positionY] for i in range(positionX - 1, -1, -1)]
        ]
        return cross

    def get_bishop_cross(self, positionX, positionY):
        cross = [
            [[positionX + i, positionY - i] for i in range(1, 8)],
            [[positionX + i, positionY + i] for i in range(1, 8)],
            [[positionX - i, positionY - i] for i in range(1, 8)],
            [[positionX - i, positionY + i] for i in range(1, 8)]
        ]
        return cross