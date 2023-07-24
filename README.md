# The-Wordle-

### Game Description:

Wordle Puzzle Setter is a unique word-guessing game where you take on the role of the puzzle setter. You get to select a secret 5-letter word as the puzzle, and the computer will attempt to solve it based on the hints you provide after each guess. The game provides three types of hints: "Green" hints represent correct letters in the correct positions, "Yellow" hints indicate correct letters but in the wrong positions, and "Grey" hints signify incorrect letters that are not present in the secret word.
The objective of the game is to challenge the computer to solve your word puzzle within a limited number of attempts.

### Functions used :

1. **load_word_list(file_path: str) -> list[str]:**
   - Loads the word list from the specified file path on the local disk.
   - The word list serves as the pool of valid words from which the puzzle setter selects the secret word.

2. **select_random_word(word_list: list[str]) -> str:**
   - Takes a list of words as input and returns a randomly chosen word from that list.
   - This function is used to select a random word for the computer's guesses during the game.

3. **is_valid_word(word: str, word_list: list[str]) -> bool:**
   - Checks if a given word is valid and exists in the word list.
   - Used to validate the puzzle set by the player and the computer's guesses.

4. **generate_hints(guess: str, secret_word: str) -> list[tuple[str, int]]:**
   - Generates hints for the computer's guess based on the secret word (puzzle).
   - Categorizes the letters of the guess as green (correct letter in correct position), yellow (correct letter in the wrong position), or grey (incorrect letter).

5. **player_set_puzzle(word_list: list[str]) -> str:**
   - Allows the player (puzzle setter) to set the puzzle by entering a valid 5-letter word.
   - Ensures the entered word is valid and has five letters before accepting it as the puzzle.

6. **computer_play_wordle(puzzle: str, word_list: list[str]) -> None:**
   - Implements the computer AI gameplay to guess the puzzle set by the player.
   - The computer will make up to 6 attempts to solve the puzzle based on the hints provided by the player.

7. **print_hints(hints: list[tuple[str, int]]) -> None:**
   - Formats and prints the hints provided to the computer after each guess.
   - Displays the hints as 'G' for green, 'Y' for yellow, and 'X' for grey.

