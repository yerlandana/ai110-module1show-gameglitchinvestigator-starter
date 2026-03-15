# 💭 Reflection: Game Glitch Investigator

Glitch 1 — it also shows go lower when should go higher and vise versa
Glitch 2 —  New Game always picks a secret from 1–100, ignoring difficulty 
Glitch 3 —  Score gives points for wrong guesses that are "Too High" on even attempts


## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- **AI tools used:** Claude Code (Anthropic) via the VSCode extension.

- **Correct AI suggestion:** Claude Code identified that `check_guess` in [app.py](app.py) had swapped hint messages — when the guess was too high it said "Go HIGHER!" and when too low it said "Go LOWER!", the opposite of what the player needs. The fix was to swap the strings so `guess > secret` returns "Go LOWER!" and `guess < secret` returns "Go HIGHER!". I verified this by running the game, entering a number I knew was above the secret (visible in Developer Debug Info), and confirming the hint now correctly said "Go LOWER!".

- **Incorrect or misleading AI suggestion:** Claude Code initially listed the swapped hints as one of 10 separate glitches (Glitch 4) citing the even/odd string comparison as the root cause, but that was a separate (deeper) issue. The more visible, direct cause of the wrong hints was simply the swapped message strings on lines 38–40. The AI's framing made it seem like fixing the string comparison would fix the hints, when in reality the messages themselves were wrong regardless. I verified by reading `check_guess` line by line and confirming the messages were swapped even before any type coercion happened.

---

## 3. Debugging and testing your fixes

- **How I decided a bug was really fixed:** I used the Developer Debug Info expander in the running Streamlit app to see the secret number, then made guesses I knew were above and below it to confirm the hint directions were correct. For the difficulty range fix, I started a new Hard game and confirmed the secret was above 100.

- **Test I ran:** I added three pytest cases to [tests/test_game_logic.py](tests/test_game_logic.py) targeting the swapped hint bug:
  - `test_too_high_message_says_go_lower` — asserts that guessing 60 when secret is 50 returns a message containing "LOWER".
  - `test_too_low_message_says_go_higher` — asserts that guessing 40 when secret is 50 returns a message containing "HIGHER".
  - `test_hint_messages_are_not_swapped` — regression guard checking both directions together.
  These tests would have caught the original bug immediately because the old messages would have failed the `assert "LOWER" in message` check.

- **AI help with tests:** Yes — Claude Code generated all three targeted test cases after I described the bug. I reviewed each assertion to confirm it matched the expected fixed behavior before accepting the change.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
