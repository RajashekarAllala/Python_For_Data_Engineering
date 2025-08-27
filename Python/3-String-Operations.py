# Different String Operations

# Accessing string characters using an index value
my_string = "Hello, World!"
first_char = my_string[0]  # 'H'
print(f"First character: {first_char}")

# String length
string_length = len(my_string)  # 13
print(f"String length: {string_length}")

# Looping Through a String
for x in my_string:
    print(x, end=' ')

# Check if a substring exists within a string
substring = "World"
if substring in my_string:
    print(f"\n'{substring}' found in '{my_string}'")
else:
    print(f"\n'{substring}' not found in '{my_string}'")

# Alternatively, using the find() method
position = my_string.find(substring)
if position != -1:
    print(f"'{substring}' found at position {position}")
else:
    print(f"'{substring}' not found in '{my_string}'")

# Using in operator with if statement
if "Hello" in my_string:
    print("'Hello' is present in the string")
else:
    print("'Hello' is not present in the string")

# using not in operator with if statement
if "Python" not in my_string:
    print("'Python' is not present in the string")
else:
    print("'Python' is present in the string")

# String Slicing with start and end indexes
sliced_string = my_string[0:5]  # 'Hello'
print(f"Sliced string: {sliced_string}")

# Slicing from the beginning
sliced_string = my_string[:5]  # 'Hello'
print(f"Sliced string: {sliced_string}")

# Slicing to the end
sliced_string = my_string[7:]  # 'World!'
print(f"Sliced string: {sliced_string}")

# Slicing with step value
sliced_string = my_string[::2]  # 'Hlo ol!'
print(f"Sliced string with step: {sliced_string}")

# Slicing with step value with start and end indexes
sliced_string = my_string[0:13:2]  # 'Hlo ol!
print(f"Sliced string with start, end and step: {sliced_string}")

# Negative Indexing
last_char = my_string[-6]  # 'W'
print(f"Character using negative indexing: {last_char}")

# Negative Indexing with slicing
sliced_string = my_string[-6:-1]  # 'World'
print(f"Sliced string using negative indexing: {sliced_string}")

# Negative Indexing with slicing and step value
sliced_string = my_string[-1:-14:-2]  # '!lo olH'
print(f"Sliced string using negative indexing and step: {sliced_string}")

# Reversing a string using slicing
reversed_string = my_string[::-1]  # '!dlroW ,olleH'
print(f"Reversed string: {reversed_string}")

# String Methods

# Convert string to uppercase
upper_string = my_string.upper()  # 'HELLO, WORLD!'
print(f"Uppercase string: {upper_string}")

# Convert string to lowercase
lower_string = my_string.lower()  # 'hello, world!'
print(f"Lowercase string: {lower_string}")

# Remove whitespace from the beginning and end of the string
sample_string = "   Hello, Python!   "
stripped_string = sample_string.strip()  # 'Hello, World!'
print(f"Stripped string: {stripped_string}")

# Replace a substring with another substring
replaced_string = my_string.replace("World", "Python")  # 'Hello, Python!'
print(f"Replaced string: {replaced_string}")

# Split a string into a list of substrings based on a delimiter
split_string = my_string.split(", ")  # ['Hello', 'World!']
print(f"Split string: {split_string}")

first_string = "I Love"
second_string = "Python"

# Capitalize the first letter of each word in a string
capitalized_string = first_string.title()  # 'I Love'
print(f"Capitalized string: {capitalized_string}")

# Concatenate two strings
concatenated_string = first_string + " " + second_string  # 'I Love Python'
print(f"Concatenated string: {concatenated_string}")

# casefold() method for case-insensitive comparison
casefolded_string1 = "Hello".casefold()
casefolded_string2 = "hello".casefold()
if casefolded_string1 == casefolded_string2:
    print("The strings are equal (case-insensitive comparison)")
else:
    print("The strings are not equal (case-insensitive comparison)")

# center() method to center align a string
centered_string = "Hello".center(20)  # '       Hello        '
print(f"Centered string: {centered_string}")
centered_string = "Hello".center(20, '*')  # '*******Hello********'
print(f"Centered string: {centered_string}")

# count() method to count occurrences of a substring
string1 = "I Love my country. My country is great!"
count_substring = string1.count("country")  # 2
print(f"Count of 'country': {count_substring}")

# endswith() method to check if a string ends with a specific substring
ends_with = string1.endswith("@")  # True
print(f"Ends with '@': {ends_with}")

# startswith() method to check if a string starts with a specific substring
starts_with = string1.startswith("I")  # True
print(f"Starts with 'I': {starts_with}")

# find() method to find the position of a substring
position = string1.find("country")  # 10
print(f"Position of 'country': {position}")

# index() method to find the position of a substring (raises an error if not found) 
try:
    position = string1.index("country")  # 10
    print(f"Position of 'country': {position}")
except ValueError:
    print("'country' not found in the string")

# print repeated words in a string
words = string1.split()
repeated_words = set()
for word in words:
    word_count = string1.count(word)
    if word_count > 1:
        repeated_words.add(word)
print(f"Repeated words: {repeated_words}")

# encode() method to encode a string
encoded_string = my_string.encode("utf-8")  # b'Hello, World!'
print(f"Encoded string: {encoded_string}")

# decode() method to decode a byte object
decoded_string = encoded_string.decode("utf-8")  # 'Hello, World!'
print(f"Decoded string: {decoded_string}")

# expandtabs() method to replace tab characters with spaces
tabbed_string = "Hello\tWorld".expandtabs(4)  # 'Hello   World'
print(f"String with expanded tabs: {tabbed_string}")

# format() method to format a string
formatted_string = "Hello, {}. Welcome to {}.".format("Alice", "Python")  # 'Hello, Alice. Welcome to Python.'
print(f"Formatted string: {formatted_string}")

# f-string for string formatting (Python 3.6+)
name = "Bob"
language = "Java"
f_string = f"Hello, {name}. Welcome to {language}."  # 'Hello, Bob. Welcome to Java.'
print(f"F-string: {f_string}")

# String Formatting Types

# Using :< to left align
left_aligned = "{:<10}".format("Hello")  # 'Hello     '
print(f"Left aligned: '{left_aligned}'")

# Using :> to right align
right_aligned = "{:>10}".format("Hello")  # '     Hello'
print(f"Right aligned: '{right_aligned}'")

# Using :^ to center align
center_aligned = "{:^10}".format("Hello")  # '  Hello   '
print(f"Centered aligned: '{center_aligned}'")

# Using := to pad with zeros
zero_padded = "{:0>10}".format("123")  # '0000000123'
print(f"Zero-padded: '{zero_padded}'")

# Using := to keep the string to left most position
left_most = "{:=<10}".format("Hello")  # 'Hello-----'
print(f"Left most: '{left_most}'")

# Using := to keep the string to right most position
right_most = "{:=>10}".format("Hello")  # '-----Hello'
print(f"Right most: '{right_most}'")

# Using := to keep the string to center position
center_most = "{:=^10}".format("Hello")  # '==Hello==='
print(f"Center most: '{center_most}'")

# Using :+ to show the sign of a number
signed_number = "{:+}".format(42)  # '+42'
print(f"Positive signed number: '{signed_number}'")

# Using :- to show the sign of a negative number
negative_signed_number = "{:-}".format(-42)  # '-42'
print(f"Negative signed number: '{negative_signed_number}'")

# Using : space to show a space for positive numbers
space_signed_number = "{: }".format(42)  # ' 42'
print(f"Space signed number: '{space_signed_number}'")

# Using :, to format a number with commas
number_with_commas = "{:,}".format(1000000)  # '1,000,000'
print(f"Number with commas: '{number_with_commas}'")

# Using :_ to format a number with underscores
number_with_underscores = "{:_}".format(1000000)  # '1_000_000'
print(f"Number with underscores: '{number_with_underscores}'")

# Using :b to format a number as binary
binary_format = "{:b}".format(10)  # '1010'
print(f"Binary format: '{binary_format}'")

# :c to format a number as its corresponding Unicode character
unicode_character = "{:c}".format(65)  # 'A'
print(f"Unicode character: '{unicode_character}'")

# Using :d to format a number as decimal
decimal_format = "{:d}".format(42)  # '42'
print(f"Decimal format: '{decimal_format}'")

# Using :e to format a number in scientific notation
scientific_notation = "{:e}".format(1000000)  # '1.000000e+06'
print(f"Scientific notation: '{scientific_notation}'")

# Using :E to format a number in scientific notation with uppercase
scientific_notation_upper = "{:E}".format(1000000)  # '1.000000E+06'
print(f"Scientific notation (uppercase): '{scientific_notation_upper}'")

# Using :f to format a number as fixed-point
fixed_point = "{:f}".format(3.14159)  # '3.141590'
print(f"Fixed-point format: '{fixed_point}'")

# Using :F to format a number as fixed-point with uppercase
fixed_point_upper = "{:F}".format(3.14159)  # '3.141590'
print(f"Fixed-point format (uppercase): '{fixed_point_upper}'")

# Using :g to format a number in general format
general_format = "{:g}".format(1000000)  # '1000000'
print(f"General format: '{general_format}'")

# Using :G to format a number in general format with uppercase
general_format_upper = "{:G}".format(1000000)  # '1000000'
print(f"General format (uppercase): '{general_format_upper}'")

# Using :o to format a number as octal
octal_format = "{:o}".format(10)  # '12'
print(f"Octal format: '{octal_format}'")

# Using :x to format a number as hexadecimal
hexadecimal_format = "{:x}".format(255)  # 'ff'
print(f"Hexadecimal format: '{hexadecimal_format}'")

# Using :X to format a number as hexadecimal with uppercase
hexadecimal_format_upper = "{:X}".format(255)  # 'FF'
print(f"Hexadecimal format (uppercase): '{hexadecimal_format_upper}'")

# Using :n to format a number according to the current locale
import locale   
locale.setlocale(locale.LC_ALL, '')  # Set to the user's default locale
locale_formatted_number = "{:n}".format(1000000)  # '1,000,000' or '1.000.000' based on locale
print(f"Locale formatted number: '{locale_formatted_number}'")

# Using :% to format a number as percentage
percentage_format = "{:.2%}".format(0.75)  # '75.00%'
print(f"Percentage format: '{percentage_format}'")

# Using :. to specify the number of decimal places
decimal_places = "{:.2f}".format(3.14159)  # '3.14'
decimal_places = "{:.3f}".format(3.14159)  # '3.142'
print(f"Decimal places: '{decimal_places}'")

# Using :* to pad with a specific character
padded_string = "{:*^10}".format("Hi")  # '****Hi****'
print(f"Padded string: '{padded_string}'")

# Using :{} to include curly braces in the formatted string
curly_braces = "This is a curly brace: {{}}".format()  #
print(f"Curly braces: '{curly_braces}'")

# Using : to format multiple values
multiple_values = "Name: {}, Age: {}, Country: {}".format("Alice", 30, "USA")  # 'Name: Alice, Age: 30, Country: USA'
print(f"Multiple values: '{multiple_values}'")

# Using : to format with positional and keyword arguments
positional_keyword = "Name: {0}, Age: {1}, Country: {country}".format("Bob", 25, country="Canada")  # 'Name: Bob, Age: 25, Country: Canada'
print(f"Positional and keyword arguments: '{positional_keyword}'")

# Using : to format with nested fields
nested_fields = "Coordinates: ({point[0]}, {point[1]})".format(point=(10, 20))  # 'Coordinates: (10, 20)'
print(f"Nested fields: '{nested_fields}'")

# Using : to format with alignment and width
alignment_width = "|{:<10}|{:^10}|{:>10}|".format("Left", "Center", "Right")  # '|Left      |  Center  |     Right|'
print(f"Alignment and width: '{alignment_width}'")

# Using format_map() method to format using a dictionary
data = {'name': 'Charlie', 'age': 28, 'country': 'UK'}
formatted_map = "Name: {name}, Age: {age}, Country: {country}".format_map(data)  # 'Name: Charlie, Age: 28, Country: UK'
print(f"Formatted using format_map: '{formatted_map}'")

# isalpha() method to check if all characters in the string are alphabetic
alpha_check = "Hello".isalpha()  # True
print(f"Is alphabetic: {alpha_check}")

# isdigit() method to check if all characters in the string are digits
digit_check = "12345".isdigit()  # True
print(f"Is digit: {digit_check}")

# isalnum() method to check if all characters in the string are alphanumeric
alnum_check = "Hello123".isalnum()  # True
print(f"Is alphanumeric: {alnum_check}")

# isascii() method to check if all characters in the string are ASCII
ascii_check = "Hello".isascii()  # True
print(f"Is ASCII: {ascii_check}")

# isdecimal() method to check if all characters in the string are decimal
decimal_check = "12345".isdecimal()  # True
print(f"Is decimal: {decimal_check}")

# isidentifier() method to check if the string is a valid identifier
identifier_check = "variable_name".isidentifier()  # True
print(f"Is identifier: {identifier_check}")

# isnumeric() method to check if all characters in the string are numeric
numeric_check = "12345".isnumeric()  # True
print(f"Is numeric: {numeric_check}")

# islower() method to check if all characters in the string are lowercase
lower_check = "hello".islower()  # True
print(f"Is lowercase: {lower_check}")

# isupper() method to check if all characters in the string are uppercase
upper_check = "HELLO".isupper()  # True
print(f"Is uppercase: {upper_check}")

# isspace() method to check if all characters in the string are whitespace
space_check = "   ".isspace()  # True
print(f"Is whitespace: {space_check}")

# istitle() method to check if the string is in title case
title_check = "Hello World".istitle()  # True
print(f"Is title case: {title_check}")

# isprintable() method to check if all characters in the string are printable
printable_check = "Hello\nWorld".isprintable()  # False
print(f"Is printable: {printable_check}")

# The output is False for the following reason:
# The string contains a newline character which is not printable.
# If we use a string without special characters, it would return True.
# For example:
# printable_check = "Hello World".isprintable()  # True
# print(f"Is printable: {printable_check}")
# Here, we keep the original example to demonstrate the method.

# join() method to join elements of an iterable into a single string
iterable = ['Hello', 'World', 'from', 'Python']
joined_string = ' '.join(iterable)  # 'Hello World from Python'
print(f"Joined string: {joined_string}")

# ljust() method to left align a string with padding
left_justified = "Hello".ljust(10, '-')  # 'Hello-----
print(f"Left justified: '{left_justified}'")

# rjust() method to right align a string with padding
right_justified = "Hello".rjust(10, '-')  # '-----Hello
print(f"Right justified: '{right_justified}'")

# lower() method to convert a string to lowercase
lowercase_string = "HELLO".lower()  # 'hello'
print(f"Lowercase string: {lowercase_string}")

# lstrip() method to remove leading whitespace
leading_stripped = "   Hello   ".lstrip()  # 'Hello   '
print(f"Leading whitespace removed: '{leading_stripped}'")

# maketrans() method to create a translation table
translation_table = str.maketrans("Helo", "Jxyz")
translated_string = "Hello, World!".translate(translation_table)  # 'Jxyyz, Wxrzd!'
print(f"Translated string: {translated_string}")

# Explaination of the output:
# The maketrans() method creates a mapping where 'H' is replaced with 'J',
# 'e' with 'x', 'l' with 'y', and 'o' with 'z'.
# The translate() method then applies this mapping to the original string.

# partition() method to split a string into three parts
partitioned_string = "Hello, World!".partition(", ")  # ('Hello', ', ', 'World!')
print(f"Partitioned string: {partitioned_string}")

# rpartition() method to split a string into three parts from the right
rpartitioned_string = "Hello, World, from Python".rpartition(", ")  # ('Hello, World', ', ', 'from Python')
print(f"Right partitioned string: {rpartitioned_string}")

# replace() method to replace occurrences of a substring
replaced_string = "Hello, World!".replace("World", "Python")  # 'Hello, Python!'
print(f"Replaced string: {replaced_string}")

# rfind() method to find the last occurrence of a substring
last_position = "Hello, World! Welcome to the World!".rfind("World")  # 26
print(f"Last position of 'World': {last_position}")

# rindex() method to find the last occurrence of a substring (raises an error if not found)
try:
    last_position = "Hello, World! Welcome to the World!".rindex("World")  # 26
    print(f"Last position of 'World': {last_position}")
except ValueError:
    print("'World' not found in the string")

# rjust() method to right align a string with padding
right_justified = "Hello".rjust(10, '-')  # '-----Hello'
print(f"Right justified: '{right_justified}'")

# rstrip() method to remove trailing whitespace 
trailing_stripped = "   Hello   ".rstrip()  # '   Hello'
print(f"Trailing whitespace removed: '{trailing_stripped}'")

# rsplit() method to split a string from the right
rsplit_string = "one,two,three,four".rsplit(",", 2)
print(f"Right split string: {rsplit_string}")  # ['one,two', 'three', 'four']

# splitlines() method to split a string at line breaks
multiline_string = "Hello\nWorld\nfrom\nPython"
split_lines = multiline_string.splitlines()  # ['Hello', 'World', 'from', 'Python']
print(f"Split lines: {split_lines}")

# swapcase() method to swap the case of each character in the string
swapped_case = "Hello World".swapcase()  # 'hELLO wORLD
print(f"Swapped case: {swapped_case}")

# title() method to convert the first character of each word to uppercase
title_case = "hello world from python".title()  # 'Hello World From Python'
print(f"Title case: {title_case}")  

# zfill() method to pad a string with zeros on the left
zero_filled = "42".zfill(5)  # '00042'
print(f"Zero filled: '{zero_filled}'")

# String Comparison
string_a = "apple"
string_b = "banana"
if string_a == string_b:
    print(f"'{string_a}' is equal to '{string_b}'")
elif string_a < string_b:
    print(f"'{string_a}' is less than '{string_b}'")
else:
    print(f"'{string_a}' is greater than '{string_b}'") 
# Output: 'apple' is less than 'banana'
# Explanation: In Python, string comparison is done lexicographically using the Unicode values of characters.
# Unicode value of 'a' is 97 and 'b' is 98, hence 'apple' is less than 'banana'.
# Note: String comparison is case-sensitive. For example, 'Apple' is greater than 'apple' because the Unicode value of 'A' (65) is less than 'a' (97).
# To perform a case-insensitive comparison, you can convert both strings to the same case using lower() or upper() methods before comparing.
# Case-insensitive string comparison
string_c = "Apple"
string_d = "apple"
if string_c.lower() == string_d.lower():
    print(f"'{string_c}' is equal to '{string_d}' (case-insensitive comparison)")
else:
    print(f"'{string_c}' is not equal to '{string_d}' (case-insensitive comparison)")
# Output: 'Apple' is equal to 'apple' (case-insensitive comparison)

