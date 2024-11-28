# Functions to be implemented
import string as st

def find_minimum(numbers):
    """Returns the smallest number in a list. Return None for an empty list."""
    return min(numbers) if numbers else None

def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer iteratively."""
    x = 1
    for i in range(1,n+1):
        x *= i
    return x

def unique_elements(items):
    """Returns a list of unique elements, maintaining their order."""
    return sorted(list(set(items)))

def check_palindrome(string):
    """Returns True if the input string is a palindrome, False otherwise."""
    string = string.replace(" ","")
    reversed_word = string[::-1]
    return string.lower() == reversed_word.lower()



def fibonacci_sequence(n):
    """Returns the first `n` numbers in the Fibonacci sequence."""
    a = 0
    b = 1
    list1 = [a,b]
    for _ in range(n):
        c = a + b
        list1.append(c)
        a = b
        b = c
    return list1[:n]



def find_max(numbers):
    """Returns the largest number in a list. Return None for an empty list."""
    return max(numbers)

def find_min(numbers):
    """Returns the smallest number in a list. Return None for an empty list."""
    return min(numbers)

def find_average(numbers):
    """Returns the average of a list of numbers. Return None for an empty list."""
    return sum(numbers)/len(numbers)

def find_even_numbers(numbers):
    """Returns a list of even numbers in a list."""
    even = tuple(filter(lambda x:x % 2 == 0,numbers))
    return even

def find_odd_numbers(numbers):
    odd = list(filter(lambda x:x % 2 != 0,numbers))
    return tuple(odd)

def find_number_of_even_numbers(numbers):
    """Returns the number of even numbers in a list."""
    return len(find_even_numbers(numbers))

def find_number_of_odd_numbers(numbers):
    """Returns the number of odd numbers in a list."""

    return  len(find_odd_numbers(numbers))

def return_list_stats(numbers):
    """Returns a dictionary with the minimum, maximum, average, and number of elements in a list."""
    stats = {
        "unique_numbers": set(numbers),
        "min": find_minimum(numbers),
        "max": find_max(numbers),
        "average": round(find_average(numbers),1),
        "even_numbers": tuple(sorted(list(find_even_numbers(numbers)))),
        "odd_numbers": tuple(sorted(list(find_odd_numbers(numbers)))),
        "number_of_even_numbers": find_number_of_even_numbers(numbers),
        "number_of_odd_numbers": find_number_of_odd_numbers(numbers)
    }
    return stats

def process_characters(string):
    """Returns a dictionary with the number of letters, digits, and special characters in a string."""
    list_of_nums = []
    list_of_chars = []
    for i in string:

        if i.isnumeric():
            list_of_nums.append(int(i))

        elif i.isalpha():
            list_of_chars.append(i)

    return sorted(list(set(list_of_chars))),sorted(list(set(list_of_nums)))

def generate_squared_dict(n):
    """Generates a dictionary with the square of numbers from 1 to n."""
    dict = {}
    if n >= 0:
        for i in range(1,n+1):
            dict[i] = i**2
    else:
        for i in range(n,0):
            dict[i] = i**2

    return dict
def convert_to_word_list(string):
    """Converts a string to a list of words."""
    return list(map(lambda x: x.strip("!:?,.'\""), string.lower().split()))

def letters_count_map(string):
    """Returns a dictionary with the count of each letter in a string."""
    string = string.lower()
    dict = {}

    for i in st.ascii_lowercase:
        dict[i] = list(string).count(i)

    return dict



def text_to_morse(text):
    """Converts text to Morse code."""
    morse_code = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----.","0": "-----"," ": " ","!": "-.-.--","\"": ".-..-.","$": "...-..-","&": ".-...","'": ".----.","(": "-.--.",")": "-.--.-","*": "-..-","+": ".-.-.","-": "-....-",".": ".-.-.-","/": "-..-.",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.","_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-",
        "?": "..--..","@": ".--.-.","_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.","_": "..--.-",
        ",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.","_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.",
        "_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.",
        "_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.",
        "_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.",
        "_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..",
        "@": ".--.-.","_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.","_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.","_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.","_": "..--.-",",": "--..--",":": "---...",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.","_": "..--.-",",": "--..--",":": "---...",}
    text = list(text.upper())
    newtext = ""
    for i in text:
        if text.index(i) == 0:
            newtext += morse_code[i]
        else:
            newtext+= f" {morse_code[i]}"

    return newtext


