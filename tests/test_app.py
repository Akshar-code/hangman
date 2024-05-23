import pytest
import tkinter as tk
from app import HangmanGame

@pytest.fixture
def app():
    root = tk.Tk()
    game = HangmanGame(root)
    yield game
    root.destroy()

def test_initial_state(app):
    assert app.word_display == ["_" for _ in app.word]
    assert app.attempts == 0
    assert app.guesses == set()

def test_check_guess_correct(app):
    initial_display = app.word_display.copy()
    correct_letter = app.word[0]
    app.guess_entry.insert(0, correct_letter)
    app.check_guess()
    assert app.word_display != initial_display
    assert correct_letter in app.guesses
    assert app.attempts == 0

def test_check_guess_incorrect(app):
    incorrect_letter = 'Z'
    while incorrect_letter in app.word:
        incorrect_letter = chr(ord(incorrect_letter) - 1)
    app.guess_entry.insert(0, incorrect_letter)
    app.check_guess()
    assert incorrect_letter in app.guesses
    assert app.attempts == 1

def test_game_win(app):
    app.word = "TEST"
    app.word_display = ["_" for _ in app.word]
    app.max_attempts = 6
    app.attempts = 0
    app.guesses = set()
    app.word_label.config(text=" ".join(app.word_display))

    print(f"Initial word_display: {app.word_display}")
    
    for letter in "TEST":
        app.guess_entry.insert(0, letter)
        app.check_guess()
        print(f"Word display after guessing '{letter}': {app.word_display}")

    assert "_" not in app.word_display
    assert app.attempts < app.max_attempts

def test_game_over(app):
    app.word = "TEST"
    app.word_display = ["_" for _ in app.word]
    app.max_attempts = 6
    app.attempts = 0
    app.guesses = set()
    app.word_label.config(text=" ".join(app.word_display))

    incorrect_letter = 'Z'
    while incorrect_letter in app.word:
        incorrect_letter = chr(ord(incorrect_letter) - 1)
    
    print(f"Initial attempts: {app.attempts}")
    
    for _ in range(app.max_attempts):
        app.guess_entry.insert(0, incorrect_letter)
        app.check_guess()
        print(f"Attempts after guessing '{incorrect_letter}': {app.attempts}")
    
    assert app.attempts >= app.max_attempts
