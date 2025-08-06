#tema 2
from pydantic_core.core_schema import no_info_before_validator_function

a=3
b1=3.14
b=a
print(a)
print(b)
print(b1)
c=b*2
print(c)

def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
is_leap_year(2010)
is_leap_year(2000)
is_leap_year(2001)
is_leap_year(2002)
is_leap_year(2003)
is_leap_year(2001)
is_leap_year(2004)

def is_ternary(n: int) -> bool:
    if n < 0:
        return False
    while n > 0:
        if n % 3 != 0 and n % 3 != 1:
            return False
        n //= 3
    return True


x = 100
y = -30
z = 0

# Type conversions
print("int to float:", float(x))
print("float to int:", int(3.99))
print("int to bool:", bool(x), bool(z))

#tema 3

nmbrs = [10, 20, 30, 40, 50]

print("List of numbers:", nmbrs)
print("First element:", nmbrs[0])
print("Last element:", nmbrs[-1])
print("Slice from index 1 to 3:", nmbrs[1:4])
print("Slice from index 2 to end:", nmbrs[2:])
print("Slice from start to index 3:", nmbrs[:4])
print("Reversed list:", nmbrs[::-1])

nmbrs.append(30)
print("List after appending 30:", nmbrs)
nmbrs.insert(2, 25)
print("List after inserting 25 at index 2:", nmbrs)
nmbrs.remove(20)
print("List after removing 20:", nmbrs)
nmbrs.pop(3)
print("List after popping element at index 3:", nmbrs)
nmbrs.sort()

# Change a specific word in a sentence (without replace())
def change_word(sentence: str, old_word: str, new_word: str) -> str:
    words = sentence.split()
    for i in range(len(words)):
        if words[i] == old_word:
            words[i] = new_word
            break  # Change only the first occurrence
    return ' '.join(words)

sentence = "I love programming in Python"
new_sentence = change_word(sentence, "Python", "Java")
print("Original sentence:", sentence)
print("Modified sentence:", new_sentence)

#palindrom chcecker
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Madam"))
print(is_palindrome("ANNA"))
print(is_palindrome("Hello"))


#  f-string Formatting
def format_person(name: str, age: int) -> str:
    return f"My name is {name} and I am {age} years old."
print(format_person("Alice", 30))

# TEMA4
data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]

for amount, currency, target_currency, rate in data:
    converted = amount * rate
    print(f"{amount} {currency} = {converted:.2f} {target_currency}")

s=0
for i in range(1, 11):
    s += i
print("Sum of numbers from 1 to 10:", s)

#Number Guessing Game (using while loop) function
import random
def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")


fruits = ['apple', 'banana', 'cherry', 'date']

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit} ({len(fruit)} letters)")


#tema 5

def invert_dict_with_duplicates(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = []
        inverted_dict[value].append(key)
    return inverted_dict
original_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}
inverted_dict = invert_dict_with_duplicates(original_dict)
print("Original dictionary:", original_dict)
print("Inverted dictionary with duplicates:", inverted_dict)

testing = {"Ana", "Bob", "Charlie", "Diana"}
development = {"Charlie", "Eve", "Frank", "Ana"}
devops = {"George", "Ana", "Bob", "Eve"}

all_three = testing & development & devops
print(all_three)  # {'Ana'}

just_one = (testing | development | devops)
print(just_one)

are_all_testing_in_devops = testing.issubset(devops)
print(are_all_testing_in_devops)

squares = [x**2 for x in range(1, 11)]
print(squares)

div_by_7 = {x for x in range(1, 51) if x % 7 == 0}
print(div_by_7)


def c_style_calculator(expr):
    try:
        # Încercăm să evaluăm expresia (folosim eval într-un mod controlat)
        allowed_chars = set("0123456789+-*/.() ")
        if not all(char in allowed_chars for char in expr):
            return "❌ Eroare: Caracter interzis în expresie."

        result = eval(expr)
        return result

    except ZeroDivisionError:
        return "div 0"
    except SyntaxError:
        return "invalida"


print(c_style_calculator("3 + 5 * 2+2+2+2+2+2"))       # 13
print(c_style_calculator("10 / 0"))          # Eroare împărțire
print(c_style_calculator("10 +"))            # Eroare sintaxă
print(c_style_calculator("5 + 3 / (2 - 2)"))  # Împărțire la zero
print(c_style_calculator("__import__('os')"))# Caracter interzis


names = ["Lucas", "Nataly", "Megi", "Maria", "Steven"]
scores = [85, 92, 78, 81, 67]
students = list(zip(names, scores))

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
filtered_students = [student for student in sorted_students if student[1] >= 80]

for name, score in sorted_students:
    print(f"{name}: {score}")
print("\nFiltered students with scores >= 80:")
for name, score in filtered_students:
    print(f"{name}: {score}")



def check_age(age_input):
    try:
        # Verificare input gol
        if age_input.strip() == "":
            raise ValueError("⚠️ Nu ai introdus nicio valoare pentru vârstă.")

        # Conversie la int
        age = int(age_input)

        # Verificare limită
        if age < 0 or age > 120:
            raise ValueError("⚠️ Vârsta trebuie să fie între 0 și 120.")

        print(f"✅ Vârsta introdusă este validă: {age} ani")

    except ValueError as ve:
        print(f"❌ Eroare de validare: {ve}")

    except Exception as e:
        print(f"❌ Eroare neașteptată: {e}")

    finally:
        print("🔍 Validation complete\n")

# Test cases
test_cases = [
    "25",
    "  ",
    "150",
    "-5",
    "30",
    "abc",
    "120",
    "0",
    "120.5",
    "100"]
for test in test_cases:
    print(f"Test case: '{test}'")
    check_age(test)
    print("-" * 30)  # Separator for readability

#tema 7
def write_students_file(filename, students):
    with open(filename, 'w') as f:
        for student in students:
            f.write(student + '\n')

def filter_students_starting_with_vowel(input_file, output_file):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            name = line.strip()
            if name and name[0].upper() in vowels:
                outfile.write(name + '\n')
students = ["Alice", "Bob", "Eve", "Oscar", "Charlie", "Uma", "Greg"]
write_students_file('students.txt', students)
filter_students_starting_with_vowel('students.txt', 'filtered.txt')



def write_log_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def reverse_file_lines(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    with open(output_file, 'w') as outfile:
        for line in reversed(lines):
            outfile.write(line)

log_lines = [
    "2023-10-01 12:00:00 - INFO - Application started",
    "2023-10-01 12:05:00 - INFO - User logged in",
    "2023-10-01 12:10:00 - ERROR - An error occurred",
    "2023-10-01 12:15:00 - INFO - Application stopped"
]
write_log_file('log.txt', log_lines)
reverse_file_lines('log.txt', 'reversed_log.txt')
def read_and_print_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"❌ Eroare: Fișierul '{filename}' nu a fost găsit.")

read_and_print_file('reversed_log.txt')