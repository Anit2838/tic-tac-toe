import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x450")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        """Create the Tic Tac Toe board."""
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            button = tk.Button(frame, text="", font=('normal', 40, 'normal'), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        reset_button = tk.Button(self.root, text="Reset", font=('normal', 20, 'normal'), command=self.reset_board)
        reset_button.pack(pady=20)

    def on_button_click(self, index):
        """Handle button click event."""
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Check if there is a winner."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_board(self):
        """Reset the game board."""
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
