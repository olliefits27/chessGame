import pygame
from board import Board
import sys
import time

LENGTH = 1000
WIDTH = 1200
BLUE = (0,68,116)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 87, 51)

pygame.font.init()

my_font = pygame.font.SysFont('consolas', 50)
header_text = my_font.render("Chess", False, RED)
turn_text_white = my_font.render("White's turn", False, WHITE)
turn_text_black = my_font.render("Black's turn", False, BLACK)
white_wins = my_font.render("White Wins", False, WHITE)
black_wins = my_font.render("Black Wins", False, BLACK)

turncount = 0
winner = False

def change_state(window):
    window.fill(BLUE)
    board.update_display(window)
    board.show_pieces(window)
    window.blit(header_text, (530, 50))
    if turncount % 2 != 0:
        window.blit(turn_text_black, (450, 100))
    else:
        window.blit(turn_text_white, (450, 100))
    if winner == "w":
        window.blit(white_wins, (450, 150))
    if winner == "b":
        window.blit(black_wins, (450, 150))
    board.piece_selected = not board.piece_selected

def try_move_piece(legal_moves, new_position_coords):
    global turncount
    global game_over
    global winner
    if board.move_is_legal(legal_moves, new_position_coords):
        tile.unhighlight()
        turncount += 1
        board.move_selected_piece(selected_piece, new_position_coords)
        winner = board.get_winner()
        change_state(window)
        board.change_turn()

window = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("CHESS")
window.fill(BLUE)
window.blit(header_text, (530, 50))
window.blit(turn_text_white, (450, 100))
board = Board(window)
board.update_display(window)
board.show_pieces(window)
game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position_coords = pygame.mouse.get_pos()
            if position_coords[0] > 1000 or position_coords[0] < 200:
                continue
            board_position = board.find_board_item(position_coords)
            if board.piece_selected == False:
                if board_position != False:
                    piece, tile = board_position
                    if piece.colour == board.turn:
                        legal_moves = board.get_legal_moves(piece, position_coords)
                        selected_piece = piece
                        tile.highlight()
                        change_state(window)
                else:
                    continue
            else:
                if board_position != False:
                    newPiece, newTile = board_position
                    if selected_piece == newPiece:
                        tile.unhighlight()
                        change_state(window)
                    else:
                        try_move_piece(legal_moves, position_coords)
                else:
                    try_move_piece(legal_moves, position_coords)

    pygame.display.update()
    if winner != False:
        time.sleep(3)
        game_over = True