import random

#FIX: Refactored four functions into logic_utils.py using agent mode
# FIX: range and attempt limit live together so they can't drift apart
DIFFICULTY_SETTINGS = {
    "Easy": {"low": 1, "high": 20, "attempts": 6},
    "Normal": {"low": 1, "high": 100, "attempts": 8},
    "Hard": {"low": 1, "high": 50, "attempts": 6},  # FIX: 5 attempts could not guarantee a win on 1-50 (needs up to 6)
}
DEFAULT_DIFFICULTY = "Normal"


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    settings = DIFFICULTY_SETTINGS.get(difficulty, DIFFICULTY_SETTINGS[DEFAULT_DIFFICULTY])
    return settings["low"], settings["high"]


def get_attempt_limit(difficulty: str):
    """Return the number of attempts allowed for a given difficulty."""
    settings = DIFFICULTY_SETTINGS.get(difficulty, DIFFICULTY_SETTINGS[DEFAULT_DIFFICULTY])
    return settings["attempts"]


def parse_guess(raw: str, low: int = None, high: int = None):
    """
    Parse user input into an int guess.

    If low/high are given, the guess must be a whole number inside that range.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()
    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            number = float(raw)
            if not number.is_integer(): # FIX: decimals are rejected, not truncated
                return False, None, "Enter a whole number."
            value = int(number)
        else:
            value = int(raw)
    except Exception: # FIX: Cast value error before check_guess using agent mode
        return False, None, "That is not a number."

    if low is not None and high is not None and not (low <= value <= high):
        return False, None, f"Enter a number between {low} and {high}." # FIX: range check

    return True, value, None


def check_guess(guess, secret): 
    """
    Compare guess to secret and return the outcome string.

    outcome: "Win", "Too High", or "Too Low"
    Both values are cast to int first, so a numeric string secret is
    compared numerically (not as text).
    """ 
    guess = int(guess) #Fix: Force to cast to integer
    secret = int(secret)

    if guess == secret: #FIX: Try is not done before comparison
        return "Win"
    if guess > secret: #FIX: Modify returns to expected outputs in test file
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number (1 = first guess)."""
    if outcome == "Win": #FIX: Correct the attempt number calculation to prevent additional one
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def new_game_state(low: int, high: int): # FIX: Addtional function handling game restart
    """Return a fresh game state with a secret inside [low, high]."""
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }
