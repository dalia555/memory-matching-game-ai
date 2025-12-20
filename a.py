import random


flat_cards = ['A', 'A', 'B', 'B', 'C', 'C']
random.shuffle(flat_cards)

# Reshape into 2x3 grid
cards = [flat_cards[:3], flat_cards[3:]]

matched =[
     [False,False,False],
     [False,False,False]
]   
memory = {} 
def print_memory():
    print("\nCurrent AI Memory:")
    for card, positions in memory.items():
        unmatched_positions = [pos for pos in positions if not matched[pos[0]][pos[1]]]
        if unmatched_positions:  
            print(f"{card}: {unmatched_positions}")
    print()

ai_score =0
player_score =0

print("Welcome to Memory Matching Game")
def show_board():
    for r in range(2):
        for c in range(3):
            if matched[r][c]:
                print(cards[r][c], end=" ")
            else:
                print("*", end=" ")
        print() 




def check_match(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return cards[r1][c1]==cards[r2][c2]


def ai_move():
    global ai_score
    
    
    for card, positions in memory.items():   #here to see if i have matching cards
        unmatched_positions = [pos for pos in positions if not matched[pos[0]][pos[1]]]
        if len(unmatched_positions) == 2:
            pos1, pos2 = unmatched_positions
        
            print(f"AI flips {card} at {pos1} and {pos2}")
            if check_match(pos1, pos2):
                matched[pos1[0]][pos1[1]] = True
                matched[pos2[0]][pos2[1]] = True
                ai_score += 1
                print("AI found a match!")
            print_memory()
            return 
        
    all_unmatched = [(r, c) for r in range(2) for c in range(3) if not matched[r][c]]
    pos1, pos2 = random.sample(all_unmatched, 2)     # to pick to random cards  
    val1 = cards[pos1[0]][pos1[1]]  
    val2 = cards[pos2[0]][pos2[1]]
    print(f"AI flips {cards[pos1[0]][pos1[1]]} at {pos1} and {cards[pos2[0]][pos2[1]]} at {pos2}")     
   
    

    if (pos1 not in memory.setdefault(val1, [])):
                   memory[val1].append(pos1)
    if (pos2 not in memory.setdefault(val2, [])):
              memory[val2].append(pos2)
    if check_match(pos1, pos2):
        matched[pos1[0]][pos1[1]] = True
        matched[pos2[0]][pos2[1]] = True
        ai_score += 1
        print("AI found a match!")
    print_memory()



def player_move():
    global player_score
    while True:
        try:
            pos1 = tuple(map(int, input("Enter first card position (row col): ").split()))
            pos2 = tuple(map(int, input("Enter second card position (row col): ").split()))
            if pos1 == pos2 or matched[pos1[0]][pos1[1]] or matched[pos2[0]][pos2[1]]:
                print("Invalid positions, try again.")
                continue
            break
        except:
            print("Invalid input. Format: row col (e.g., 0 1)")

    val1 = cards[pos1[0]][pos1[1]]
    val2 = cards[pos2[0]][pos2[1]]
    print(f"You flipped {val1} and {val2}")

    # Update AI memory
    if pos1 not in memory.setdefault(val1, []):
        memory[val1].append(pos1)
    if pos2 not in memory.setdefault(val2, []):
        memory[val2].append(pos2)
    
    if check_match(pos1, pos2):
        matched[pos1[0]][pos1[1]] = True
        matched[pos2[0]][pos2[1]] = True
        player_score += 1
        print("You found a match!")


while not all(all(row) for row in matched):
    show_board()
    print("Your turn:")
    player_move()
    show_board()
    
    if all(all(row) for row in matched):
        break
    
    print("AI's turn:")
    ai_move()


# Game finished
print("\nGame finished!")
show_board()
print(f"Your score: {player_score}")
print(f"AI score: {ai_score}")

if player_score > ai_score:
    print("You win!")
elif ai_score > player_score:
    print("AI wins!")
else:
    print("It's a tie!")



