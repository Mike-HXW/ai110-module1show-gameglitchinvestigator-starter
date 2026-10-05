# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected code location
|-------|-------------------|-----------------|------------------------|---------------|
 guess 9  Go Lower hint       Go Higher hint     None                  app.py check_guess
Difficulty show "guess a number show "guess a number
   Easy     between 1-20."       between 1-100"        None            app.py get_range_for_difficulty
Difficulty have 1-20 secret. have 73,84 as secret.    None             app.py
  Easy         

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked AI the way to completely reset the game. It adds on all missing reset components on the original missing part. I verified it by TBD
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
When I asked AI to write test on check_guess block, it keeps just GO HIGHER except too low, which is inconsistent with the existing test case and not plain enough. So I change it to keep both part in the output texts to be both clear and precise.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decide it by passing through test cases and testing related utilities on the actual app
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
