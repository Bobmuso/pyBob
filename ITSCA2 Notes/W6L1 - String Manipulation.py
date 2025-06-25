# String literal
s1 = 'Hello, World'
s2 = "Python Program"
s3 = """This is a
multiline string"""
print(s1)
print(s2)
print(s3)

#Formating string (Presentation type)
x = f"{10:d}"
s4 = "Value: " + x
print(s4) #Vlaue: 10

y = F"{3.14159:.3f}" #3 numbers after decimal
s5 = "Pi: " + y
print(s5) #Pi: 3.142

name = f'{"Elis":s}'
s6 = "Hello, " + name
print(s6) #Hello, Elis

#Formatting string (Fiels Width and Alignment)
a = f'{10:10d}' #occupy 10 spaces
b = f'{3.14159:10f}'
c = f'{"Alice":10s}'

print([a]) #['        10'] num align to right
print([b]) #['  3.141590']
print([c]) #['Alice     '] sltring align to left

a = f'{10:<10d}' # < changes alignment to left
b = f'{3.14159:<10f}'
c = f'{"Alice":>10s}' # > changes alignment to right
d = f'{"Alice":^10s}' # ^ changes alignment to center

print([a]) #['10        ']
print([b]) #['3.141590  ']
print([c]) #['     Alice']
print([d]) #['  Alice   ']

s7 = 'Value: {:d}'.format(10)
s8 = 'Pi: {:.2f}'.format(3.14159)
name = 'Alice'
s9 = 'Hello, {}'.format(name)

age = 30

s10 = 'Name: {}, Age: {}'.format(name, age)

#Concatenat and repeat string
s11 = 'Hello, ' + 'World'
s12 = 'Repeat, ' * 4

#Stripping white space
s = ' Remove whitespace '
stripped = s.strip() # 'Removed whitespace'
lStripped = s.lstrip() # 'Removed whitespace '
rStripped = s.rstrip() # ' Removed whitespace'

# Case change
e = 'lowercase joe'
upper = e.upper() # 'LOWERCASE JOE'
lower = e.lower() # 'lowercase joe'
cap = e.capitalize() # 'Lowercase joe'
titlec = e.title() # 'Lowercase Joe'

# Comparsion Operation
s13 = 'apple'
s14 = 'banana'
print(f'a: {ord("a")}; p: {ord("p")}') # ord is to get ascii value

if s13 == s14:
    print('Equal')
elif s13 != s14:
    print('Not equal')

if s13 < s14:
    print(f'{s1} comes before {s2}')
elif s13 > s14:
    print(f'{s2} comes before {s1}')

# Searching for substring
s = 'Python Programming'
res1 = s.find('Pro') # 7
res2 = s.count('Pro') # 1
res3 = 'Pri' in s # False
res4 = s.startswith('pyth') # False, ascii value
res5 = s.endswith('ing') # True
res6 = s.replace('Python', 'Java')

t = 'Hello, World.'
res7 = t.split(',') # ['Hello', ' World.']
res8 = ','.join(res7) # ['Hello, World.']

#Checking for characters
res1 = '-27'.isdigit() #Check if only numbers (0-9) = False
res2 = 'A9876'.isalnum() #Checks for letters and numbers = True

#Regular Expression
import re
pattern = '02215'

if re.fullmatch(pattern, r'02215'): # r before text is to indicate raw text so \n will be seen as just text
    print('match')
else:
    print('no match')

s = 'The quick brown fox jumps over the lazy dog.'
pattern = r'fox'

match = re.search(pattern, s)
if match:
    print('Pattern: ', match.group()) #group() returns the word
else:
    print('Pattern not found')

pattern = r'\d' # Find number char in string

s = 'There is 123 apples in the basket'

match = re.findall(pattern, s) # ['1', '2', '3']

s = 'The quick brown fox jumps over the lazy dog.'
pattern = r'\b\w{3}\b' #\w{3} = Find 3 letter words; \b = Word is bounded by space on that side

match = re.findall(pattern, s) # ['The', 'fox', 'the', 'dog']

s = 'The quick brown fox jumps over the lazy dog.'
pattern = r'\b\w{4,}\b' #\w{4,} = Find 4 or more letter words; \b = Word is bounded by space on that side

match = re.findall(pattern, s) # ['quick', 'brown', 'jumps', 'over', 'lazy']

pattern = r'colou?r' # the ? means the letter u may or not be present

match1 = re.search(pattern, 'color')
match2 = re.search(pattern, 'colour')

text = 'Contact us at info@example.com or support@example.org'

pattern = r'[a-zA-Z0-9._%+-] + @[A-Za-z0-9.-] + \.[A-Z|a-z]{3}' #finding email

emails = re.findall(pattern, text) # ['info@example.com', 'support@example.org# ']

"""
search returns true or false + .group() returns the word
findall returns the search text in a list

expression patterns:
^ = match beginning of line
$ = match end of line
. = match any single char except newline
[...] = match char in bracket
[^...] = match char no in bracket
\w = match word characters
\W = match non-word characters
\s = match whitespaces
\S = match non-whitespaces
\d = match digits
\D = match non-digits
\A = match beginning of string
\Z or \z = match end of string
\G = match point where last match finish
x| y = match either x or y
[0-9] = match any digit
[a-z] = match any lowercase ascii letter
[A-Z] = match any upper ascii letter
[a-zA-Z0-9] = match any of the following 
[^aeiou] = match any other than lowercase vowel
[^0-9] = match any other than digit
"""

text = 'Contact us at 123-456-7890 or 555-222-4564'

pattern = r'\d{3}-\d{3}-\d{4}'

phoneNum = re.findall(pattern, text) # ['123-456-7890', '555-222-4564']

text = 'Hello, #World!'
pattern = r'[^a-zA-Z0-9\s]'

cleanText = re.sub(pattern, '', text) # 'Hello World' removes # and !


