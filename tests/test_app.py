import pytest
from app import HangmanGame
import tkinter as tk

class MockRoot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()

@pytest.fixture
def app():
    root = MockRoot()
    game = HangmanGame(root)
    return game

def test_check_guess(app):
    app.word = "TEST"
    app.word_display = ["_" for _ in app.word]
    app.max_attempts = 6
    app.attempts = 0
    app.guesses = set()
    app.word_label.config(text=" ".join(app.word_display))

    # Test a correct guess
    app.guess_entry.insert(0, 'T')
    app.check_guess()
    assert app.word_display == ['T', '_', '_', 'T']

    # Test an incorrect guess
    app.guess_entry.delete(0, 'end')
    app.guess_entry.insert(0, 'A')
    app.check_guess()
    assert app.attempts == 1

if __name__ == "__main__":
    pytest.main()
