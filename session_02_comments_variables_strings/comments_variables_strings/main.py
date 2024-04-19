# %% [markdown]
# # Comments, Variables and Strings in Python
# 

# %% [markdown]
# ---
# 

# %% [markdown]
# ### Comments
# 
# Comments in Python are invaluable tools for enhancing code clarity and maintainability. By providing explanations, context, and insights into the logic behind the code, comments help both present and future developers understand the purpose and functionality of different parts of the codebase. Additionally, comments can serve as reminders for unfinished tasks, clarify complex sections, and document algorithms, contributing to better collaboration, easier debugging, and overall code quality.
# 

# %% [markdown]
# **Single Line Comment**
# 

# %%
# This is a single-line comment

# %%
"""
This is a multi-line comment.
It spans across multiple lines.
"""

# %%
"""
This is another way of writing a multi-line comment.
"""

# %% [markdown]
# ---
# 

# %% [markdown]
# ### Variables
# 
# In Python, variable names must adhere to certain rules for proper definition:
# 
# 1. **Naming Convention**: Variable names should be descriptive and meaningful, following the convention of using lowercase letters with words separated by underscores (snake_case). For example: `my_variable`, `user_name`, `total_count`.
# 
# 2. **Start with a Letter or Underscore**: Variable names must start with either a letter (a-z, A-Z) or an underscore (`_`). They cannot start with a digit or any special characters other than an underscore.
# 
# 3. **Consist of Letters, Digits, and Underscores**: After the first character, variable names can consist of letters (a-z, A-Z), digits (0-9), and underscores (`_`). They cannot contain spaces or any other special characters.
# 
# 4. **Case Sensitivity**: Python is case-sensitive, so variable names like `my_variable`, `My_Variable`, and `MY_VARIABLE` would be treated as distinct variables.
# 
# 5. **Reserved Keywords**: Variable names cannot be the same as Python's reserved keywords, which are predefined and have special meanings in the language. For example, you cannot name a variable `for`, `if`, `while`, `def`, `class`, etc.
# 
# 6. **Avoid Using Built-in Names**: It's best to avoid using names of built-in functions or modules (such as `print`, `list`, `dict`, etc.) as variable names to prevent potential conflicts and confusion.
# 
# 7. **Note** Use `snake_case` for variable names and `UPPER_SNAKE_CASE` for constants.
# 
# Following these rules ensures that your variable names are clear, readable, and won't cause unexpected behavior in your Python code.
# 

# %%
# Reserved keywords list

import keyword

reserved_words: list[str] = keyword.kwlist
print(reserved_words)

# %%
# Builtin Functions name list

import builtins

builtin_functions: list[str] = [
    func for func in dir(builtins) if callable(getattr(builtins, func))
]
print(builtin_functions)

# %%
# Defining a variable

height: int = 5

print(height)
print(type(height))
print(id(height))
print(dir(height))
print([i for i in dir(height) if "__" not in i])

# %% [markdown]
# ---
# 

# %% [markdown]
# ### Strings
# 
# In Python, strings are sequences of characters, typically used to represent text data. They are immutable, meaning once created, their contents cannot be changed. Strings can be enclosed in either single quotes (') or double quotes ("), and triple quotes (''' or """) are used for multiline strings. Python provides a rich set of methods and operations to manipulate and work with strings, including concatenation, slicing, formatting, and searching. Strings support Unicode characters, making Python particularly versatile for handling text data in various languages and encodings.
# 

# %%
name: str = "Hassan"
print(type(name))
print(name)
print(id(height))
print([i for i in dir(name) if "__" not in i])

# %%
name: str = "Hassan"
print(type(name))
print(name)

# %%
name: str = """Hassan"""
print(type(name))
print(name)

# %%
name: str = """Hassan"""
print(type(name))
print(name)

# %% [markdown]
# You can also use single quote or double quote in a string
# 

# %%
message: str = "Father's Name : Zaheer"
print(message)

# %%
message: str = "Father's Name : Zaheer"
print(message)

# %% [markdown]
# **Concatenation**
# 

# %%
name: str = "Hassan " + "Ali " + "Khan"
print(name)

# %%
print("Hassan" + str(92))

# %% [markdown]
# **Why Multiline Strings / triple quotes**
# 

# %%
# We need work around with type conversion, concatenation, skipping words etc

name: str = "Hassan"
fname: str = "Zaheer"
education: str = "Master's"
age: int = 30

card: str = (
    "PIAIC Student Card\
    \nStudent Name: "
    + name
    + "\nFather Name: "
    + fname
    + "\nAge:"
    + str(age)
    + "\nEducation:"
    + education
)

print(card)

# %% [markdown]
# **Defining Multiline String**
# 

# %%
name: str = "Hassan"
fname: str = "Zaheer"
education: str = "Master's"
age: int = 30

card: str = """PIAIC Student Card
    
    Student Name: ---
    Father Name: ---
    Age: ---
    Education: ---
    """

print(card)

# %%
# F-string in Python

name: str = "Hassan"
fname: str = "Zaheer"
education: str = "Master's"
age: int = 30

card: str = f"""PIAIC Student Card
    
    Student Name: {name}
    Father Name: {fname}
    Age: {age}
    Education: {education}
    """

print(card)

# %%
# F-string in Python

name: str = "Hassan"
fname: str = "Zaheer"
education: str = "Master's"
age: int = 30

card: str = f"""PIAIC Student Card
    
    Student Name: {name}
    Father Name: {fname}
    Age: {age}
    Education: {education}
    """

print(card)

# %%
# jinja style in Python

name: str = "Hassan"
fname: str = "Zaheer"
education: str = "Master's"
age: int = 30

card: str = (
    f"""PIAIC Student Card
    
    Student Name: %s
    Father Name: %s
    Age: %d
    Education: %s
    """
    % (name, fname, age, education)
)

print(card)

# %% [markdown]
# **escape characters**
# 

# %%
print("Hello\nworld")

# %%
print("Hello\tworld")

# %%
print("Hello\bworld")

# %% [markdown]
# **String Methods**
# 

# %%
[i for i in dir(str) if "__" not in i]

# %%
# capitalize: Converts the first character to uppercase
text: str = "hello world"
print(text.capitalize())

# %%
# casefold: Converts string into lowercase
text: str = "HELLO World"
print(text.casefold())

# %%
# center: Returns a centered string
text: str = "hello"
print(text.center(8, "*"))

# %%
# count: Returns the number of occurrences of a substring
text: str = "hello world"
print(text.count("o"))

# %%
# encode: Returns the encoded version of the string
text: str = "hello"
print(text.encode())

# %%
# endswith: Checks if a string ends with a specified suffix
text: str = "hello world"
print(text.endswith("world"))

# %%
# expandtabs: Sets the tab size of the string
text: str = "hello\tworld"
print(text.expandtabs(20))

# %%
# find: Searches the string for a specified value and returns the position of where it was found
text: str = "hello world"
print(text.find("world"))

# %%
# format: Formats the string
name: str = "John"
age: int = 30
print("My name is {} and I am {} years old.".format(name, age))

# %%
# format: Formats the string
name: str = "John"
age: int = 30
print("My name is {0} and I am {1} years old.".format(name, age))

# %%
# format: Formats the string
name: str = "John"
age: int = 30
print("My name is {a} and I am {b} years old.".format(a=name, b=age))

# %%
# format_map: Formats the string using a mapping
person: dict[str:any] = {"name": "John", "age": 30}
print("My name is {name} and I am {age} years old.".format_map(person))

# %%
# index: Searches the string for a specified value and returns the position of where it was found
text: str = "hello world"
print(text.index("world"))

# %%
# isalnum: Checks if all characters are alphanumeric
text: str = "hello123"
print(text.isalnum())

# %%
# isalpha: Checks if all characters are alphabetic
text: str = "hello"
print(text.isalpha())

# %%
# isascii: Checks if all characters are ASCII
text: str = "hello"
print(text.isascii())

# %%
# isdecimal: Checks if all characters are decimals
text: str = "123"
print(text.isdecimal())

# %%
# isdigit: Checks if all characters are digits
text: str = "123"
print(text.isdigit())

# %%
# isidentifier: Checks if the string is a valid identifier
text: str = "print"
print(text.isidentifier())

# %%
# islower: Checks if all characters are lowercase
text: str = "heLlo"
print(text.islower())

# %%
# isnumeric: Checks if all characters are numeric
text: str = "123"
print(text.isnumeric())

# %%
# isprintable: Checks if all characters are printable
text: str = "hello"
print(text.isprintable())

# %%
# isspace: Checks if all characters are whitespaces
text: str = "   "
print(text.isspace())

# %%
# istitle: Checks if the string follows the rules of a title
text: str = "Hello Wurld"
print(text.istitle())

# %%
# isupper: Checks if all characters are uppercase
text: str = "HELlO"
print(text.isupper())

# %%
# join: Joins the elements of an iterable to create a string
words: list[str] = ["hello", "world", "from", "Hassan"]
print("-".join(words))

# %%
# ljust: Returns a left-justified string
text: str = "hello"
print(text.ljust(10, "*"))

# %%
# lower: Converts string into lowercase
text = "HELLO"
print(text.lower())

# %%
# lstrip: Removes leading characters
text: str = "   hello   "
print(text)
print(text.lstrip())

# %%
# maketrans: Returns a translation table to be used in translate function
intab: str = "aeiou"
outtab: str = "12345"
trans = str.maketrans(intab, outtab)
text: str = "hello"
print(text.translate(trans))

# %%
# partition: Returns a tuple where the string is parted into three parts
text: str = "hello world"
print(text.partition("o"))

# %%
# removeprefix: Removes a prefix from the string
text: str = "hello world"
print(text.removeprefix("hello "))

# %%
# removesuffix: Removes a suffix from the string
text: str = "hello world"
print(text.removesuffix(" world"))

# %%
# replace: Replaces a specified substring with another substring
text: str = "hello world"
print(text.replace("world", "universe"))

# %%
# rfind: Searches the string for a specified value and returns the last position of where it was found
text: str = "hello world hello"
print(text.rfind("hello"))

# %%
# rjust: Returns a right-justified string
text: str = "hello"
print(text.rjust(10, "*"))

# %%
# rpartition: Returns a tuple where the string is parted into three parts, starting from the right
text: str = "hello world"
print(text.rpartition("o"))

# %%
# rsplit: Splits the string at the specified separator, starting from the right
text: str = "hello world"
print(text.rsplit("o"))

# %%
# rstrip: Removes trailing characters
text: str = "   hello   "
print(text.rstrip())

# %%
# split: Splits the string at the specified separator
text = "hello world"
print(text.split(" "))

# %%
# splitlines: Splits the string at line breaks
text: str = "hello\nworld"
print(text)
print(text.splitlines())

# %%
# startswith: Checks if a string starts with a specified prefix
text: str = "hello world"
print(text.startswith("hello"))

# %%
# strip: Removes leading and trailing characters
text: str = "   hello   "
print(text.strip())

# %%
# swapcase: Swaps cases, lower case becomes upper case and vice versa
text: str = "Hello World"
print(text.swapcase())

# %%
# title: Converts the first character of each word to uppercase
text: str = "hello world"
print(text.title())

# %%
# translate: Returns a translated string
intab: str = "aeiou"
outtab: str = "123-5"
trans = str.maketrans(intab, outtab)
text: str = "hello"
print(text.translate(trans))

# %%
# upper: Converts string into uppercase
text: str = "hello"
print(text.upper())

# %%
# zfill: Fills the string with a specified number of 0 values at the beginning
text: str = "42"
print(text.zfill(5))

# %% [markdown]
# ---
# 


