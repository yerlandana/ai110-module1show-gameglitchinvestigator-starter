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


# --- Tests targeting the swapped hint message bug ---

def test_too_high_message_says_go_lower():
    # Bug: when guess > secret the message incorrectly said "Go HIGHER!"
    # Fix: it should say "Go LOWER!" so the player corrects downward
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint, got: '{message}'"

def test_too_low_message_says_go_higher():
    # Bug: when guess < secret the message incorrectly said "Go LOWER!"
    # Fix: it should say "Go HIGHER!" so the player corrects upward
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint, got: '{message}'"

def test_hint_messages_are_not_swapped():
    # Regression guard: the two hint directions must be opposites of each other
    _, high_msg = check_guess(99, 1)   # way too high → go lower
    _, low_msg  = check_guess(1, 99)   # way too low  → go higher
    assert "LOWER" in high_msg and "HIGHER" not in high_msg
    assert "HIGHER" in low_msg and "LOWER" not in low_msg
