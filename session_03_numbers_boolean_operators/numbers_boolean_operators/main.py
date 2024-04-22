# %% [markdown]
# # Numbers, Boolean and Operators in Python
# 

# %% [markdown]
# ---
# 

# %% [markdown]
# ## Numbers
# 
# `Numbers` in Python come in two main flavors: integers (whole numbers) and floats (decimal numbers). You can perform various mathematical operations like addition, subtraction, multiplication, and division with them. Python also supports complex numbers for advanced calculations. Remember, numbers are essential building blocks for many programming tasks, so understanding how to work with them efficiently is key!
# 

# %% [markdown]
# ### Integers
# 
# Integers in Python are whole numbers without any decimal point. They can be positive, negative, or zero. Unlike some other programming languages, Python has arbitrary precision integers, meaning integers can be arbitrarily large without causing overflow errors. This makes Python suitable for tasks involving large integers, such as cryptography and mathematical computations.
# 

# %%
# Integers

age: int = 20
print(age)
print(type(age))

# %%
# underscores in numbers
universe_age: int = 14_000_000_000
print(universe_age)

# %%
# methods of integers
[i for i in dir(int) if "__" not in i]

# %%
# bit_count() - Returns the number of set bits in the binary representation of the integer.

x: int = 42
count: int = x.bit_count()
print("Number of set bits in", x, ":", count)

# %%
# `bit_length()` - Returns the number of bits necessary to represent the integer in binary, excluding the sign and leading zeros.

x: int = 42
length: int = x.bit_length()
print("Bit length of", x, ":", length)

# %%
# is_integer() - Returns True if the integer is finite with no fractional part, else False.

x: int = 8
is_int: bool = x.is_integer()
print(x, "is an integer?", is_int)

# %%
# denominator() - Returns the denominator of the integer

x: int = 15
denom: int = x.denominator
print("Denominator of", x, ":", denom)

# %%
# numerator() - Returns the numerator of the integer.

x: int = 25
num: int = x.numerator
print("Numerator of", x, ":", num)

# %%
# from_bytes() - Creates an integer from the given bytes object and byte order.

bytes_obj: bytes = b"\x00\x0A"
int_val = int.from_bytes(bytes_obj, byteorder="big")
print("Integer value from bytes:", int_val)

# %%
# to_bytes() - Returns the bytes representation of the integer.

x: int = 1255
bytes_rep: bytes = x.to_bytes(2, byteorder="big")
print("Bytes representation of", x, ":", bytes_rep)

# %% [markdown]
# ### Float
# 
# Floats in Python represent real numbers with a decimal point. They are used to store and manipulate numerical data that requires fractional or decimal values. Python's float type conforms to the IEEE 754 standard for floating-point arithmetic, providing a balance between precision and range. However, due to the limitations of binary representation, floats in Python may exhibit rounding errors when dealing with certain decimal values. It's essential to be aware of these limitations when working with floats, especially in critical applications like financial calculations or scientific computations. Python provides various built-in functions and methods for performing arithmetic operations, comparisons, and conversions with floats. Understanding the behavior of floats and how to handle precision and rounding issues is crucial for writing robust and accurate Python programs involving numerical computations."
# 

# %%
# Float

age: float = 20.5
print(age)
print(type(age))

# %%
# methods of floats
[i for i in dir(float) if "__" not in i]

# %%
# as_integer_ratio() - Returns a tuple representing the integer as a ratio of two integers.

x: float = 10.25
ratio: tuple[int, int] = x.as_integer_ratio()
print("Ratio of", x, ":", ratio)

# %%
# is_integer() - Returns True if the integer is finite with no fractional part, else False.

x: float = 8.5
is_int: bool = x.is_integer()
print(x, "is an integer?", is_int)

# %%
# Creating a float from a hexadecimal string
hex_string: str = "0x1.47ae147ae147bp+3"
float_value: float = float.fromhex(hex_string)
print("Float value:", float_value)

# %%
# Creating a hexadecimal string from a float
float_value: float = 10.25
hex_string: str = float.hex(float_value)
print("Float value:", hex_string)

# %% [markdown]
# ### Complex Numbers
# 
# Complex numbers in Python extend the traditional real number system by introducing the concept of an imaginary unit, denoted by \(i\). These numbers take the form \(a + bi\), where \(a\) and \(b\) are real numbers, and \(i\) represents the square root of -1. In Python, complex numbers are represented using the `complex()` constructor or by directly specifying the real and imaginary parts. They are widely used in various fields such as engineering, physics, and signal processing to model systems with both real and imaginary components. Python provides robust support for arithmetic operations, trigonometric functions, and conversions involving complex numbers, making it a versatile tool for mathematical and scientific computations involving complex phenomena. Understanding how to work with complex numbers in Python is essential for tackling a wide range of mathematical problems effectively.
# 

# %%
# complex numbers

z1: complex = 3 + 4j
print(z1)
print(type(z1))

# %%
# complex numbers

z1: complex = complex(2, -5)
print(z1)
print(type(z1))

# %%
# methods of complex numbers
[i for i in dir(complex) if "__" not in i]

# %%
# conjugate() - Returns the complex conjugate of the number.

x: complex = complex(2, -5)
conjugate: complex = x.conjugate()
print("Conjugate of", x, ":", conjugate)

# %%
# imag() - Returns the imaginary part of the number.

x: complex = 7 + 8j
imag_part: float = x.imag
print("Imaginary part of", x, ":", imag_part)

# %%
# real() - Returns the real part of the number.

x: complex = 7 + 8j
real_part: float = x.real
print("real part of", x, ":", real_part)

# %% [markdown]
# ---
# 

# %% [markdown]
# ### Boolean
# 
# Boolean values in Python, encompassing True and False, are pivotal components of programming, enabling decision-making and control flow within code. Resulting from comparison operations or logical expressions, they play a foundational role in conditional statements like if, elif, and else, as well as in loops and control structures, directing the flow of execution based on specific conditions. Python's case-sensitive keywords, True and False, are essential in constructing logical expressions and facilitating clear and effective code. Additionally, Boolean values are returned by various built-in functions and methods, signaling the success or failure of operations. With support for Boolean operations such as and, or, and not, Python facilitates the creation of intricate logical expressions, empowering programmers to navigate complex decision-making processes seamlessly. Understanding Boolean values is fundamental to proficient programming in Python, as they underpin critical aspects of logic and control within code structures.
# 

# %%
bool1: bool = True
bool2: bool = False
print(bool1)
print(type(bool2))

# %%
# methods of booleans
[i for i in dir(bool) if "__" not in i]

# %% [markdown]
# ---
# 

# %% [markdown]
# ## Operators in Python
# 
# Python divides the operators in the following groups:
# 
# - Arithmetic operators
# - Assignment operators
# - Comparison operators
# - Logical operators
# - Identity operators
# - Membership operators
# - Bitwise operators
# 

# %% [markdown]
# ### Arithmetic operators
# 
# | Operator | Name           | Example  |
# | -------- | -------------- | -------- |
# | +        | Addition       | x + y    |
# | -        | Subtraction    | x - y    |
# | \*       | Multiplication | x \* y   |
# | /        | Division       | x / y    |
# | %        | Modulus        | x % y    |
# | \*\*     | Exponentiation | x \*\* y |
# | //       | Floor division | x // y   |
# 

# %%
# Addition
x: int = 11
y: int = 25
c = x + y
print(c)

# %%
# Subtraction
x: int = 1
y: float = 11.25
c = x - y
print(c)

# %%
# Multiplication
x: int = 1 + 1j
y: complex = 11 + 1j
c = x * y
print(c)

# %%
x: str = "a"
print(x * 3)

# %%
# Division
x: int = 12
y: int = 3
c = x / y
print(c)

# %%
# Modulus
x: int = 13
y: int = 3
c = x % y
print(c)

# %%
# Exponential
x: int = 13
y: int = 3
c = x**y
print(c)

# %%
# Floor Division
x: int = 13
y: int = 3
c = x // y
print(c)

# %% [markdown]
# ### Comparison Operators
# 
# | Operator | Name                     | Example |
# | -------- | ------------------------ | ------- |
# | ==       | Equal                    | x == y  |
# | !=       | Not equal                | x != y  |
# | >        | Greater than             | x > y   |
# | <        | Less than                | x < y   |
# | >=       | Greater than or equal to | x >= y  |
# | <=       | Less than or equal to    | x <= y  |
# 
# - Comparison operators work based on ASCI code
# 

# %%
print(ord("A"))
print(chr(65))

# %%
# equal
x: int = 5
y: int = 10
c: bool = x == y
print(c)

# %%
# Not Equal
x: int = 5
y: int = 10
c: bool = x != y
print(c)

# %%
# Greater than
x: int = 5
y: int = 10
c: bool = x > y
print(c)

# %%
# Less than
x: int = 5
y: int = 10
c: bool = x < y
print(c)

# %%
# Greater than equal to
x: int = 5
y: int = 10
c: bool = x >= y
print(c)

# %%
# Less than equal to
x: int = 5
y: int = 10
c: bool = x <= y
print(c)

# %% [markdown]
# ### Logical Operators
# 
# | Operator | Description                                   | Example               |
# | -------- | --------------------------------------------- | --------------------- |
# | and      | Returns True if both statements are true      | x < 5 and x < 10      |
# | or       | Returns True if one of the statements is true | x < 5 or x < 4        |
# | not      | Reverse the result                            | not(x < 5 and x < 10) |
# 

# %%
# and
print(True and True)

# %%
# or
print(True or False)

# %%
# not
print(not True)

# %%
# examples
print(True and True and True and True)

# %%
# examples
print(True and True and True and True)

# %%
# example
print(True and True and True and True)
print(True and True and False and True)
print(False and False and False and True)

# %%
# example
print(True or True or True or True)
print(True or True or False or True)
print(False or False or False or True)
print(False or False or False or False)

# %% [markdown]
# ### Assignment Operators
# 
# | Operator | Example   | Same As      |
# | -------- | --------- | ------------ |
# | =        | x = 5     | x = 5        |
# | +=       | x += 3    | x = x + 3    |
# | -=       | x -= 3    | x = x - 3    |
# | \_=      | x \_= 3   | x = x \* 3   |
# | /=       | x /= 3    | x = x / 3    |
# | %=       | x %= 3    | x = x % 3    |
# | //=      | x //= 3   | x = x // 3   |
# | \*\*=    | x \*\*= 3 | x = x \*\* 3 |
# | &=       | x &= 3    | x = x & 3    |
# | \|=      | x\|=3     | x = x \| 3   |
# | ^=       | x ^= 3    | x = x ^ 3    |
# | >>=      | x >>= 3   | x = x >> 3   |
# | <<=      | x <<= 3   | x = x << 3   |
# 

# %%
# =
x: int = 5
print(x)

# %%
# =
a, b, c = "qasim", 7, 3.0
print(a)
print(b)
print(c)

# %%
# +=
x: int = 5
# x = x + 3
x += 3
print(x)

# %%
# -=
x: int = 5
# x = x - 3
x -= 3
print(x)

# %%
# *=
x: int = 5
# x = x * 3
x *= 3
print(x)

# %%
# /=
x: int = 5
# x = x / 3
x /= 3
print(x)

# %%
# %=
x: int = 5
# x = x % 3
x %= 3
print(x)

# %%
# //=
x: int = 5
# x = x // 3
x //= 3
print(x)

# %%
# **=
x: int = 5
# x = x ** 3
x **= 3
print(x)

# %%
# &=
x: int = 4
# x = x & 2
x &= 2
print(x)

# %%
# |=
x: int = 4
# x = x | 2
x |= 2
print(x)

# %%
# ^=
x: int = 4
# x = x ^ 2
x ^= 2
print(x)

# %%
# >>=
x: int = 5
# x = x >> 3
# 101 ---> 000
x >>= 3
print(x)

# %%
# <<=
x: int = 5
# x = x << 3
# 101 ---> 101 000
x <<= 3
print(x)

# %% [markdown]
# ### Identity Operators
# 
# | Operator | Description                                    | Example    |
# | -------- | ---------------------------------------------- | ---------- |
# | is       | Returns True if both variables are the same    | x is y     |
# | is not   | Returns True if both variables are not the sam | x is not y |
# 

# %%
x: str = "abc"
z: str = "abc"

print(id(x))
print(id(z))

# %%
i: str = "abc"
j: str = "xyz"

print(id(i))
print(id(j))

# %%
# is
print(x is z)

# %%
# is not
print(x is not j)

# %% [markdown]
# ### Membership Operators
# 
# | Operator | Example    |
# | -------- | ---------- |
# | in       | x in y     |
# | not in   | x not in y |
# 

# %%
# in
names: list[str] = [chr(i) for i in range(65, 91)]

print("D" in names)

# %%
# in
names: list[str] = [chr(i) for i in range(65, 91)]

"Pakistan" in names

# %%
# not in
names: list[str] = [chr(i) for i in range(65, 91)]

print("D" not in names)

# %% [markdown]
# ### PEDMAS
# 
# - **P** --- Parentheses/Brackets
# - **E** --- Exponents
# - **D** --- Division
# - **M** --- Multiplication
# - **A** --- Addition
# - **S** --- Subtraction
# 

# %%
print(3 + 2 - 2 * 4 / 2 + 2)

# %% [markdown]
# ---
# 


