import pytest
from app import HangmanGame

class MockRoot:
    def __init__(self):
        self.title = ""
        self.geometry = ""
    
    def title(self, title):
        self.title = title

    def geometry(self, geometry):
        self.geometry = geometry

@pytest.fixture
def game():
    root = MockRoot()
    return HangmanGame(root)

def test_initial_state(game):
    assert game.attempts == 0
    assert len(game.word) > 0
    assert len(game.word_display) == len(game.word)
    assert all(letter == "_" for letter in game.word_display)
    assert game.max_attempts == 6

def test_check_guess_correct(game):
    game.word = "TEST"
    game.word_display = ["_", "_", "_", "_"]
    game.check_guess = lambda guess: HangmanGame.check_guess(game)
    game.guess_entry.get = lambda: "E"
    game.check_guess()
    assert game.word_display == ["_", "E", "_", "_"]
    assert game.attempts == 0

def test_check_guess_incorrect(game):
    game.word = "TEST"
    game.word_display = ["_", "_", "_", "_"]
    game.check_guess = lambda guess: HangmanGame.check_guess(game)
    game.guess_entry.get = lambda: "X"
    game.check_guess()
    assert game.word_display == ["_", "_", "_", "_"]
    assert game.attempts == 1

def test_game_win(game):
    game.word = "TEST"
    game.word_display = ["T", "E", "S", "T"]
    game.check_guess = lambda guess: HangmanGame.check_guess(game)
    game.guess_entry.get = lambda: "E"
    game.check_guess()
    assert game.word_display == ["T", "E", "S", "T"]
    assert game.attempts == 0

def test_game_over(game):
    game.word = "TEST"
    game.word_display = ["_", "_", "_", "_"]
    game.attempts = 5
    game.check_guess = lambda guess: HangmanGame.check_guess(game)
    game.guess_entry.get = lambda: "X"
    game.check_guess()
    assert game.attempts == 6
