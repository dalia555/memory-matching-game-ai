import random
import tkinter as tk
from tkinter import messagebox

# Initialize cards and shuffle
flat_cards = ['A', 'A', 'B', 'B', 'C', 'C']
random.shuffle(flat_cards)
cards = [flat_cards[:3], flat_cards[3:]]

matched = [[False]*3 for _ in range(2)]
memory = {}

ai_score = 0
player_score = 0
player_turn = True

root = tk.Tk()
root.title("Memory Matching Game")

buttons = [[None]*3 for _ in range(2)]
revealed = []

score_label = tk.Label(root, text=f"Player: {player_score}  AI: {ai_score}", font=("Arial", 14))
score_label.grid(row=3, column=0, columnspan=3, pady=10)

def print_memory():
    print("\nCurrent AI Memory:")
    for card, positions in memory.items():
        unmatched_positions = [pos for pos in positions if not matched[pos[0]][pos[1]]]
        if unmatched_positions:
            print(f"{card}: {unmatched_positions}")

def update_score():
    score_label.config(text=f"Player: {player_score}  AI: {ai_score}")

def show_card(r, c):
    buttons[r][c].config(text=cards[r][c], state="disabled")

def hide_card(r, c):
    if not matched[r][c]:
        buttons[r][c].config(text="*", state="normal")

def check_match(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return cards[r1][c1] == cards[r2][c2]

def end_game():
    if player_score > ai_score:
        msg = "You win!"
    elif ai_score > player_score:
        msg = "AI wins!"
    else:
        msg = "It's a tie!"
    messagebox.showinfo("Game Over", f"Game finished!\nPlayer score: {player_score}\nAI score: {ai_score}\n{msg}")
    root.quit()

def ai_move():
    global ai_score, player_turn

    # Check if AI already knows a matching pair
    for card, positions in memory.items():
        unmatched_positions = [pos for pos in positions if not matched[pos[0]][pos[1]]]
        if len(unmatched_positions) == 2:
            pos1, pos2 = unmatched_positions
            break
    else:
        # Pick two random unmatched cards
        all_unmatched = [(r, c) for r in range(2) for c in range(3) if not matched[r][c]]
        pos1, pos2 = random.sample(all_unmatched, 2)

    r1, c1 = pos1
    r2, c2 = pos2
    show_card(r1, c1)
    show_card(r2, c2)
    root.update()
    root.after(1000)  # Pause so player can see AI's move

    val1 = cards[r1][c1]
    val2 = cards[r2][c2]

    # Update AI memory
    if pos1 not in memory.setdefault(val1, []):
        memory[val1].append(pos1)
    if pos2 not in memory.setdefault(val2, []):
        memory[val2].append(pos2)

    if check_match(pos1, pos2):
        matched[r1][c1] = True
        matched[r2][c2] = True
        ai_score += 1
        print(f"AI found a match: {val1} at {pos1} and {pos2}")
    else:
        hide_card(r1, c1)
        hide_card(r2, c2)

    update_score()

    if all(all(row) for row in matched):
        end_game()
    else:
        player_turn = True

clicked = []

def on_click(r, c):
    global player_score, player_turn, clicked

    if not player_turn or matched[r][c] or (r,c) in clicked:
        return

    show_card(r, c)
    clicked.append((r, c))

    if len(clicked) == 2:
        pos1, pos2 = clicked
        val1 = cards[pos1[0]][pos1[1]]
        val2 = cards[pos2[0]][pos2[1]]

        # Update AI memory
        if pos1 not in memory.setdefault(val1, []):
            memory[val1].append(pos1)
        if pos2 not in memory.setdefault(val2, []):
            memory[val2].append(pos2)

        if check_match(pos1, pos2):
            matched[pos1[0]][pos1[1]] = True
            matched[pos2[0]][pos2[1]] = True
            player_score += 1
            update_score()
            clicked = []
            if all(all(row) for row in matched):
                end_game()
            return
        else:
            player_turn = False
            root.after(1000, hide_mismatch)

def hide_mismatch():
    global clicked, player_turn
    for r, c in clicked:
        hide_card(r, c)
    clicked = []
    update_score()
    ai_move()

# Create buttons for cards
for r in range(2):
    for c in range(3):
        btn = tk.Button(root, text="*", width=6, height=3, font=("Arial", 24),
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = btn

root.mainloop()
