import random

def load_word_list(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return [word.strip() for word in file]

def select_random_word(word_list: list[str]) -> str:
    return random.choice(word_list)

def is_valid_word(word: str, word_list: list[str]) -> bool:
    return word in word_list

def generate_hints(guess: str, secret_word: str) -> list[tuple[str, int]]:
    hints = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            hints.append(('green', i))
        elif guess[i] in secret_word:
            hints.append(('yellow', i))
        else:
            hints.append(('grey', i))
    return hints

def player_set_puzzle(word_list: list[str]) -> str:
    puzzle = ''
    while not is_valid_word(puzzle, word_list) or len(puzzle) != 5:
        puzzle = input("Enter a valid 5-letter word as the puzzle: ").lower()
    return puzzle

def computer_play_wordle(puzzle: str, word_list: list[str]) -> None:
    attempts = 1
    while attempts < 7:
        guess = select_random_word(word_list)
        print("Attempt {}: Guessing... {}".format(attempts, guess))
        hints = generate_hints(guess, puzzle)
        print_hints(hints)
        if all(hint[0] == 'green' for hint in hints):
            print("Computer solved the puzzle!")
            break
        attempts += 1
    else:
        print("Computer failed to solve the puzzle!")

def print_hints(hints: list[tuple[str, int]]) -> None:
    hint_str = [' ' for _ in range(5)]
    for hint_type, index in hints:
        if hint_type == 'green':
            hint_str[index] = 'G'
        elif hint_type == 'yellow':
            hint_str[index] = 'Y'
        else:
            hint_str[index] = 'X'
    print("Hints: {}".format(' '.join(hint_str)))

def main():
    # Replace "5.letter.words.txt" with the actual file path on your local disk
    word_list = load_word_list("5.letter.words.txt")
    print("Welcome to Wordle Puzzle Setter!")
    puzzle = player_set_puzzle(word_list)
    computer_play_wordle(puzzle, word_list)

if __name__ == "__main__":
    main()
