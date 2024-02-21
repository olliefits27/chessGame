import pygame

WHITE = (255, 255, 255)
RED = (102,0,0)
WIDTH = 200
HEIGHT = 200

class Tile:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.highlighted_colour = RED
        self.highlighted = False

    def draw(self, window):
        if self.highlighted == True:
            pygame.draw.rect(window, self.highlighted_colour, (self.x+WIDTH, self.y+HEIGHT, self.width, self.width))
        else:
            pygame.draw.rect(window, self.colour, (self.x+WIDTH, self.y+HEIGHT, self.width, self.width))

    def highlight(self):
        self.highlighted = True

    def unhighlight(self):
        self.highlighted = False