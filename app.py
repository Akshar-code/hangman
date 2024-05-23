import tkinter as tk

class HangmanGame:
    """
    HangmanGame is a simple hangman game implemented using Tkinter.
    """
    def __init__(self, root):
        """
        Initialize the game with the given root window.
        """
        self.root = root
        self.word = "TEST"
        self.word_display = ["_" for _ in self.word]
        self.max_attempts = 6
        self.attempts = 0
        self.guesses = set()
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets for the game.
        """
        self.word_label = tk.Label(self.root, text=" ".join(self.word_display))
        self.word_label.pack()
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()
        self.check_button = tk.Button(self.root, text="Check Guess", command=self.check_guess)
        self.check_button.pack()

    def check_guess(self):
        """
        Check the user's guess and update the game state.
        """
        guess = self.guess_entry.get().upper()
        if guess in self.guesses:
            return

        self.guesses.add(guess)
        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_display[i] = guess
            self.word_label.config(text=" ".join(self.word_display))
        else:
            self.attempts += 1

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
