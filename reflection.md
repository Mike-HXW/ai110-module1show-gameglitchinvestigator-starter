# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  Tons of bugs appears. No correct guess can be made with wrong hints. UI is broken either and fails to reflect game states.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  Hints are provided opposite directions. No integer can hit the answer under the trials I make.
  UI presentation like number range, winning state etc. do not refresh after restart the game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected code location
|--------------------------|-------------------|-----------------------|-----------------------|
| guess 9 | Go Lower hint | Go Higher hint | None | app.py check_guess |
| Difficulty Easy | show "guess a number between 1-20." | show "guess a number  between 1-100" | None | app.py get_range_for_difficulty |
| Difficulty Easy | have 1-20 secret | have 73,84 as secret | None | app.py |      

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  I asked AI the way to completely reset the game. It adds on all missing reset components on the original missing part. I verified it by passing tests on it. I also tested it in actual environment
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  When I asked AI to write test on check_guess block, it keeps just GO HIGHER except too low, which is inconsistent with the existing test case and not plain enough. So I change it to keep both part in the output. Therefore the hint texts are both consistent with the result and give a cheerful guide on next step.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decide it by whether it passes through related test cases. I also tested related utilities on the actual app. I also checked with AI with the related code blocks.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  The test test_parse_guess_rejects_empty_and_non_numbers tests several weird inputs in pauss_guess. This makes sure that they are not handled and moved forward. The function deals all input issue which all later parts have no need to consider more.
- Did AI help you design or understand any tests? How?
  AI did a great help on design and understand tests. It quickly proposes edge cases that should be handled specifically by my code It also wrote tedius test module title name very fast.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns the whole program from top to bottom every time you click a button or type in a box, so any normal variable gets reset each time. Session state is like a small notebook that Streamlit keeps between reruns, so things like the secret number, score and attempts don't disappear. In this game, I had to keep those values in session state and be careful about where each line sits in the script, because a line that runs before a click is handled shows the old value.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I learn from this project is to deeply collaborate with AI to help me debug. AI now is very sufficient in handling minor issues that is hard to observe by humans. It will be useful to ask AI for check when some fundamental changes are made before moving forward.
- What is one thing you would do differently next time you work with AI on a coding task?
  One thing I would do differently is to make AI show what it changes. Otherwise it takes some time for me to locate the related code. Though it is a utility of GitHub, it is more efficient to handle it before commiting it.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  It is very powerful, especially compared to old models which can hardly grasp complex problems just a couple years ago.
