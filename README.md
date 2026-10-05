# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   The game's purpose is to guess an integer number in a fixed range in a limit number of tries. A hint of either the guess is too high or too low is provided after each guess.
- [ ] Detail which bugs you found.
   Several types of bugs are found. The first type is logic bugs, which includes an opposite direction hints and wrong score addition when attempts are even. The second type is data type handling, where some time string is used to compare with integer which leads bugs. The third type is system setting, where UI like number range, attempts, and game status are not updated when it is required.
- [ ] Explain what fixes you applied.
   With the help of AI, the first type of bugs is fixed by debugging  incorrect logics in comparison functions. The second type of bug is fixed by letting all input type handled by a single function before any further comparison is made Data type and range checking are used in the function. The third type of error is fixed by considering the workflow when and what game state should restart.  Python tests are written for all fixes. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

## Demo Walkthrough
1. User selects a difficulty, normal by default
2. User enters a guess of 50
3. Game returns "Too High! Go LOWER!"
4. User enters a guess of 30, and the game shows "Too Low! GO HIGHER"
5. After several entries, when user enters 42, game returns "Correct!"
6. A celebration effects appear with the corrected final score based on guess times.
7. Game ends here, user can switch diffculties or start new games if needed


