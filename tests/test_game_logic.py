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


# --- Tests for the second round of fixes ---
from logic_utils import parse_guess


def test_parse_guess_accepts_valid_in_range():
    assert parse_guess("50", 1, 100) == (True, 50, None)
    assert parse_guess(" 7 ", 1, 20) == (True, 7, None)
    assert parse_guess("5.0", 1, 20) == (True, 5, None)


def test_parse_guess_rejects_out_of_range():
    for raw in ["0", "-5", "21", "9999"]:
        ok, value, err = parse_guess(raw, 1, 20)
        assert not ok and value is None
        assert "between 1 and 20" in err


def test_parse_guess_rejects_decimals_instead_of_truncating():
    ok, value, err = parse_guess("3.9", 1, 20)
    assert not ok and value is None
    assert err == "Enter a whole number."


def test_parse_guess_rejects_empty_and_non_numbers():
    for raw in [None, "", "   "]:
        assert parse_guess(raw, 1, 20)[0] is False
    for raw in ["abc", "nan", "inf", "1e400"]:
        assert parse_guess(raw, 1, 20)[0] is False


def test_parse_guess_without_range_skips_range_check():
    assert parse_guess("9999") == (True, 9999, None)


# --- Difficulty config: range and attempts must stay consistent ---
import math
from logic_utils import DIFFICULTY_SETTINGS, get_attempt_limit, get_range_for_difficulty


def test_every_difficulty_is_winnable_by_binary_search():
    # Attempts must be >= ceil(log2(range size)), otherwise a win isn't guaranteed
    for name in DIFFICULTY_SETTINGS:
        low, high = get_range_for_difficulty(name)
        needed = math.ceil(math.log2(high - low + 1))
        assert get_attempt_limit(name) >= needed, name


def test_getters_match_settings_and_unknown_falls_back_to_normal():
    for name, cfg in DIFFICULTY_SETTINGS.items():
        assert get_range_for_difficulty(name) == (cfg["low"], cfg["high"])
        assert get_attempt_limit(name) == cfg["attempts"]
    assert get_range_for_difficulty("Nope") == get_range_for_difficulty("Normal")
    assert get_attempt_limit("Nope") == get_attempt_limit("Normal")
