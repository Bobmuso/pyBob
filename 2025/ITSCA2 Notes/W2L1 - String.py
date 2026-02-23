# booleans
a = 32 == 8 # False

x = 23
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
# positive

b = True and False # False
c = False or True # True
d = (30 > 45) or (27 < 30) # True

# boolean casting - empty value is seen as false (zero, empty array, empty tuple)
bool([]) # False
bool(['e']) # True
bool(0) # False
bool(69) # True
bool('') # False
bool(' ') # True

# String
name = 'John Cena'
name[-1] # returns 'a'
name[-6:] # returns 'n Cena'
name[:3] # returns 'Joh'
name[5:] # returns 'Cena'
name[4:8] # returns ' Cen'

# Escape sequences & raw strings
'\n' # New line
'\t' # Horizonal tab
'\\' # Text backslash

f = "John"
g = "Walker"
h = " "
print(f + g) # 'JohnWalker'
print(f + h + g) # 'John Walker'
print(f + " " + g) # 'John Walker'

i = "I am going to watch a movie"
i.split() # returns ['I', 'am', 'going', 'to', 'watch', 'a', 'movie']
record = "12343522;Hollow;Jack;29;123@example.com"
record.split(';') # returns ['12343522', 'Hollow', 'Jack' '29', '123@example.com']

j = ' '
j.join(["Jack", "is", "going", "home"]) # returns "Jack is going home"

k = "Top 100 Movies"
k.find('10') # returns '4'
k[8] # returns 'M'
len(k) # returns '14'

l = "Harry"
print(f"Hello, I'm {l}") # returns "Hello, I'm Harry"
print("Hello, I'm {}".format(l)) # returns "Hello, I'm Harry"
l.upper() # returns "HARRY"
l.lower() # returns "harry"

txt = """This is Coron.
She is 18 yrs old.
She is currently a student."""

name1 = "Daniel"
age = "21"
job = "programmer"

rplc1 = txt.replace("Coron", name1)
rplc1 = rplc1.replace("18", age)
rplc1 = rplc1.replace("student", job)
print(rplc1) # returns This is Daniel. She is 21 yrs old. She is currently a programmer.
