print("Welcome to the Python Knowledge Quiz!")
print("You will be asked 5 questions. Each correct answer earns 1 point.\n")

score = 0

# Question 1
answer = input("1. What keyword is used to define a function in Python?\nA) func\nB) define\nC) def\nYour answer: ").strip().lower()
if answer == 'c' or answer == 'def':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'def'.\n")

# Question 2
answer = input("2. What data type is used to store True or False values?\nA) integer\nB) boolean\nC) string\nYour answer: ").strip().lower()
if answer == 'b' or answer == 'boolean':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'bool'.\n")

# Question 3
answer = input("3. Which symbol is used for comments in Python?\nA) //\nB) <!-- -->\nC) #\nYour answer: ").strip().lower()
if answer == 'c' or answer == '#':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is '#'.\n")

# Question 4
answer = input("4. How do you create a variable with the value 5?\nA) x == 5\nB) x = 5\nC) int x = 5\nYour answer: ").strip().lower()
if answer == 'b' or answer == 'x = 5':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'x = 5'.\n")

# Question 5
answer = input("5. What function do you use to display output in Python?\nA) output()\nB) print()\nC) echo()\nYour answer: ").strip().lower()
if answer == 'b' or answer == 'print()':
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is 'print()'.\n")

# Final score
print(f"Your final score is {score} out of 5.")

if score == 5:
    print("Excellent job!")
elif score >= 3:
    print("Good work, keep practicing!")
else:
    print("Keep studying, you'll get there!")
