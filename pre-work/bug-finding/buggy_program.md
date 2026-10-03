# Buggy Program

This is to explain how I found the bugs and document the fixes.


## Part 1


 1. Line 3 is missing a colon
	- At the end of function definition, there needs to be a colon. One is missing from the function at line 3
	- SyntaxError
	- def  calculate_stats(numbers):
	- Found myself
	
	
 2. Line 10 is missing a colon
	- Conditionals need colons at the end as well
	- SyntaxError
	- if  num  >  average:
	- Found myself

3. Line 20 
	- has a string type when it should be a number
	- TypeError
	- scores  = [85, 92, 78, 95, 88, 70, 93]
	- Found myself
4. Line 24 
	- Not surrounding the object key in quotes, so it comes back as undefined
	- NameError
	- scores  = [85, 92, 78, 95, 88, 70, 93]
	- Found myself




## Part 2
I chose grade_analyzer.py to ask AI three questions for improvement.

1. "How can I make this code more Pythonic?"
	- At line 6 enumerate(scores)` creates an index i` that the loop never uses. Write`for score in scores:`
	- No error
	- for score in scores:
	- Found using AI
	- I will implement it because it is correct that the index is not used and not needed.
	- Code still works
2. "What edge cases am I not handling?"
	-   **Scores outside the expected range:**  Negative scores and scores above 100 are accepted and included in the report. At line 41
	- No error
	- if  0  <=  score  <=  100:
	- Found using AI
	- I will implement it because it is correct that the the input number could not be between 0 and 100
	- Code still works
3. "Are there any security or reliability concerns?"
	-  Non-integer input crashes the program: `int(new_score)` raises `ValueError` for blank input or text. Also, `"Done"` does not exit as intended because it reaches that conversion first. Normalize the input with `.strip().lower()` and handle conversion errors around lines 39-47.
	- ValueError
	- new_score  =  input("Enter a score (or 'done' to finish): ").strip()
	- Found using AI
	- I will implement it because it is correct that the the input could be better normalized and made more reliable
	- Code still works
