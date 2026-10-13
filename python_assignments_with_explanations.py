"""
PYTHON PROGRAMMING ASSIGNMENTS WITH EXPLANATIONS
Level: Beginner to Intermediate

How to use:
1. Run this file with: python python_assignments_with_explanations.py
2. Select an assignment from the menu.
3. Read the comments to understand the code.
"""

# ASSIGNMENT 1: Print a message
def assignment_1():
    name = "Vilas"
    print("My name is", name)
    print("Welcome to Python programming!")

# Explanation:
# Variables store values. print() displays values in the terminal.


# ASSIGNMENT 2: Add two numbers
def assignment_2():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    total = first_number + second_number
    print("Sum:", total)

# Explanation:
# input() reads text. float() converts it to a number.
# The + operator adds the two numbers.


# ASSIGNMENT 3: Check even or odd
def assignment_3():
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

# Explanation:
# % returns the remainder. Even numbers have remainder zero when divided by 2.


# ASSIGNMENT 4: Find the largest of three numbers
def assignment_4():
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    c = float(input("Enter number 3: "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number:", largest)

# Explanation:
# if and elif check conditions. and requires both conditions to be true.


# ASSIGNMENT 5: Multiplication table
def assignment_5():
    number = int(input("Enter a number: "))
    for multiplier in range(1, 11):
        print(number, "x", multiplier, "=", number * multiplier)

# Explanation:
# range(1, 11) produces numbers from 1 to 10. The for loop repeats the code.


# ASSIGNMENT 6: Sum from 1 to N
def assignment_6():
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("Please enter a positive integer.")
        return

    total = 0
    for number in range(1, n + 1):
        total += number

    print("Sum:", total)

# Explanation:
# total += number adds number to the existing total.
# The range endpoint is excluded, so n + 1 includes n.


# ASSIGNMENT 7: Factorial
def assignment_7():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative integers.")
        return

    factorial = 1
    for number in range(1, n + 1):
        factorial *= number

    print("Factorial:", factorial)

# Explanation:
# The loop multiplies the numbers from 1 through n.
# The factorial of 0 is 1, which this code handles correctly.


# ASSIGNMENT 8: Reverse a string
def assignment_8():
    text = input("Enter text: ")
    print("Reversed text:", text[::-1])

# Explanation:
# The slice step -1 reads a string from its last character to its first.


# ASSIGNMENT 9: Count vowels
def assignment_9():
    text = input("Enter text: ").lower()
    vowels = "aeiou"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    print("Number of vowels:", count)

# Explanation:
# lower() handles uppercase vowels. The loop checks each character.


# ASSIGNMENT 10: List statistics
def assignment_10():
    numbers = [12, 7, 25, 4, 18]
    total = sum(numbers)
    print("Numbers:", numbers)
    print("Sum:", total)
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
    print("Average:", total / len(numbers))

# Explanation:
# sum(), min(), max(), and len() calculate common list statistics.


# ASSIGNMENT 11: Remove duplicates while preserving order
def assignment_11():
    numbers = [2, 4, 2, 7, 4, 9, 7]
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    print("Original list:", numbers)
    print("Without duplicates:", unique_numbers)

# Explanation:
# append() adds an item. The membership check prevents duplicates.


# ASSIGNMENT 12: Count word frequency
def assignment_12():
    sentence = input("Enter a sentence: ").lower()
    words = sentence.split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    for word, count in frequency.items():
        print(word, ":", count)

# Explanation:
# split() separates words. A dictionary stores each word and its count.
# get(word, 0) returns zero when the word is not already present.


# ASSIGNMENT 13: Prime number checker
def assignment_13():
    number = int(input("Enter an integer: "))

    if number < 2:
        print("Not a prime number")
        return

    divisor = 2
    is_prime = True

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    print("Prime number" if is_prime else "Not a prime number")

# Explanation:
# A prime number is greater than 1 and has no divisors other than 1 and itself.
# Testing divisors up to the square root is sufficient.


# ASSIGNMENT 14: Write and call a function
def square(number):
    return number * number


def assignment_14():
    value = float(input("Enter a number: "))
    print("Square:", square(value))

# Explanation:
# def defines a function. return sends a result back to the caller.


# ASSIGNMENT 15: Exception handling
def assignment_15():
    user_text = input("Enter an integer: ")
    try:
        number = int(user_text)
        print("You entered:", number)
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Explanation:
# int() raises ValueError for unsuitable text. except handles that error.


# ASSIGNMENT 16: Student marks using a dictionary
def assignment_16():
    marks = {
        "Python": 82,
        "SQL": 76,
        "Statistics": 88,
        "Machine Learning": 91,
    }

    for subject, score in marks.items():
        print(subject, ":", score)

    average = sum(marks.values()) / len(marks)
    print("Average marks:", round(average, 2))
    print("Result:", "Pass" if average >= 40 else "Fail")

# Explanation:
# items() provides key-value pairs; values() provides the marks.
# round() rounds the average to two decimal places.


# ASSIGNMENT 17: Write and read a text file
def assignment_17():
    file_name = "practice_notes.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Python file handling practice.\n")
        file.write("Text files store information for later use.\n")

    with open(file_name, "r", encoding="utf-8") as file:
        contents = file.read()

    print(contents)

# Explanation:
# "w" opens a file for writing and replaces existing contents.
# "r" opens it for reading. with closes the file automatically.


# ASSIGNMENT 18: Class and object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student name:", self.name)
        print("Marks:", self.marks)


def assignment_18():
    student = Student("Amit", 85)
    student.display()

# Explanation:
# A class describes an object. __init__ sets its attributes.
# self refers to the current object; display() is an instance method.


# ASSIGNMENT 19: Find common list elements
def assignment_19():
    first = [1, 2, 3, 4, 5, 3]
    second = [3, 4, 5, 6, 7]
    common = []

    for value in first:
        if value in second and value not in common:
            common.append(value)

    print("Common elements:", common)

# Explanation:
# in checks membership. The second check avoids duplicate results.


# ASSIGNMENT 20: Mini expense tracker
def assignment_20():
    expenses = []

    while True:
        entry = input("Enter expense amount or type 'done': ").strip()
        if entry.lower() == "done":
            break

        try:
            amount = float(entry)
            if amount < 0:
                print("Expense cannot be negative.")
                continue
            expenses.append(amount)
        except ValueError:
            print("Enter a valid number or 'done'.")

    if not expenses:
        print("No expenses were entered.")
        return

    total = sum(expenses)
    print("Expenses:", expenses)
    print("Total:", round(total, 2))
    print("Average:", round(total / len(expenses), 2))

# Explanation:
# while repeats until break. continue skips to the next iteration.
# The empty-list check prevents division by zero.


ASSIGNMENTS = {
    "1": ("Print a message", assignment_1),
    "2": ("Add two numbers", assignment_2),
    "3": ("Even or odd", assignment_3),
    "4": ("Largest of three numbers", assignment_4),
    "5": ("Multiplication table", assignment_5),
    "6": ("Sum from 1 to N", assignment_6),
    "7": ("Factorial", assignment_7),
    "8": ("Reverse a string", assignment_8),
    "9": ("Count vowels", assignment_9),
    "10": ("List statistics", assignment_10),
    "11": ("Remove duplicates", assignment_11),
    "12": ("Word frequency", assignment_12),
    "13": ("Prime number checker", assignment_13),
    "14": ("Functions and return", assignment_14),
    "15": ("Exception handling", assignment_15),
    "16": ("Student marks", assignment_16),
    "17": ("File handling", assignment_17),
    "18": ("Class and object", assignment_18),
    "19": ("Common list elements", assignment_19),
    "20": ("Mini expense tracker", assignment_20),
}


def main():
    print("\nPYTHON PROGRAMMING ASSIGNMENTS")
    for number, (title, _) in ASSIGNMENTS.items():
        print(f"{number}. {title}")
    print("0. Exit")

    while True:
        choice = input("\nChoose an assignment number: ").strip()
        if choice == "0":
            print("Goodbye!")
            break

        selected = ASSIGNMENTS.get(choice)
        if selected is None:
            print("Invalid choice. Select a number from 0 to 20.")
            continue

        title, function = selected
        print(f"\n--- {title} ---")
        function()


if __name__ == "__main__":
    main()
