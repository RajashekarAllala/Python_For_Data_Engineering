# Different String Operations

# Accessing string characters using an index value
# Explaination: In Python, strings are indexed starting from 0.
# So, the first character of the string is at index 0, the second character is at index 1, and so on.
# You can access individual characters of a string using square brackets [] and the index value.
my_string = "Hello, World!"
first_char = my_string[0]  # 'H'
print(f"First character: {first_char}")

# String length
# Explaination: The len() function in Python is used to get the length of a string.
# It returns the number of characters in the string, including spaces and special characters.
string_length = len(my_string)  # 13
print(f"String length: {string_length}")

# Looping Through a String
# Explaination: You can loop through each character in a string using a for loop.
print("Characters in the string:")
for x in my_string:
    print(x, end=' ')

# Check if a substring exists within a string
# Explaination: The in operator is used to check if a substring exists within a string.
# It returns True if the substring is found, and False otherwise.
substring = "World"
if substring in my_string:
    print(f"\n'{substring}' found in '{my_string}'")
else:
    print(f"\n'{substring}' not found in '{my_string}'")

# Alternatively, using the find() method
# Explaination: The find() method returns the lowest index of the substring if it is found in the string.
# If the substring is not found, it returns -1.
# This method is case-sensitive.
position = my_string.find(substring)
if position != -1:
    print(f"'{substring}' found at position {position}")
else:
    print(f"'{substring}' not found in '{my_string}'")

# Using in operator with if statement
# Explaination: The in operator can be used in conditional statements to execute code based on the presence of a substring.
# Here, we check if "Hello" is present in the string.
# If it is, we print a message, otherwise we print another message.
# This is useful for validating input or checking conditions in your code.
if "Hello" in my_string:
    print("'Hello' is present in the string")
else:
    print("'Hello' is not present in the string")

# using not in operator with if statement
# Explaination: The not in operator is used to check if a substring does not exist within a string.
# It returns True if the substring is not found, and False if it is found.
if "Python" not in my_string:
    print("'Python' is not present in the string")
else:
    print("'Python' is present in the string")

# String Slicing with start and end indexes
# Explaination: String slicing allows you to extract a portion of a string by specifying the start and end indexes.
# The syntax for slicing is string[start:end], where start is the index of the first character
# you want to include in the slice and end is the index of the first character you want to exclude from the slice.
# The slice will include characters from the start index up to, but not including, the end index.
# If you omit the start index, it defaults to 0 (the beginning of the string).
# If you omit the end index, it defaults to the length of the string (the end of the string).
# You can also use negative indexes to slice from the end of the string.
# Negative indexes count from the end of the string, with -1 being the last character, -2 being the second to last character, and so on.
# You can also specify a step value to skip characters in the slice.
# The syntax for slicing with a step value is string[start:end:step], where step is the number of characters to skip.
# The step value can be positive or negative. A positive step value slices the string from left to right,
# while a negative step value slices the string from right to left.

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
# Explaination: String methods are built-in functions that perform specific operations on strings.
# They are called using the dot notation, where the method name is followed by parentheses.
# Here are some commonly used string methods:
# upper(), lower(), strip(), replace(), split(), title(), concat(), casefold(), center(), count(), endswith(), startswith(),
# find(), index(), encode(), decode(), expandtabs(), format(), f-string, isalpha(), isdigit(), isalnum(), isascii(), isdecimal(), isidentifier(),
# isnumeric(), islower(), isupper(), isspace(), istitle(), isprintable(), join(), ljust(), rjust(), lstrip(), maketrans(), partition(), rpartition(), rfind(), rindex(),
# rjust(), rstrip(), rsplit(), splitlines(), swapcase(), zfill(), and more.
# Each method performs a specific operation and returns a new string or a value based on the operation.
# Note: String methods do not modify the original string, as strings are immutable in Python.
# Instead, they return a new string with the desired modifications.

# Convert string to uppercase
# Explaination: The upper() method is used to convert all characters in a string to uppercase.
# It returns a new string with all characters in uppercase.
upper_string = my_string.upper()  # 'HELLO, WORLD!'
print(f"Uppercase string: {upper_string}")

# Convert string to lowercase
# Explaination: The lower() method is used to convert all characters in a string to lowercase.
# It returns a new string with all characters in lowercase.
lower_string = my_string.lower()  # 'hello, world!'
print(f"Lowercase string: {lower_string}")

# Remove whitespace from the beginning and end of the string
# Explaination: The strip() method is used to remove whitespace characters from the beginning and end of a string.
# It does not remove whitespace characters from the middle of the string.
# The method returns a new string with the whitespace removed.
# If you want to remove specific characters instead of whitespace, you can pass those characters as an argument to the strip() method.
# For example, to remove leading and trailing asterisks (*) from a string, you can use the following code:
# original_string = "***Hello, World!***"
# stripped_string = original_string.strip("*")  # 'Hello, World!'
# print(stripped_string)
# In this example, the strip("*") method removes all leading and trailing asterisks from the original string.
# If no argument is provided, the strip() method removes all leading and trailing whitespace characters by default.
sample_string = "   Hello, Python!   "
stripped_string = sample_string.strip()  # 'Hello, World!'
print(f"Stripped string: {stripped_string}")

# Replace a substring with another substring
# Explaination: The replace() method is used to replace occurrences of a specified substring with another substring.
# It takes two arguments: the substring to be replaced and the substring to replace it with.
# The method returns a new string with the replacements made.
# If the substring to be replaced is not found in the original string, the method returns the original string unchanged.
# The replace() method is case-sensitive, meaning that it will only replace substrings that match the case of the specified substring.
# You can also specify the maximum number of replacements to be made by providing an optional third argument.
# If the third argument is not provided, all occurrences of the substring will be replaced.
# If the third argument is provided, only the first n occurrences of the substring will be replaced.
# Here is an example:
# original_string = "Hello, World! Welcome to the World!"
# replaced_string = original_string.replace("World", "Python", 1)  #
# print(replaced_string)  # 'Hello, Python! Welcome to the World!'
# In this example, only the first occurrence of "World" is replaced with "Python".
# The second occurrence remains unchanged.
# If you want to replace all occurrences, you can omit the third argument:
# original_string = "Hello, World! Welcome to the World!"
# replaced_string = original_string.replace("World", "Python")  #
# print(replaced_string)  # 'Hello, Python! Welcome to the Python!'
# In this example, all occurrences of "World" are replaced with "Python".
replaced_string = my_string.replace("World", "Python")  # 'Hello, Python!'
print(f"Replaced string: {replaced_string}")

# Split a string into a list of substrings based on a delimiter
# Explaination: The split() method splits a string into a list of substrings based on a delimiter.
# The default delimiter is any whitespace character (space, tab, newline), but you can specify a different delimiter by passing it as an argument to the method.
# The method returns a list of substrings, which can be accessed using indexing or iterated through using a loop.

split_string = my_string.split(", ")  # ['Hello', 'World!']
print(f"Split string: {split_string}")

first_string = "I Love"
second_string = "Python"

# Capitalize the first letter of each word in a string
# Explaination: The title() method is used to convert the first character of each word in a string to uppercase.
# It returns a new string with the first letter of each word capitalized.
# Words are defined as sequences of characters separated by whitespace or punctuation.
# The title() method is useful for formatting titles, headings, or names in a consistent way.
capitalized_string = first_string.title()  # 'I Love'
print(f"Capitalized string: {capitalized_string}")

# capitalize the first letter of the string
# Explaination: The capitalize() method is used to convert the first character of a string to uppercase and the rest of the characters to lowercase.
# It returns a new string with the first letter capitalized and the rest of the letters in lowercase.
# This method is useful for formatting sentences or phrases in a consistent way.
capitalized_string = first_string.capitalize()  # 'I love'
print(f"Capitalized string: {capitalized_string}")

# Concatenate two strings
# Explaination: In Python, you can concatenate (join) two or more strings using the + operator.
# When you use the + operator with strings, it combines them into a single string.
# You can also add a space or any other character between the strings to separate them.
concatenated_string = first_string + " " + second_string  # 'I Love Python'
print(f"Concatenated string: {concatenated_string}")

# casefold() method for case-insensitive comparison
# Explaination: The casefold() method is used to convert a string to lowercase in a way that is suitable for case-insensitive comparisons.
# It is similar to the lower() method, but it is more aggressive in its conversion, as it is designed to handle special cases in different languages.
# The casefold() method is useful when you want to compare two strings without considering their case (uppercase or lowercase).
casefolded_string1 = "Hello".casefold()
casefolded_string2 = "hello".casefold()
if casefolded_string1 == casefolded_string2:
    print("The strings are equal (case-insensitive comparison)")
else:
    print("The strings are not equal (case-insensitive comparison)")

# center() method to center align a string
# Explaination: The center() method is used to center align a string within a specified width.
# It takes two arguments: the width of the resulting string and an optional fill character (default is space).
# The method returns a new string that is centered within the specified width, with the fill character added to both sides if necessary.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
centered_string = "Hello".center(20)  # '       Hello        '
print(f"Centered string: {centered_string}")
centered_string = "Hello".center(20, '*')  # '*******Hello********'
print(f"Centered string: {centered_string}")

# count() method to count occurrences of a substring
# Explaination: The count() method is used to count the number of occurrences of a substring in a string.
# It takes one argument: the substring to be counted.
# The method returns an integer representing the number of times the substring appears in the string.
# The count() method is case-sensitive, meaning that it will only count substrings that match the case of the specified substring.
# You can also specify optional start and end indexes to limit the search to a specific portion of the string.
# If the substring is not found in the string, the method returns 0.
string1 = "I Love my country. My country is great!"
count_substring = string1.count("country")  # 2
print(f"Count of 'country': {count_substring}")

# endswith() method to check if a string ends with a specific substring
# Explaination: The endswith() method is used to check if a string ends with a specific substring.
# It takes one argument: the substring to be checked.
# The method returns True if the string ends with the specified substring, and False otherwise.
# The endswith() method is case-sensitive, meaning that it will only return True if the substring matches the case of the end of the string.
# You can also specify optional start and end indexes to limit the search to a specific portion of the string.
# If the substring is an empty string, the method will always return True, as every string ends with an empty string.
ends_with = string1.endswith("@")  # True
print(f"Ends with '@': {ends_with}")

# startswith() method to check if a string starts with a specific substring
# Explaination: The startswith() method is used to check if a string starts with a specific substring.
# It takes one argument: the substring to be checked.
# The method returns True if the string starts with the specified substring, and False otherwise.
# The startswith() method is case-sensitive, meaning that it will only return True if the substring matches the case of the start of the string.
# You can also specify optional start and end indexes to limit the search to a specific portion of the string.
# If the substring is an empty string, the method will always return True, as every string starts with an empty string.
starts_with = string1.startswith("I")  # True
print(f"Starts with 'I': {starts_with}")

# find() method to find the position of a substring
# Explaination: The find() method is used to find the position of a substring in a string.
# It takes one argument: the substring to be found.
# The method returns the index of the first occurrence of the substring in the string.
# If the substring is not found, the method returns -1.
# The find() method is case-sensitive, meaning that it will only find substrings that match the case of the specified substring.
# You can also specify optional start and end indexes to limit the search to a specific portion of the string.
# If the substring is an empty string, the method will return the index of the first character, which is 0.
position = string1.find("country")  # 10
print(f"Position of 'country': {position}")

# index() method to find the position of a substring (raises an error if not found) 
# Explaination: The index() method is similar to the find() method, but it raises a ValueError if the substring is not found in the string.
# It takes one argument: the substring to be found.
# The method returns the index of the first occurrence of the substring in the string.
# If the substring is not found, the method raises a ValueError.
# The index() method is case-sensitive, meaning that it will only find substrings that match the case of the specified substring.
# You can also specify optional start and end indexes to limit the search to a specific portion of the string.
# If the substring is an empty string, the method will return the index of the first character, which is 0.
try:
    position = string1.index("country")  # 10
    print(f"Position of 'country': {position}")
except ValueError:
    print("'country' not found in the string")

# print repeated words in a string
# Explaination: To find and print repeated words in a string, you can split the string into individual words using the split() method.
# Then, you can use a loop to iterate through the list of words and count the occurrences of each word using the count() method.
# If a word appears more than once, you can add it to a set to avoid duplicates.
# Finally, you can print the set of repeated words.
words = string1.split()
repeated_words = set()
for word in words:
    word_count = string1.count(word)
    if word_count > 1:
        repeated_words.add(word)
print(f"Repeated words: {repeated_words}")

# encode() method to encode a string
# Explaination: The encode() method is used to encode a string into a byte object.
# It takes one argument: the encoding format (default is 'utf-8').
# The method returns a byte object representing the encoded string.
# The encode() method is useful when you need to convert a string to bytes for storage or transmission.
# The most common encoding format is 'utf-8', which can represent all characters in the Unicode standard.
# You can also use other encoding formats, such as 'ascii', 'latin-1', or 'utf-16', depending on your requirements.
# If the specified encoding format is not supported, the method raises a LookupError.
# If the string contains characters that cannot be encoded in the specified format, the method raises a UnicodeEncodeError.
# To handle encoding errors, you can specify an optional error handling scheme as a second argument to the encode() method.
# The most common error handling schemes are 'strict' (default), 'ignore', and 'replace'.
# 'strict' raises a UnicodeEncodeError on encoding errors, 'ignore' ignores the characters that cannot be encoded,
# and 'replace' replaces the characters that cannot be encoded with a replacement character (usually '?').
encoded_string = my_string.encode("utf-8")  # b'Hello, World!'
print(f"Encoded string: {encoded_string}")

# decode() method to decode a byte object
# Explaination: The decode() method is used to decode a byte object back into a string.
# It takes one argument: the encoding format (default is 'utf-8').
# The method returns a string representing the decoded byte object.
# The decode() method is useful when you need to convert bytes back to a string after storage or transmission.
# The most common encoding format is 'utf-8', which can represent all characters in the Unicode standard.
# You can also use other encoding formats, such as 'ascii', 'latin-1', or 'utf-16', depending on your requirements.
# If the specified encoding format is not supported, the method raises a LookupError.
# If the byte object contains bytes that cannot be decoded in the specified format, the method raises a UnicodeDecodeError.
# To handle decoding errors, you can specify an optional error handling scheme as a second argument to the decode() method.
# The most common error handling schemes are 'strict' (default), 'ignore', and 'replace'.
# 'strict' raises a UnicodeDecodeError on decoding errors, 'ignore' ignores the bytes that cannot be decoded,
# and 'replace' replaces the bytes that cannot be decoded with a replacement character (usually '?').
decoded_string = encoded_string.decode("utf-8")  # 'Hello, World!'
print(f"Decoded string: {decoded_string}")

# expandtabs() method to replace tab characters with spaces
# Explaination: The expandtabs() method is used to replace tab characters ('\t') in a string with spaces.
# It takes one argument: the number of spaces to replace each tab character with.
# The method returns a new string with the tab characters replaced with the specified number of spaces.
# If no argument is provided, the method defaults to replacing each tab character with 8 spaces.
# The expandtabs() method is useful for formatting strings that contain tab characters, especially when displaying them in a fixed-width font.
# You can adjust the number of spaces to suit your formatting needs.
tabbed_string = "Hello\tWorld".expandtabs(4)  # 'Hello   World'
print(f"String with expanded tabs: {tabbed_string}")

# format() method to format a string
# Explaination: The format() method is used to format a string by replacing placeholders with specified values.
# Placeholders are defined using curly braces {} in the string.
# The values to be replaced are passed as arguments to the format() method.
# The method returns a new string with the placeholders replaced by the specified values.
# You can use positional arguments, keyword arguments, or a combination of both to specify the values.
# You can also use format specifiers within the placeholders to control the formatting of the values.
# For example, you can specify the number of decimal places for a floating-point number or the width of a string.
# The format() method is useful for creating dynamic strings that include variable data.
# It allows you to create templates for strings and fill in the values as needed.
formatted_string = "Hello, {}. Welcome to {}.".format("Alice", "Python")  # 'Hello, Alice. Welcome to Python.'
print(f"Formatted string: {formatted_string}")

# f-string for string formatting (Python 3.6+)
# Explaination: F-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}.
# They were introduced in Python 3.6 and provide a more concise and readable way to format strings compared to the format() method.
# To create an f-string, prefix the string with the letter 'f' or 'F'.
# Inside the curly braces, you can include any valid Python expression, including variables, arithmetic operations, function calls, and more. 
# The expressions are evaluated at runtime, and their values are inserted into the string.
# F-strings also support format specifiers, similar to the format() method, allowing you to control the formatting of the values.
# F-strings are often more efficient than the format() method, as they are evaluated at runtime and do not require additional function calls.
# They are a popular choice for string formatting in modern Python code.
# Note: F-strings are only available in Python 3.6 and later versions.
# If you are using an earlier version of Python, you will need to use the format() method or other string formatting techniques.
name = "Bob"
language = "Java"
f_string = f"Hello, {name}. Welcome to {language}."  # 'Hello, Bob. Welcome to Java.'
print(f"F-string: {f_string}")

# String Formatting Types
# Explaination: Python provides several ways to format strings, including the use of format specifiers.
# Format specifiers are used to control the appearance of the formatted values, such as alignment, padding, number formatting, and more.
# Here are some commonly used format specifiers:

# Using :< to left align
# Explaination: The :< format specifier is used to left align a string within a specified width.
# It takes one argument: the width of the resulting string.
# The method returns a new string that is left aligned within the specified width, with spaces added to the right if necessary.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
# This format specifier is useful for creating tables or aligning text in a consistent way.
left_aligned = "{:<10}".format("Hello")  # 'Hello     '
print(f"Left aligned: '{left_aligned}'")

# Using :> to right align
# Explaination: The :> format specifier is used to right align a string within a specified width.
# It takes one argument: the width of the resulting string.
# The method returns a new string that is right aligned within the specified width, with spaces added to the left if necessary.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
# This format specifier is useful for creating tables or aligning text in a consistent way.
right_aligned = "{:>10}".format("Hello")  # '     Hello'
print(f"Right aligned: '{right_aligned}'")

# Using :^ to center align
# Explaination: The :^ format specifier is used to center align a string within a specified width.
# It takes one argument: the width of the resulting string.
# The method returns a new string that is centered within the specified width, with spaces added to both sides if necessary.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
# This format specifier is useful for creating tables or aligning text in a consistent way.
center_aligned = "{:^10}".format("Hello")  # '  Hello   '
print(f"Centered aligned: '{center_aligned}'")

# Using := to pad with zeros
# Explaination: The :0> format specifier is used to pad a string with leading zeros to a specified width.
# It takes one argument: the width of the resulting string.
# The method returns a new string that is padded with leading zeros to the specified width.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
# This format specifier is useful for formatting numbers or codes that require a fixed length.
# For example, you might use it to format a number as a 10-digit code by padding it with leading zeros.
zero_padded = "{:0>10}".format("123")  # '0000000123'
print(f"Zero-padded: '{zero_padded}'")

# Using := to keep the string to left most position
# Explaination: The := format specifier is used to pad a string with a specified character to a specified width.
# It takes two arguments: the character to pad with and the width of the resulting string.
# The method returns a new string that is padded with the specified character to the specified width.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
# This format specifier is useful for formatting strings in a specific way, such as creating a fixed-width field or aligning text.
# For example, you might use it to create a string that is left-aligned within a 10-character field, padded with dashes (-).
left_most = "{:=<10}".format("Hello")  # 'Hello-----'
print(f"Left most: '{left_most}'")

# Using := to keep the string to right most position
# Explaination: The := format specifier is used to pad a string with a specified character to a specified width.
# It takes two arguments: the character to pad with and the width of the resulting string.
# The method returns a new string that is padded with the specified character to the specified width.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
# This format specifier is useful for formatting strings in a specific way, such as creating a fixed-width field or aligning text.
# For example, you might use it to create a string that is right-aligned within a 10-character field, padded with dashes (-).
right_most = "{:=>10}".format("Hello")  # '-----Hello'
print(f"Right most: '{right_most}'")

# Using := to keep the string to center position
# Explaination: The := format specifier is used to pad a string with a specified character to a specified width.
# It takes two arguments: the character to pad with and the width of the resulting string.
# The method returns a new string that is padded with the specified character to the specified width.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
# This format specifier is useful for formatting strings in a specific way, such as creating a fixed-width field or aligning text.
# For example, you might use it to create a string that is center-aligned within a 10-character field, padded with equal signs (=).
center_most = "{:=^10}".format("Hello")  # '==Hello==='
print(f"Center most: '{center_most}'")

# Using :+ to show the sign of a number
# Explaination: The :+ format specifier is used to show the sign of a number.
# It adds a plus sign (+) before positive numbers and a minus sign (-) before negative numbers.
# The method returns a new string representing the number with the appropriate sign.
# This format specifier is useful for displaying numbers in a way that clearly indicates their sign, especially in financial or mathematical contexts.
# For example, you might use it to format a number as a signed value in a report or a table.
# Note: The :+ format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed without a sign.
signed_number = "{:+}".format(42)  # '+42'
print(f"Positive signed number: '{signed_number}'")

# Using :- to show the sign of a negative number
# Explaination: The :- format specifier is used to show the sign of a negative number.
# It adds a minus sign (-) before negative numbers.
# The method returns a new string representing the number with the appropriate sign.
# This format specifier is useful for displaying negative numbers in a way that clearly indicates their sign, especially in financial or mathematical contexts.
# For example, you might use it to format a number as a signed value in a report or a table.
# Note: The :- format specifier can be used with both integers and floating-point numbers.
# If the number is positive or zero, it will be displayed without a sign.
negative_signed_number = "{:-}".format(-42)  # '-42'
print(f"Negative signed number: '{negative_signed_number}'")

# Using : space to show a space for positive numbers
# Explaination: The : (space) format specifier is used to show a space before positive numbers.
# It adds a space before positive numbers and a minus sign (-) before negative numbers.
# The method returns a new string representing the number with the appropriate sign or space.
# This format specifier is useful for aligning numbers in a column, especially when displaying both positive and negative values.
# For example, you might use it to format a list of numbers in a table where positive and negative values need to be aligned.
# Note: The : (space) format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed with a leading space.
space_signed_number = "{: }".format(42)  # ' 42'
print(f"Space signed number: '{space_signed_number}'")

# Using :, to format a number with commas
# Explaination: The :, format specifier is used to format a number with commas as thousands separators.
# It adds commas to the number to separate groups of three digits, making it easier to read large numbers.
# The method returns a new string representing the number with commas as thousands separators. 
# This format specifier is useful for displaying large numbers in a way that is more readable.
# For example, you might use it to format a number in a financial report or a data table.
# Note: The :, format specifier can be used with both integers and floating-point numbers.
number_with_commas = "{:,}".format(1000000)  # '1,000,000'
print(f"Number with commas: '{number_with_commas}'")

# Using :_ to format a number with underscores
# Explaination: The :_ format specifier is used to format a number with underscores as thousands separators.
# It adds underscores to the number to separate groups of three digits, making it easier to read large numbers.
# The method returns a new string representing the number with underscores as thousands separators.
# This format specifier is useful for displaying large numbers in a way that is more readable, especially in programming contexts where underscores are often used in numeric literals.
# For example, you might use it to format a number in a code comment or documentation.
# Note: The :_ format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed without underscores.
number_with_underscores = "{:_}".format(1000000)  # '1_000_000'
print(f"Number with underscores: '{number_with_underscores}'")

# Using :b to format a number as binary
# Explaination: The :b format specifier is used to format a number as its binary representation.
# It converts the number to a binary string, which consists of only 0s and 1s.
# The method returns a new string representing the binary representation of the number.
# This format specifier is useful for displaying numbers in binary format, especially in programming or computer science contexts.
# For example, you might use it to format a number when working with bitwise operations or binary data.
# Note: The :b format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0'.
binary_format = "{:b}".format(10)  # '1010'
print(f"Binary format: '{binary_format}'")

# :c to format a number as its corresponding Unicode character
# Explaination: The :c format specifier is used to format a number as its corresponding Unicode character.
# It converts the number to a character based on its Unicode code point.
# The method returns a new string representing the Unicode character corresponding to the number.
# This format specifier is useful for displaying characters based on their Unicode values, especially when working with character encoding or text processing.
# For example, you might use it to format a number when working with ASCII values or Unicode characters.
# Note: The :c format specifier can be used with integers that represent valid Unicode code points.
# If the number is not a valid Unicode code point, it will raise a ValueError.
# For example, the number 65 corresponds to the Unicode character 'A'.
unicode_character = "{:c}".format(65)  # 'A'
print(f"Unicode character: '{unicode_character}'")

# Using :d to format a number as decimal
# Explaination: The :d format specifier is used to format a number as a decimal (base 10) integer.
# It converts the number to a string representation of its decimal value.
# The method returns a new string representing the decimal value of the number.
# This format specifier is useful for displaying integers in a standard decimal format.
# For example, you might use it to format a number in a report or a data table.
# Note: The :d format specifier can be used with both positive and negative integers.
# If the number is zero, it will be displayed as '0'.
# If the number is a floating-point number, it will be truncated to an integer before formatting.
# If the number is not an integer, it will raise a ValueError.
# For example, the number 42 will be formatted as '42'.
decimal_format = "{:d}".format(42)  # '42'
print(f"Decimal format: '{decimal_format}'")

# Using :e to format a number in scientific notation
# Explaination: The :e format specifier is used to format a number in scientific notation (also known as exponential notation).
# It converts the number to a string representation in the form of 'm.nnnnnne±xx', where 'm' is the mantissa, 'nnnnnn' is the fractional part, and 'xx' is the exponent.
# The method returns a new string representing the number in scientific notation.
# This format specifier is useful for displaying very large or very small numbers in a compact and readable format.
# For example, you might use it to format a number in a scientific report or a data table.
# Note: The :e format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0.000000e+00'.
# If the number is negative, the mantissa will include a minus sign.
# For example, the number 1000000 will be formatted as '1.000000e+06'.
scientific_notation = "{:e}".format(1000000)  # '1.000000e+06'
print(f"Scientific notation: '{scientific_notation}'")

# Using :E to format a number in scientific notation with uppercase
# Explaination: The :E format specifier is similar to the :e format specifier, but it uses uppercase 'E'
# to indicate the exponent in scientific notation.
# It converts the number to a string representation in the form of 'm.nnnnnnE±xx', where 'm' is the mantissa, 'nnnnnn' is the fractional part, and 'xx' is the exponent.
# The method returns a new string representing the number in scientific notation with an uppercase 'E'.
# This format specifier is useful for displaying very large or very small numbers in a compact and readable format, especially in contexts where uppercase notation is preferred.
# For example, you might use it to format a number in a scientific report or a data table.
# Note: The :E format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0.000000E+00'.
# If the number is negative, the mantissa will include a minus sign.
scientific_notation_upper = "{:E}".format(1000000)  # '1.000000E+06'
print(f"Scientific notation (uppercase): '{scientific_notation_upper}'")

# Using :f to format a number as fixed-point
# Explaination: The :f format specifier is used to format a number as a fixed-point number.
# It converts the number to a string representation with a specified number of decimal places (default is 6).
# The method returns a new string representing the number in fixed-point format.
# This format specifier is useful for displaying floating-point numbers in a standard decimal format.
# For example, you might use it to format a number in a financial report or a data table.
# Note: The :f format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0.000000'.
# If the number is negative, the string will include a minus sign.
# You can specify the number of decimal places by adding a precision value after the decimal point in the format specifier (e.g., :.2f for 2 decimal places).
# For example, the number 3.14159 will be formatted as '3.141590'.
fixed_point = "{:f}".format(3.14159)  # '3.141590'
print(f"Fixed-point format: '{fixed_point}'")

# Using :F to format a number as fixed-point with uppercase
# Explaination: The :F format specifier is similar to the :f format specifier, but it uses uppercase 'F' to indicate fixed-point format.
# It converts the number to a string representation with a specified number of decimal places (default is   6).
# The method returns a new string representing the number in fixed-point format with an uppercase 'F'.
# This format specifier is useful for displaying floating-point numbers in a standard decimal format, especially in contexts where uppercase notation is preferred.
# For example, you might use it to format a number in a financial report or a data table.
# Note: The :F format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0.000000'.
# If the number is negative, the string will include a minus sign.
# You can specify the number of decimal places by adding a precision value after the decimal point in the format specifier (e.g., :.2F for 2 decimal places).
# For example, the number 3.14159 will be formatted as '3.141590'.
fixed_point_upper = "{:F}".format(3.14159)  # '3.141590'
print(f"Fixed-point format (uppercase): '{fixed_point_upper}'")

# Using :g to format a number in general format
# Explaination: The :g format specifier is used to format a number in general format.
# It automatically chooses between fixed-point format and scientific notation based on the value of the number and the specified precision.
# The method returns a new string representing the number in general format.
# This format specifier is useful for displaying large or small numbers in a compact and readable format.
# For example, you might use it to format a number in a scientific report or a data table.
# Note: The :g format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0'.
general_format = "{:g}".format(1000000)  # '1000000'
print(f"General format: '{general_format}'")

# Using :G to format a number in general format with uppercase
# Explaination: The :G format specifier is similar to the :g format specifier, but it uses uppercase 'E' for scientific notation.
# It automatically chooses between fixed-point format and scientific notation based on the value of the number and the specified precision.
# The method returns a new string representing the number in general format with an uppercase 'E'.
# This format specifier is useful for displaying large or small numbers in a compact and readable format, especially in contexts where uppercase notation is preferred.
# For example, you might use it to format a number in a scientific report or a data table.
# Note: The :G format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0'.
# For example, the number 1000000 will be formatted as '1000000'.
general_format_upper = "{:G}".format(1000000)  # '1000000'
print(f"General format (uppercase): '{general_format_upper}'")

# Using :o to format a number as octal
# Explaination: The :o format specifier is used to format a number as its octal (base 8) representation.
# It converts the number to an octal string, which consists of digits 0-7.
# The method returns a new string representing the octal representation of the number.
# This format specifier is useful for displaying numbers in octal format, especially in programming or computer science contexts.
# For example, you might use it to format a number when working with file permissions or other octal-based data.
# Note: The :o format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0'.
# For example, the number 10 will be formatted as '12'.
octal_format = "{:o}".format(10)  # '12'
print(f"Octal format: '{octal_format}'")

# Using :x to format a number as hexadecimal
# Explaination: The :x format specifier is used to format a number as its hexadecimal (base 16) representation.
# It converts the number to a hexadecimal string, which consists of digits 0-9 and letters a-f.
# The method returns a new string representing the hexadecimal representation of the number.
# This format specifier is useful for displaying numbers in hexadecimal format, especially in programming or computer science contexts.
# For example, you might use it to format a number when working with memory addresses or color codes.
# Note: The :x format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0'.   
# For example, the number 255 will be formatted as 'ff'.
hexadecimal_format = "{:x}".format(255)  # 'ff'
print(f"Hexadecimal format: '{hexadecimal_format}'")

# Using :X to format a number as hexadecimal with uppercase
# Explaination: The :X format specifier is similar to the :x format specifier, but it uses uppercase letters (A-F) for the hexadecimal representation.
# It converts the number to a hexadecimal string, which consists of digits 0-9 and uppercase letters A-F.
# The method returns a new string representing the hexadecimal representation of the number with uppercase letters.
# This format specifier is useful for displaying numbers in hexadecimal format, especially in programming or computer science contexts where uppercase notation is preferred.
# For example, you might use it to format a number when working with memory addresses or color codes.
# Note: The :X format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0'.
# For example, the number 255 will be formatted as 'FF'.
hexadecimal_format_upper = "{:X}".format(255)  # 'FF'
print(f"Hexadecimal format (uppercase): '{hexadecimal_format_upper}'")

# Using :n to format a number according to the current locale
# Explaination: The :n format specifier is used to format a number according to the current locale.
# It formats the number with appropriate thousands separators and decimal points based on the user's locale settings.
# The method returns a new string representing the number formatted according to the current locale.
# This format specifier is useful for displaying numbers in a way that is familiar to users from different regions.
# For example, you might use it to format a number in a currency report or a data table.
# Note: The :n format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0' or '0.
# The actual formatting will depend on the locale settings of the user's environment.
# To use the :n format specifier effectively, you may need to set the locale using the locale module.
import locale   
locale.setlocale(locale.LC_ALL, '')  # Set to the user's default locale
locale_formatted_number = "{:n}".format(1000000)  # '1,000,000' or '1.000.000' based on locale
print(f"Locale formatted number: '{locale_formatted_number}'")

# Using :% to format a number as percentage
# Explaination: The :% format specifier is used to format a number as a percentage.
# It multiplies the number by 100 and appends a percent sign (%) to the result.
# The method returns a new string representing the number as a percentage.
# This format specifier is useful for displaying percentages in a standard format.
# For example, you might use it to format a number in a report or a data table.
# Note: The :% format specifier can be used with both integers and floating-point numbers.
# If the number is zero, it will be displayed as '0.00%'.
percentage_format = "{:.2%}".format(0.75)  # '75.00%'
print(f"Percentage format: '{percentage_format}'")

# Using :. to specify the number of decimal places
# Explaination: The :. format specifier is used to specify the number of decimal places to display for a floating-point number.
# It takes one argument: the number of decimal places to display.
# The method returns a new string representing the number formatted with the specified number of decimal places.
# This format specifier is useful for controlling the precision of floating-point numbers in a consistent way.
# For example, you might use it to format a number in a financial report or a data table.
# Note: The :. format specifier can be used with floating-point numbers.
# If the number is an integer, it will be converted to a floating-point number before formatting.
# If the number is zero, it will be displayed with the specified number of decimal places (e.g., '0.00' for 2 decimal places).
# You can specify the number of decimal places by adding a precision value after the decimal point in the format specifier (e.g., :.2f for 2 decimal places).
# For example, the number 3.14159 will be formatted as '3.14'.
decimal_places = "{:.2f}".format(3.14159)  # '3.14'
decimal_places = "{:.3f}".format(3.14159)  # '3.142'
print(f"Decimal places: '{decimal_places}'")

# Using :* to pad with a specific character
# Explaination: The :* format specifier is used to pad a string with a specific character.
# It takes two arguments: the character to pad with and the width of the resulting string.
# The method returns a new string that is padded with the specified character to the specified width.
# If the specified width is less than or equal to the length of the original string, the original string is returned unchanged.
# This format specifier is useful for formatting strings in a specific way, such as creating a fixed-width field or aligning text.
# For example, you might use it to create a string that is centered within a 10-character field, padded with asterisks (*).
# You can use any character for padding, not just asterisks.
padded_string = "{:*^10}".format("Hi")  # '****Hi****'
print(f"Padded string: '{padded_string}'")

# Using :{} to include curly braces in the formatted string
# Explaination: The :{} format specifier is used to include curly braces in the formatted string.
# It takes no arguments.
# To include a literal curly brace in the output, you need to double the curly braces in the format string (i.e., use '{{' and '}}').
# The method returns a new string with the curly braces included.
# This format specifier is useful when you want to include curly braces in a string that is being formatted, such as when creating templates or documentation.
# For example, you might use it to create a string that includes a curly brace as part of the text.
# Note: The :{} format specifier does not affect the formatting of other values in the string.
# It is simply a way to include curly braces in the output.
# If you want to include a single curly brace, you need to use double curly braces in the format string.
curly_braces = "This is a curly brace: {{}}".format()  #
print(f"Curly braces: '{curly_braces}'")

# Using : to format multiple values
# Explaination: The : format specifier can be used to format multiple values in a single string.
# You can include multiple placeholders in the format string, each represented by curly braces {}.
# The values to be replaced are passed as arguments to the format() method in the order they should appear in the string.
# The method returns a new string with all the placeholders replaced by the specified values.
# This format specifier is useful for creating dynamic strings that include multiple pieces of variable data.
# For example, you might use it to create a greeting message that includes a person's name, age, and country.
# You can also use positional or keyword arguments to specify the values to be replaced.
# For example, you can use {0}, {1}, etc. for positional arguments, or {name}, {age}, etc. for keyword arguments.
# You can mix positional and keyword arguments in the same format string.
# You can also use nested fields, alignment, and width specifiers with multiple values.
# For example, you can use {:<10}, {:^10}, {:>10}, etc. to control the alignment and width of each value.
# Note: The number of placeholders in the format string must match the number of arguments passed to the format() method.
# If there are more placeholders than arguments, a IndexError will be raised.
# If there are more arguments than placeholders, the extra arguments will be ignored.
# You can also use the format_map() method to format a string using a dictionary.
# This method takes a single argument, which is a dictionary containing the values to be replaced.
# The keys in the dictionary correspond to the placeholders in the format string.
# For example, you can use {name}, {age}, etc. as placeholders and pass a dictionary with the corresponding keys and values.
# This method is useful when you have a large number of values to be replaced, or when the values are stored in a dictionary.
# It allows you to avoid passing a long list of arguments to the format() method.
multiple_values = "Name: {}, Age: {}, Country: {}".format("Alice", 30, "USA")  # 'Name: Alice, Age: 30, Country: USA'
print(f"Multiple values: '{multiple_values}'")

# Using : to format with positional and keyword arguments
# Explaination: The : format specifier can be used to format a string using both positional and keyword arguments.
# You can include multiple placeholders in the format string, each represented by curly braces {}.
# The values to be replaced can be passed as positional arguments (in the order they should appear) or as keyword arguments (using the format key=value).
# The method returns a new string with all the placeholders replaced by the specified values.
# This format specifier is useful for creating dynamic strings that include multiple pieces of variable data, especially when some values are more naturally represented as keywords.
# For example, you might use it to create a greeting message that includes a person's name, age, and country.
# You can mix positional and keyword arguments in the same format string.
# For example, you can use {0}, {1}, etc. for positional arguments, or {name}, {age}, etc. for keyword arguments.
# You can also use nested fields, alignment, and width specifiers with positional and keyword arguments.
# For example, you can use {:<10}, {:^10}, {:>10}, etc. to control the alignment and width of each value.
# Note: The number of placeholders in the format string must match the number of arguments passed to the format() method.
# If there are more placeholders than arguments, a IndexError will be raised.
# If there are more arguments than placeholders, the extra arguments will be ignored.
# You can also use the format_map() method to format a string using a dictionary, as described earlier.
positional_keyword = "Name: {0}, Age: {1}, Country: {country}".format("Bob", 25, country="Canada")  # 'Name: Bob, Age: 25, Country: Canada'
print(f"Positional and keyword arguments: '{positional_keyword}'")

# Using : to format with nested fields
# Explaination: The : format specifier can be used to format a string with nested fields.
# Nested fields allow you to access elements of a data structure (like a list or dictionary) within the format string.
# You can include placeholders in the format string that reference elements of a data structure using indexing or key access.
# The method returns a new string with all the placeholders replaced by the specified values from the data structure.
# This format specifier is useful for creating dynamic strings that include data from complex structures.
# For example, you might use it to create a message that includes coordinates from a tuple or values from a dictionary.
# You can mix nested fields with positional and keyword arguments, as well as alignment and width specifiers.
# For example, you can use {:<10}, {:^10}, {:>10}, etc. to control the alignment and width of each value.
# Note: The data structure being accessed must be passed as an argument to the format() method.
# If the specified index or key does not exist in the data structure, a KeyError or IndexError will be raised.
# You can also use the format_map() method to format a string using a dictionary, as described earlier.
nested_fields = "Coordinates: ({point[0]}, {point[1]})".format(point=(10, 20))  # 'Coordinates: (10, 20)'
print(f"Nested fields: '{nested_fields}'")

# Using : to format with alignment and width
# Explaination: The : format specifier can be used to format a string with alignment and width.
# You can include alignment and width specifiers in the format string to control how the values are displayed.
# The alignment specifiers are:
# '<' for left alignment
# '^' for center alignment
# '>' for right alignment
# The width specifier is an integer that specifies the minimum width of the resulting string.
# If the specified width is greater than the length of the original string, the string will be padded with spaces (or another specified character) to reach the desired width.
# The method returns a new string with the specified alignment and width applied to each value.
# This format specifier is useful for creating neatly formatted output, especially in tables or reports.
# For example, you might use it to create a table with columns that are aligned and have a fixed width.
# You can mix alignment and width specifiers with positional and keyword arguments, as well as nested fields.
# For example, you can use {0:<10}, {1:^10}, {name:>10}, etc. to control the alignment and width of each value.
# Note: The number of placeholders in the format string must match the number of arguments passed to the format() method.
# If there are more placeholders than arguments, a IndexError will be raised.
# If there are more arguments than placeholders, the extra arguments will be ignored.
# You can also use the format_map() method to format a string using a dictionary, as described earlier.
alignment_width = "|{:<10}|{:^10}|{:>10}|".format("Left", "Center", "Right")  # '|Left      |  Center  |     Right|'
print(f"Alignment and width: '{alignment_width}'")

# Using format_map() method to format using a dictionary
# Explaination: The format_map() method is used to format a string using a dictionary.
# It takes a single argument, which is a dictionary containing the values to be replaced in the format string.
# The keys in the dictionary correspond to the placeholders in the format string.
# The method returns a new string with all the placeholders replaced by the specified values from the dictionary.
# This method is useful when you have a large number of values to be replaced, or when the values are stored in a dictionary.
# It allows you to avoid passing a long list of arguments to the format() method.
# For example, you can use {name}, {age}, etc. as placeholders and pass a dictionary with the corresponding keys and values.
# You can mix format_map() with other formatting options, such as alignment and width specifiers.
# For example, you can use {:<10}, {:^10}, {:>10}, etc. to control the alignment and width of each value.
# Note: The keys in the dictionary must match the placeholders in the format string.
# If a key in the format string does not exist in the dictionary, a KeyError will be raised.
# If there are extra keys in the dictionary that are not used in the format string, they will be ignored.
# You can also use the format() method to format a string using positional and keyword arguments, as described earlier.
data = {'name': 'Charlie', 'age': 28, 'country': 'UK'}
formatted_map = "Name: {name}, Age: {age}, Country: {country}".format_map(data)  # 'Name: Charlie, Age: 28, Country: UK'
print(f"Formatted using format_map: '{formatted_map}'")

# isalpha() method to check if all characters in the string are alphabetic
# Explaination: The isalpha() method checks if all characters in a string are alphabetic (letters).
# It returns True if all characters are alphabetic and there is at least one character, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only letters, such as names or words.
# For example, "Hello" would return True, while "Hello123" or "Hello!" would return False.
# Note: The isalpha() method does not consider spaces, numbers, or special characters as alphabetic.
# It only checks for letters (a-z, A-Z) and does not account for accented characters or letters from non-Latin alphabets.
alpha_check = "Hello".isalpha()  # True
print(f"Is alphabetic: {alpha_check}")

# isdigit() method to check if all characters in the string are digits
# Explaination: The isdigit() method checks if all characters in a string are digits (0-9).
# It returns True if all characters are digits and there is at least one character, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only numeric characters, such as phone numbers or IDs.
# For example, "12345" would return True, while "123a45" or "123 45" would return False.
# Note: The isdigit() method does not consider spaces, letters, or special characters as digits.
# It only checks for numeric characters (0-9) and does not account for decimal points or negative signs.
digit_check = "12345".isdigit()  # True
print(f"Is digit: {digit_check}")

# isalnum() method to check if all characters in the string are alphanumeric
# Explaination: The isalnum() method checks if all characters in a string are alphanumeric (letters or digits).
# It returns True if all characters are alphanumeric and there is at least one character, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only letters and numbers, such as usernames or passwords.
# For example, "Hello123" would return True, while "Hello 123" or "Hello!" would return False.
# Note: The isalnum() method does not consider spaces or special characters as alphanumeric.
# It only checks for letters (a-z, A-Z) and digits (0-9).
# It does not account for accented characters or letters from non-Latin alphabets.
alnum_check = "Hello123".isalnum()  # True
print(f"Is alphanumeric: {alnum_check}")

# isascii() method to check if all characters in the string are ASCII
# Explaination: The isascii() method checks if all characters in a string are ASCII characters.
# It returns True if all characters are ASCII (i.e., have a Unicode code point in the range 0-127) and there is at least one character, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only standard ASCII characters, which are commonly used in programming and data processing.
# For example, "Hello" would return True, while "Héllo" or "Hello!" would return False.
# Note: The isascii() method does not consider non-ASCII characters, such as accented letters or characters from non-Latin alphabets, as ASCII.
# It only checks for characters in the standard ASCII range (0-127).
ascii_check = "Hello".isascii()  # True
print(f"Is ASCII: {ascii_check}")

# isdecimal() method to check if all characters in the string are decimal
# Explaination: The isdecimal() method checks if all characters in a string are decimal characters.
# It returns True if all characters are decimal and there is at least one character, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only decimal characters, such as numbers in a specific numeral system.
# For example, "12345" would return True, while "123a45" or "123 45" would return False.
# Note: The isdecimal() method only considers characters that are classified as decimal characters in Unicode.
# This includes the standard digits (0-9) as well as other decimal characters from different numeral systems.
# It does not consider letters, spaces, or special characters as decimal.
decimal_check = "12345".isdecimal()  # True
print(f"Is decimal: {decimal_check}")

# isidentifier() method to check if the string is a valid identifier
# Explaination: The isidentifier() method checks if a string is a valid Python identifier.
# It returns True if the string is a valid identifier, otherwise it returns False.
# A valid identifier must start with a letter (a-z, A-Z) or an underscore (_), followed by letters, digits (0-9), or underscores.
# It cannot be a reserved keyword in Python (e.g., "if", "else", "while", etc.).
# This method is useful for validating variable names, function names, or other identifiers in Python code.
# For example, "variable_name" would return True, while "1variable" or "var-name" would return False.
# Note: The isidentifier() method does not check for reserved keywords.
# It only checks the syntax of the string to determine if it can be used as an identifier.
# You can use the keyword module to check if a string is a reserved keyword in Python.
identifier_check = "variable_name".isidentifier()  # True
print(f"Is identifier: {identifier_check}")

# isnumeric() method to check if all characters in the string are numeric
# Explaination: The isnumeric() method checks if all characters in a string are numeric characters.
# It returns True if all characters are numeric and there is at least one character, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only numeric characters, such as numbers in various numeral systems.
# For example, "12345" would return True, while "123a45" or "123 45" would return False.
# Note: The isnumeric() method considers a wider range of numeric characters than the isdigit() and isdecimal() methods.
# It includes characters that represent numbers in different numeral systems, such as Roman numerals, fractions, and other numeric symbols.
# It does not consider letters, spaces, or special characters as numeric.
numeric_check = "12345".isnumeric()  # True
print(f"Is numeric: {numeric_check}")

# islower() method to check if all characters in the string are lowercase
# Explaination: The islower() method checks if all characters in a string are lowercase letters.
# It returns True if all characters are lowercase and there is at least one lowercase letter, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only lowercase letters, such as usernames or certain types of identifiers.
# For example, "hello" would return True, while "Hello" or "hello123" would return False.
# Note: The islower() method does not consider uppercase letters, digits, spaces, or special characters as lowercase.
# It only checks for lowercase letters (a-z).
lower_check = "hello".islower()  # True
print(f"Is lowercase: {lower_check}")

# isupper() method to check if all characters in the string are uppercase
# Explaination: The isupper() method checks if all characters in a string are uppercase letters.
# It returns True if all characters are uppercase and there is at least one uppercase letter, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only uppercase letters, such as acronyms or certain types of identifiers.
# For example, "HELLO" would return True, while "Hello" or "HELLO123" would return False.
# Note: The isupper() method does not consider lowercase letters, digits, spaces, or special characters as uppercase.
# It only checks for uppercase letters (A-Z).
upper_check = "HELLO".isupper()  # True
print(f"Is uppercase: {upper_check}")

# isspace() method to check if all characters in the string are whitespace
# Explaination: The isspace() method checks if all characters in a string are whitespace characters.
# It returns True if all characters are whitespace and there is at least one character, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only whitespace, such as when checking for empty or blank strings.
# For example, "   " would return True, while " Hello " or "Hello" would return False.
# Note: The isspace() method considers spaces, tabs, newlines, and other whitespace characters as whitespace.
# It does not consider letters, digits, or special characters as whitespace.
space_check = "   ".isspace()  # True
print(f"Is whitespace: {space_check}")

# istitle() method to check if the string is in title case
# Explaination: The istitle() method checks if a string is in title case.
# It returns True if the string is in title case, otherwise it returns False.
# A string is considered to be in title case if each word in the string starts with an uppercase letter followed by lowercase letters.
# This method is useful for validating input to ensure that it follows title case formatting, such as for book titles or headings.
# For example, "Hello World" would return True, while "hello world" or "Hello world" would return False.
# Note: The istitle() method does not consider words that are entirely uppercase or entirely lowercase as title case.
# It only checks for the specific pattern of an uppercase letter followed by lowercase letters for each word.
# It also considers non-letter characters (such as punctuation) as word boundaries.
title_check = "Hello World".istitle()  # True
print(f"Is title case: {title_check}")

# isprintable() method to check if all characters in the string are printable
# Explaination: The isprintable() method checks if all characters in a string are printable.
# It returns True if all characters are printable or the string is empty, otherwise it returns False.
# This method is useful for validating input to ensure that it contains only characters that can be printed, such as when displaying text in a user interface or printing to a console.
# For example, "Hello World" would return True, while "Hello\nWorld" or "Hello\tWorld" would return False.
# Note: The isprintable() method considers letters, digits, punctuation, and whitespace characters (except for control characters like newlines and tabs) as printable.
# It does not consider control characters or non-printable characters as printable.
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
# Explaination: The join() method is used to join elements of an iterable (such as a list or tuple) into a single string.
# It takes one argument, which is the iterable containing the elements to be joined.
# The method returns a new string that is the concatenation of the elements in the iterable, separated by the string on which the method is called.
# This method is useful for creating a single string from multiple pieces of data, such as when generating a comma-separated list or a sentence from individual words.
# For example, you might use it to join a list of words into a sentence or a list of items into a comma-separated string.
# Note: The elements in the iterable must be strings; otherwise, a TypeError will be raised.
# If the iterable is empty, the method will return an empty string.
# You can use any string as the separator, including an empty string.
# For example, using a space as the separator will join the words with spaces in between.
iterable = ['Hello', 'World', 'from', 'Python']
joined_string = ' '.join(iterable)  # 'Hello World from Python'
print(f"Joined string: {joined_string}")

# ljust() method to left align a string with padding
# Explaination: The ljust() method is used to left-align a string within a specified width.
# It takes two arguments: the width of the resulting string and an optional fill character (default is a space).
# The method returns a new string that is left-aligned and padded with the specified fill character to reach the desired width.
# This method is useful for formatting strings in a specific way, such as creating a fixed-width field or aligning text.
# For example, you might use it to create a string that is left-aligned within a 10-character field, padded with hyphens (-).
# You can use any character for padding, not just hyphens.
left_justified = "Hello".ljust(10, '-')  # 'Hello-----
print(f"Left justified: '{left_justified}'")

# rjust() method to right align a string with padding
# Explaination: The rjust() method is used to right-align a string within a specified width.
# It takes two arguments: the width of the resulting string and an optional fill character (default is a space).
# The method returns a new string that is right-aligned and padded with the specified fill character to reach the desired width.
# This method is useful for formatting strings in a specific way, such as creating a fixed-width field or aligning text.
# For example, you might use it to create a string that is right-aligned within a 10-character field, padded with hyphens (-).
# You can use any character for padding, not just hyphens.
right_justified = "Hello".rjust(10, '-')  # '-----Hello
print(f"Right justified: '{right_justified}'")

# lower() method to convert a string to lowercase
# Explaination: The lower() method is used to convert all uppercase letters in a string to lowercase.
# It returns a new string with all characters converted to lowercase.
# This method is useful for standardizing text input, such as when performing case-insensitive comparisons or searches.
# For example, you might use it to convert user input to lowercase before checking if it matches a specific value.
# Note: The lower() method does not modify the original string; it returns a new string.
# It only affects uppercase letters (A-Z) and does not change lowercase letters, digits, spaces, or special characters.
# For example, "Hello World!" would be converted to "hello world!".
lowercase_string = "HELLO".lower()  # 'hello'
print(f"Lowercase string: {lowercase_string}")

# lstrip() method to remove leading whitespace
# Explaination: The lstrip() method is used to remove leading whitespace characters from a string.
# It returns a new string with leading whitespace removed.
# This method is useful for cleaning up text input, such as when removing extra spaces at the beginning of a string.
# For example, you might use it to remove leading spaces from user input before processing it.
# Note: The lstrip() method only removes whitespace characters (spaces, tabs, newlines) from the beginning of the string.
# It does not affect trailing whitespace or whitespace in the middle of the string.
# If there are no leading whitespace characters, the original string is returned unchanged.
# For example, "   Hello   " would be converted to "Hello   ".
leading_stripped = "   Hello   ".lstrip()  # 'Hello   '
print(f"Leading whitespace removed: '{leading_stripped}'")

# maketrans() method to create a translation table
# Explaination: The maketrans() method is used to create a translation table for use with the translate() method.
# It takes two arguments: a string of characters to be replaced and a string of characters to replace them with.
# The method returns a translation table that can be used to translate characters in a string.
# This method is useful for performing character substitutions in a string, such as replacing certain letters with others.
# For example, you might use it to create a simple cipher or to replace specific characters in user input.
# Note: The two strings passed to maketrans() must be of the same length, as each character in the first string will be replaced by the corresponding character in the second string.
# The translate() method is then used with the translation table to perform the substitutions in a string.
# If a character in the original string is not found in the translation table, it remains unchanged.
# You can also use the maketrans() method to create a translation table that removes specific characters by passing None as the second argument.
translation_table = str.maketrans("Helo", "Jxyz")
translated_string = "Hello, World!".translate(translation_table)  # 'Jxyyz, Wxrzd!'
print(f"Translated string: {translated_string}")

# Explaination of the output:
# The maketrans() method creates a mapping where 'H' is replaced with 'J',
# 'e' with 'x', 'l' with 'y', and 'o' with 'z'.
# The translate() method then applies this mapping to the original string.

# partition() method to split a string into three parts
# Explaination: The partition() method is used to split a string into three parts based on the first occurrence of a specified separator.
# It takes one argument, which is the separator string.
# The method returns a tuple containing three elements: the part before the separator, the separator itself, and the part after the separator.
# This method is useful for extracting specific parts of a string, such as when parsing data or processing text.
# For example, you might use it to split a string at the first comma to separate a name from a list of items.
# Note: If the separator is not found in the string, the method returns a tuple containing the original string, an empty string, and another empty string.
# The partition() method only splits at the first occurrence of the separator.
# If you need to split at the last occurrence, you can use the rpartition() method instead.
# The separator can be any string, including special characters or whitespace.
# If the separator is an empty string, the method will raise a ValueError.
partitioned_string = "Hello, World!".partition(", ")  # ('Hello', ', ', 'World!')
print(f"Partitioned string: {partitioned_string}")

# rpartition() method to split a string into three parts from the right
# Explaination: The rpartition() method is used to split a string into three parts based on the last occurrence of a specified separator.
# It takes one argument, which is the separator string.
# The method returns a tuple containing three elements: the part before the separator, the separator itself, and the part after the separator.
# This method is useful for extracting specific parts of a string, such as when parsing data or processing text.
# For example, you might use it to split a string at the last comma to separate a name from a list of items.
# Note: If the separator is not found in the string, the method returns a tuple containing two empty strings and the original string.
# The rpartition() method only splits at the last occurrence of the separator.
# If you need to split at the first occurrence, you can use the partition() method instead.
# The separator can be any string, including special characters or whitespace.
# If the separator is an empty string, the method will raise a ValueError.
rpartitioned_string = "Hello, World, from Python".rpartition(", ")  # ('Hello, World', ', ', 'from Python')
print(f"Right partitioned string: {rpartitioned_string}")

# replace() method to replace occurrences of a substring
# Explaination: The replace() method is used to replace occurrences of a specified substring with another substring in a string.
# It takes two arguments: the substring to be replaced and the substring to replace it with.
# The method returns a new string with all occurrences of the specified substring replaced.
# This method is useful for modifying text, such as correcting typos, updating information, or formatting data.
# For example, you might use it to replace all occurrences of "World" with "Python" in a greeting message.
# Note: The replace() method does not modify the original string; it returns a new string.
# You can also specify a third argument, which is the maximum number of occurrences to replace.
replaced_string = "Hello, World!".replace("World", "Python")  # 'Hello, Python!'
print(f"Replaced string: {replaced_string}")

# rfind() method to find the last occurrence of a substring
# Explaination: The rfind() method is used to find the last occurrence of a specified substring in a string.
# It takes one argument, which is the substring to search for.
# The method returns the index of the last occurrence of the specified substring, or -1 if the substring is not found.
# This method is useful for locating specific parts of a string, such as when searching for keywords or parsing data.
# For example, you might use it to find the last occurrence of "World" in a greeting message.
# Note: The rfind() method searches from the end of the string towards the beginning.
# It is case-sensitive, meaning that "world" and "World" would be treated as different substrings.
# If the substring is not found, the method returns -1.
# You can also use the find() method to find the first occurrence of a substring, as described earlier.
last_position = "Hello, World! Welcome to the World!".rfind("World")  # 26
print(f"Last position of 'World': {last_position}")

# rindex() method to find the last occurrence of a substring (raises an error if not found)
# Explaination: The rindex() method is similar to the rfind() method, but it raises a ValueError if the specified substring is not found in the string.
# It takes one argument, which is the substring to search for.
# The method returns the index of the last occurrence of the specified substring.
# This method is useful for locating specific parts of a string when you want to ensure that the substring exists.
# For example, you might use it to find the last occurrence of "World" in a greeting message and handle the case where it is not found.
# Note: The rindex() method searches from the end of the string towards the beginning.
# It is case-sensitive, meaning that "world" and "World" would be treated as different substrings.
# If the substring is not found, the method raises a ValueError.
try:
    last_position = "Hello, World! Welcome to the World!".rindex("World")  # 26
    print(f"Last position of 'World': {last_position}")
except ValueError:
    print("'World' not found in the string")

# rjust() method to right align a string with padding
# Explaination: The rjust() method is used to right-align a string within a specified width.
# It takes two arguments: the width of the resulting string and an optional fill character (default is a space).
# The method returns a new string that is right-aligned and padded with the specified fill character to reach the desired width.
# This method is useful for formatting strings in a specific way, such as creating a fixed-width field or aligning text.
# For example, you might use it to create a string that is right-aligned within a 10-character field, padded with hyphens (-).
# You can use any character for padding, not just hyphens.
# For example, using a space as the separator will join the words with spaces in between.
right_justified = "Hello".rjust(10, '-')  # '-----Hello'
print(f"Right justified: '{right_justified}'")

# rstrip() method to remove trailing whitespace 
# Explaination: The rstrip() method is used to remove trailing whitespace characters from a string.
# It returns a new string with trailing whitespace removed.
# This method is useful for cleaning up text input, such as when removing extra spaces at the end of a string.
# For example, you might use it to remove trailing spaces from user input before processing it.
# Note: The rstrip() method only removes whitespace characters (spaces, tabs, newlines) from the end of the string.
# It does not affect leading whitespace or whitespace in the middle of the string.
# If there are no trailing whitespace characters, the original string is returned unchanged.
# For example, "   Hello   " would be converted to "   Hello".
# You can also use the lstrip() method to remove leading whitespace, as described earlier.
trailing_stripped = "   Hello   ".rstrip()  # '   Hello'
print(f"Trailing whitespace removed: '{trailing_stripped}'")

# rsplit() method to split a string from the right
# Explaination: The rsplit() method is used to split a string into a list of substrings based on a specified separator, starting from the right side of the string.
# It takes two arguments: the separator string and an optional maximum number of splits (default is -1, which means no limit).
# The method returns a list of substrings, split from the right side of the string.
# This method is useful for extracting specific parts of a string when you want to limit the number of splits or when the relevant data is located towards the end of the string.
# For example, you might use it to split a string at the last two commas to separate a name from a list of items.
# Note: If the separator is not found in the string, the method returns a list containing the original string.
# If the maximum number of splits is specified, the method will perform at most that many splits, starting from the right.
# The separator can be any string, including special characters or whitespace.
# If the separator is an empty string, the method will raise a ValueError.
rsplit_string = "one,two,three,four".rsplit(",", 2)
print(f"Right split string: {rsplit_string}")  # ['one,two', 'three', 'four']

# splitlines() method to split a string at line breaks
# Explaination: The splitlines() method is used to split a string into a list of lines based on line breaks.
# It returns a list of strings, where each string represents a line in the original string.
# This method is useful for processing multi-line text, such as reading data from a file or handling user input that spans multiple lines.
# For example, you might use it to split a multi-line string into a list of lines.
# Note: The splitlines() method recognizes various line break characters, including '\n' (newline), '\r' (carriage return), and '\r\n' (carriage return followed by newline).
# By default, the line break characters are not included in the resulting list of lines.
# If you want to keep the line break characters, you can pass True as an argument to the method.
# If the string does not contain any line breaks, the method returns a list containing the original string.
# You can also use the split() method to split a string based on a specific separator, as described earlier.
# For example, using split('\n') would achieve a similar result for newline characters.
# Here, we demonstrate the default behavior without keeping line breaks.
multiline_string = "Hello\nWorld\nfrom\nPython"
split_lines = multiline_string.splitlines()  # ['Hello', 'World', 'from', 'Python']
print(f"Split lines: {split_lines}")

# swapcase() method to swap the case of each character in the string
# Explaination: The swapcase() method is used to swap the case of each character in a string.
# It converts all uppercase characters to lowercase and all lowercase characters to uppercase.
# Non-alphabetic characters (like numbers, symbols, and spaces) are left unchanged.
# This method returns a new string and does not modify the original one.
swapped_case = "Hello World".swapcase()  # 'hELLO wORLD'
print(f"Swapped case: {swapped_case}")

# title() method to convert the first character of each word to uppercase
# Explaination: The title() method returns a "titlecased" version of the string.
# This means that the first character of each word is converted to uppercase,
# and all subsequent characters in the word are converted to lowercase.
# Words are identified as sequences of letters separated by non-letter characters (like spaces or punctuation).
# This method is useful for formatting headings, titles, or names.
title_case = "hello world from python".title()  # 'Hello World From Python'
print(f"Title case: {title_case}")  

# zfill() method to pad a string with zeros on the left
# Explaination: The zfill() method pads a string on the left with zeros ('0') to fill a specified width.
# It takes one argument: the desired width of the final string.
# If the original string's length is less than the specified width, it adds leading zeros.
# If the length is already equal to or greater than the width, the original string is returned unchanged.
# This method is sign-aware, meaning if the string starts with '+' or '-', the padding is applied after the sign.
# It is useful for formatting fixed-width numeric strings, like serial numbers or time values.
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