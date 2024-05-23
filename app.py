import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x400")
        
        self.word_list = ["python", "hangman", "challenge", "interface", "programming"]
        self.word = random.choice(self.word_list).upper()
        self.word_display = ["_" for _ in self.word]
        self.guesses = set()
        self.max_attempts = 6
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.word_label = tk.Label(self.root, text=" ".join(self.word_display), font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess, font=("Helvetica", 16))
        self.guess_button.pack(pady=10)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.max_attempts - self.attempts}", font=("Helvetica", 16))
        self.attempts_label.pack(pady=10)

    def check_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)
        
        if not guess.isalpha() or len(guess) != 1:
            messagebox.showerror("Invalid input", "Please enter a single letter.")
            return
        
        if guess in self.guesses:
            messagebox.showwarning("Repeated guess", "You have already guessed that letter.")
            return

        self.guesses.add(guess)
        
        if guess in self.word:
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_display[idx] = guess
        else:
            self.attempts += 1

        self.word_label.config(text=" ".join(self.word_display))
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts - self.attempts}")

        if "_" not in self.word_display:
            messagebox.showinfo("Hangman", "Congratulations! You've won!")
            self.reset_game()
        elif self.attempts >= self.max_attempts:
            messagebox.showinfo("Hangman", f"Game Over! The word was {self.word}")
            self.reset_game()

    def reset_game(self):
        self.word = random.choice(self.word_list).upper()
        self.word_display = ["_" for _ in self.word]
        self.guesses = set()
        self.attempts = 0
        self.word_label.config(text=" ".join(self.word_display))
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
