Project Structure:

This program has been written in top down manner. Each time the input stream is given the entire input s-expression and then it is parsed. (I have already discussed this with Prof. Soundarajan)

Main.py- Runs the Input/Output and Evaluator (Will be added in the next part)
Lisp.py- The class that contains Input, Output, Eval, DList, AList and Symbol List.
SExp.py- Class for s-expressions

The Lisp Class contains utility functions for input and output.


Running the code:

1.	execute- python Main.py
2.	copy and paste the test cases like shown below:

	(DEFUN MINUS2 (A B) (MINUS A B))
	$

	Then the output follows as show below:

	> (DEFUN . (MINUS2 . ((A . (B . NIL)) . ((MINUS . (A . (B . NIL))) . NIL)))

3.	end the code by '$$'

	$$
	> bye!!
