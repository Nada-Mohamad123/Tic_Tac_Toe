import tkinter as tk
from logic import (
    create_board,
    find_best_move,
    evaluate,
    is_moves_left,
    PLAYER,
    AI,
    EMPTY
)

# Initialize game state
board = create_board()
current_turn = PLAYER

def check_winner():
    score = evaluate(board)
    if score == 10:
        status_label.config(text="AI wins!")
        disable_buttons()
        return True
    elif score == -10:
        status_label.config(text="You win!")
        disable_buttons()
        return True
    elif not is_moves_left(board):
        status_label.config(text="It's a draw!")
        disable_buttons()
        return True
    return False

def on_click(i, j):
    global current_turn
    if board[i][j] == EMPTY and current_turn == PLAYER:
        board[i][j] = PLAYER
        buttons[i][j].config(text=PLAYER, state='disabled')
        if not check_winner():
            current_turn = AI
            status_label.config(text="AI is thinking...")
            root.after(500, ai_turn)

def ai_turn():
    global current_turn
    i, j = find_best_move(board)
    if i != -1 and j != -1:
        board[i][j] = AI
        buttons[i][j].config(text=AI, state='disabled')
    if not check_winner():
        current_turn = PLAYER
        status_label.config(text="Your turn!")

def disable_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state='disabled')

def enable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state='normal')
            board[i][j] = EMPTY

def restart_game():
    global current_turn, board
    enable_buttons()
    board = create_board()
    current_turn = starter.get()
    if current_turn == PLAYER:
        status_label.config(text="Your turn!")
    else:
        status_label.config(text="AI is thinking...")
        root.after(500, ai_turn)

# GUI Setup
root = tk.Tk()
root.title("Tic Tac Toe (Minimax + Alpha Beta)")

starter = tk.StringVar(value=PLAYER)

starter_frame = tk.Frame(root)
starter_frame.grid(row=0, column=0, columnspan=3)
tk.Label(starter_frame, text="Who starts:").pack(side=tk.LEFT)
tk.Radiobutton(starter_frame, text="You (X)", variable=starter, value=PLAYER).pack(side=tk.LEFT)
tk.Radiobutton(starter_frame, text="AI (O)", variable=starter, value=AI).pack(side=tk.LEFT)

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            root,
            text='',
            font='Helvetica 20',
            width=5,
            height=2,
            command=lambda i=i, j=j: on_click(i, j)
        )
        buttons[i][j].grid(row=i+1, column=j)

status_label = tk.Label(root, text="Your turn!", font='Helvetica 14')
status_label.grid(row=4, column=0, columnspan=3)

restart_button = tk.Button(root, text="Restart Game", font='Helvetica 12', command=restart_game)
restart_button.grid(row=5, column=0, columnspan=3, pady=10)

# Start the game initially
restart_game()
root.mainloop()
