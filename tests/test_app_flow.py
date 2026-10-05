from streamlit.testing.v1 import AppTest

APP = "app.py"


def run_app():
    at = AppTest.from_file(APP, default_timeout=10)
    at.run()
    return at


def submit(at, text):
    at.text_input[0].set_value(text).run()
    at.button[0].click().run()


def test_info_text_uses_difficulty_range():
    at = run_app()
    assert "between 1 and 100" in at.info[0].value
    at.selectbox[0].select("Easy").run()
    assert "between 1 and 20" in at.info[0].value


def test_changing_difficulty_restarts_game():
    at = run_app()
    at.session_state.secret = 99
    submit(at, "1")
    assert at.session_state.attempts == 1
    at.selectbox[0].select("Easy").run()
    assert at.session_state.attempts == 0
    assert at.session_state.score == 0
    assert at.session_state.history == []
    assert 1 <= at.session_state.secret <= 20


def test_invalid_input_uses_no_attempt_and_no_score():
    at = run_app()
    for bad in ["abc", "", "0", "101", "3.5"]:
        submit(at, bad)
        assert at.session_state.attempts == 0
        assert at.session_state.score == 0
        assert at.error  # error message shown
    assert at.session_state.status == "playing"


def test_attempts_left_updates_right_after_guess():
    at = run_app()
    at.session_state.secret = 99
    submit(at, "1")
    assert "Attempts left: 7" in at.info[0].value  # Normal: 8 allowed


def test_game_ends_after_attempt_limit_with_valid_guesses_only():
    at = run_app()
    at.session_state.secret = 99
    submit(at, "abc")  # invalid, must not count
    for _ in range(8):
        submit(at, "1")
    assert at.session_state.status == "lost"


def debug_text(at):
    return " ".join(m.value for m in at.expander[0].markdown)


def test_debug_panel_shows_values_after_the_guess():
    at = run_app()
    at.session_state.secret = 99
    submit(at, "1")
    text = debug_text(at)
    assert "Attempts:" in text and "1" in text
    assert "Score:" in text and "-5" in text
    assert at.expander[0].json[0].value == "[1]"  # history is rendered as JSON


def test_new_game_clears_guess_box():
    at = run_app()
    at.session_state.secret = 99
    submit(at, "1")
    assert at.text_input[0].value == "1"
    at.button[1].click().run()
    assert at.text_input[0].value == ""
    assert at.session_state.attempts == 0


def test_hard_mode_is_winnable_by_binary_search():
    # 1-50 needs up to ceil(log2(50)) = 6 guesses, so Hard must allow at least 6
    at = run_app()
    at.selectbox[0].select("Hard").run()
    assert "Attempts left: 6" in at.info[0].value
    at.session_state.secret = 50  # worst case for a low-first search
    lo, hi = 1, 50
    while at.session_state.status == "playing":
        mid = (lo + hi) // 2
        submit(at, str(mid))
        if mid < 50:
            lo = mid + 1
        else:
            hi = mid - 1
    assert at.session_state.status == "won"
