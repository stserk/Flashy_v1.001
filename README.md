# Flashy - Language Flashcard Application

Flashy is a language learning application that helps you learn and memorize new words using flashcards. The application supports a dynamic set of flashcards and allows users to mark words as known, flip cards to see translations, and restart progress.

## Features

- **Flashcard Display:** Shows a new flashcard every few seconds with an English word.
- **Card Flipping:** Flip the card to see the translation in Russian.
- **Mark as Known:** Mark a word as known, removing it from the learning pool.
- **Restart Progress:** Option to restart learning, clearing all progress.
- **Dynamic Learning Set:** Updates the set of words to learn based on user progress.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/flashy.git
    cd flashy
    ```

2. **Install the required dependencies:**
    Ensure you have `pandas` and `tkinter` installed in your Python environment.
    ```sh
    pip install pandas
    ```

3. **Prepare your data:**
    Ensure you have the necessary CSV files and images:
    - `data/en_words.csv`: The original set of English-Russian word pairs.
    - `data/words_to_learn.csv`: Will be created and managed by the application to track learning progress.
    - `images/card_front.png`: Image for the front of the card.
    - `images/card_back.png`: Image for the back of the card.
    - `images/right.png`, `images/wrong.png`, `images/flip.png`, `images/restart.png`: Button images.

## Usage

1. **Run the application:**
    ```sh
    python flashy.py
    ```

2. **Interact with the application:**
    - Click the "Right" button if you know the word.
    - Click the "Wrong" button to skip to the next word.
    - Click the "Flip" button to flip the card and see the translation.
    - Click the "Restart" button to restart your progress.

## Code Overview

### Flashcard Logic
- `next_card()`: Displays the next word in the learning set.
- `flip_card()`: Flips the card to show the translation.
- `is_known()`: Removes the current word from the learning set if marked as known.
- `flip_back()`: Manually flips the card back to the English word.
- `restart()`: Restarts the learning progress by removing the `words_to_learn.csv` file.

### UI Setup
- The application uses Tkinter for the graphical interface.
- Images are loaded using `PhotoImage` and placed on a `Canvas` widget.
- Buttons are configured with images and linked to their respective functions.

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License.
