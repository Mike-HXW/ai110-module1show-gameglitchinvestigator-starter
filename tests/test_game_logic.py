from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Regression tests for the bugs fixed after the refactor ---
from logic_utils import new_game_state, update_score


def test_check_guess_compares_numerically_with_string_secret():
    # Bug: app passed str(secret) on even attempts -> text comparison ("9" > "10")
    assert check_guess(9, "10") == "Too Low"
    assert check_guess(10, "9") == "Too High"
    assert check_guess(10, "10") == "Win"


def test_win_score_uses_attempt_number_without_extra_plus_one():
    # Bug: win points used (attempt_number + 1), under-rewarding every win
    assert update_score(0, "Win", 1) == 90
    assert update_score(0, "Win", 3) == 70


def test_win_score_has_minimum_of_10():
    assert update_score(0, "Win", 20) == 10


def test_too_high_always_loses_points():
    # Bug: "Too High" gave +5 on even attempts
    assert update_score(0, "Too High", 2) == -5
    assert update_score(0, "Too High", 3) == -5


def test_too_low_loses_points():
    assert update_score(0, "Too Low", 2) == -5


def test_new_game_state_resets_everything():
    # Bug: New Game only reset attempts/secret, not score/status/history,
    # and ignored the difficulty range
    state = new_game_state(1, 20)
    assert 1 <= state["secret"] <= 20
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
