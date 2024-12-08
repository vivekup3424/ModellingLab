import numpy as np
import random
import os
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class ConnectFour:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.board = np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))
        self.PLAYER_PIECE = 1
        self.AI_PIECE = 2
        self.WINDOW_LENGTH = 4
        self.EMPTY = 0

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[self.ROW_COUNT - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.ROW_COUNT):
            if self.board[r][col] == 0:
                return r
        return None

    def print_board(self):
        clear_screen()
        print("\nConnect Four - You (X) vs AI (O)\n")
        # Print column numbers
        print(" ", end="")
        for j in range(self.COLUMN_COUNT):
            print(f" {j+1} ", end="")
        print("\n")

        # Print board
        for r in range(self.ROW_COUNT - 1, -1, -1):
            print("|", end="")
            for c in range(self.COLUMN_COUNT):
                if self.board[r][c] == 0:
                    print(" · ", end="")
                elif self.board[r][c] == 1:
                    print(" X ", end="")
                else:
                    print(" O ", end="")
            print("|")
        print("-" * (self.COLUMN_COUNT * 3 + 2))

    def winning_move(self, piece):
        # Horizontal
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if (
                    self.board[r][c] == piece
                    and self.board[r][c + 1] == piece
                    and self.board[r][c + 2] == piece
                    and self.board[r][c + 3] == piece
                ):
                    return True

        # Vertical
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT - 3):
                if (
                    self.board[r][c] == piece
                    and self.board[r + 1][c] == piece
                    and self.board[r + 2][c] == piece
                    and self.board[r + 3][c] == piece
                ):
                    return True

        # Diagonal (positive slope)
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if (
                    self.board[r][c] == piece
                    and self.board[r + 1][c + 1] == piece
                    and self.board[r + 2][c + 2] == piece
                    and self.board[r + 3][c + 3] == piece
                ):
                    return True

        # Diagonal (negative slope)
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if (
                    self.board[r][c] == piece
                    and self.board[r - 1][c + 1] == piece
                    and self.board[r - 2][c + 2] == piece
                    and self.board[r - 3][c + 3] == piece
                ):
                    return True

        return False

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = self.PLAYER_PIECE if piece == self.AI_PIECE else self.AI_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(self.EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(self.EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(self.EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, piece):
        score = 0

        # Center column
        center_array = [int(i) for i in list(self.board[:, self.COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Horizontal
        for r in range(self.ROW_COUNT):
            row_array = [int(i) for i in list(self.board[r, :])]
            for c in range(self.COLUMN_COUNT - 3):
                window = row_array[c : c + self.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Vertical
        for c in range(self.COLUMN_COUNT):
            col_array = [int(i) for i in list(self.board[:, c])]
            for r in range(self.ROW_COUNT - 3):
                window = col_array[r : r + self.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Diagonal (positive slope)
        for r in range(self.ROW_COUNT - 3):
            for c in range(self.COLUMN_COUNT - 3):
                window = [self.board[r + i][c + i] for i in range(self.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        # Diagonal (negative slope)
        for r in range(3, self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT - 3):
                window = [self.board[r - i][c + i] for i in range(self.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def is_terminal_node(self):
        return (
            self.winning_move(self.PLAYER_PIECE)
            or self.winning_move(self.AI_PIECE)
            or len(self.get_valid_locations()) == 0
        )

    def get_valid_locations(self):
        valid_locations = []
        for col in range(self.COLUMN_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def minimax(self, depth, alpha, beta, maximizing_player):
        valid_locations = self.get_valid_locations()
        is_terminal = self.is_terminal_node()

        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winning_move(self.AI_PIECE):
                    return (None, 100000000000000)
                elif self.winning_move(self.PLAYER_PIECE):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, self.score_position(self.AI_PIECE))

        if maximizing_player:
            value = float("-inf")
            column = random.choice(valid_locations)

            for col in valid_locations:
                row = self.get_next_open_row(col)
                temp_board = self.board.copy()
                self.drop_piece(row, col, self.AI_PIECE)
                new_score = self.minimax(depth - 1, alpha, beta, False)[1]
                self.board = temp_board

                if new_score > value:
                    value = new_score
                    column = col

                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return column, value

        else:  # Minimizing player
            value = float("inf")
            column = random.choice(valid_locations)

            for col in valid_locations:
                row = self.get_next_open_row(col)
                temp_board = self.board.copy()
                self.drop_piece(row, col, self.PLAYER_PIECE)
                new_score = self.minimax(depth - 1, alpha, beta, True)[1]
                self.board = temp_board

                if new_score < value:
                    value = new_score
                    column = col

                beta = min(beta, value)
                if alpha >= beta:
                    break

            return column, value

    def play_game(self):
        game_over = False
        turn = random.randint(0, 1)  # Randomly decide who goes first

        while not game_over:
            self.print_board()

            if turn == 0:  # Player's turn
                print("\nYour turn!")
                valid_move = False
                while not valid_move:
                    try:
                        col = int(input("Choose column (1-7): ")) - 1
                        if 0 <= col <= 6:
                            if self.is_valid_location(col):
                                row = self.get_next_open_row(col)
                                self.drop_piece(row, col, self.PLAYER_PIECE)
                                valid_move = True
                            else:
                                print("Column is full! Try again.")
                        else:
                            print("Invalid column! Choose between 1 and 7.")
                    except ValueError:
                        print("Invalid input! Enter a number between 1 and 7.")

                if self.winning_move(self.PLAYER_PIECE):
                    self.print_board()
                    print("\nCongratulations! You win!")
                    game_over = True

            else:  # AI's turn
                print("\nAI is thinking...")
                time.sleep(1)  # Add a small delay to make it feel more natural
                col, minimax_score = self.minimax(5, float("-inf"), float("inf"), True)

                if self.is_valid_location(col):
                    row = self.get_next_open_row(col)
                    self.drop_piece(row, col, self.AI_PIECE)

                    if self.winning_move(self.AI_PIECE):
                        self.print_board()
                        print("\nAI wins! Better luck next time!")
                        game_over = True

            if not game_over and len(self.get_valid_locations()) == 0:
                self.print_board()
                print("\nIt's a tie!")
                game_over = True

            turn = (turn + 1) % 2


if __name__ == "__main__":
    while True:
        clear_screen()
        print("Welcome to Connect Four!")
        print("\nRules:")
        print("- Connect 4 pieces vertically, horizontally, or diagonally to win")
        print("- You are X, AI is O")
        print("- Choose a column number between 1-7 to drop your piece")
        input("\nPress Enter to start...")

        game = ConnectFour()
        game.play_game()

        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing!")
            break
