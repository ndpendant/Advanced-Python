Collatz Assignment

Python Features Required: Basic python, print, user defined functions, exceptions

File(s) to Submit: collatz.py

Specification: Write the code for the functions collatz and collatz_sequence described below. Your code should be in the collatz.py file.
The collatz() function has one parameter named number. If number is even, then collatz() prints number//2 and then return this value. If number is odd, then collatz() should print and return 3*number+1.
A collatz sequence with initial value n is the sequence of numbers collatz(n), collatz(collatz(n)), …. In all known cases, the sequence eventually reaches 1 and all subsequent values will be 1. Mathematicians aren’t sure why this is the case (i.e., no one has proved that this will happen). This problem is sometimes called “the simplest impossible math problem".
So, you are to write another function collatz_sequence() that first prompts for and inputs the first term of the sequence using the input() function. Remember to convert the the string returned by the input() function to an integer with the int() conversion function.
The int() function will raise a ValueError exception if it is passed a noninteger string, as in int('puppy'). Your code should include a try-except block that prints "Invalid input: must be an integer" and returns False if the exception occurs.
Otherwise, the function prints the collatz sequence by repeatedly calling collatz() on the previous term in the sequence, printing the values until the function returns the value 1. After printing the 1, the function returns True.
The output of this program could look something like this, where user input is underlined:

Enter number: 3
10
5
16
8
4
2
1
