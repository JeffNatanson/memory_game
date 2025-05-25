import random
import operator
import random
import pandas as pd 

# List of card pairs (using letters for simplicity)
cards = ["A","A", "B", "C", "D", "E", "F", "G", "H"] * 2
random.shuffle(cards)

# Function to display the current state of the board()
def display_board(board, revealed):
    print("\nMemory Game Board:")
    for i in range(0, 16, 2):
        row = [board[j] if revealed[j] else "?" for j in range(i, i+4)]
        print(" ".join(row))

# Main function to run the game
def play_memory_game():
    revealed = [False] * 16
    attempts = 0
    pairs_found = 0

    print("Welcome to the Memory Game!")
    while pairs_found < 8:
        display_board(cards, revealed)

        try:
            # Player chooses two cards
            first = int(input("\nChoose the first card (1-16): ")) - 1
            second = int(input("Choose the second card (1-16): ")) - 1

            # Validate input and check if chosen cards are different
            if (first < 0 or first >= 16 or second < 0 or second >= 16 or
                first == second or revealed[first] or revealed[second]):
                print("Invalid selection. Please choose two different hidden cards.")
                continue

            # Reveal chosen cards
            revealed[first] = True
            revealed[second] = True
            display_board(cards, revealed)
            attempts += 1

            # Check for a match
            if cards[first] == cards[second]:
                print("Match found!")
                pairs_found += 1
            else:
                print("No match! Try again.")
                revealed[first] = False
                revealed[second] = False

        except ValueError:
            print("Please enter valid numbers.")

    print(f"\nCongratulations! You found all pairs in {attempts} attempts.")

# Run the game if executed directly
if __name__ == "__main__":
    play_memory_game()
