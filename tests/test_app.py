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
    for letter in set(app.word):
        app.guess_entry.insert(0, letter)
        app.check_guess()
    assert "_" not in app.word_display
    assert app.attempts < app.max_attempts

def test_game_over(app):
    incorrect_letter = 'Z'
    while incorrect_letter in app.word:
        incorrect_letter = chr(ord(incorrect_letter) - 1)
    for _ in range(app.max_attempts):
        app.guess_entry.insert(0, incorrect_letter)
        app.check_guess()
    assert app.attempts >= app.max_attempts
