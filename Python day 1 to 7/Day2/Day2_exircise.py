#Level 1
'Day 2:30 Days of python programming'

firts_name = 'John'
last_name = 'Doe'
full_name = firts_name + ' ' + last_name
country = 'USA'
city = 'New York'
age = 30
year = 2025
is_married = False
is_true = True
is_light_on = True
skills = ['Python', 'JavaScript', 'HTML', 'CSS']

#Level 2
type_of_first_name = type(firts_name)
type_of_last_name = type(last_name)
type_of_full_name = type(full_name)
type_of_country = type(country)
type_of_city = type(city)
type_of_age = type(age)
type_of_year = type(year)
type_of_is_married = type(is_married)
type_of_is_true = type(is_true)
type_of_is_light_on = type(is_light_on)
type_of_skills = type(skills)

length_of_first_name = len(firts_name)
length_of_last_name = len(last_name)

comLength = length_of_first_name > length_of_last_name

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two 
# Level 3

def circle_area():
    radius = input('Enter the radius of the circle: ')
    radius = float(radius)
    pi = 3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference
    

def askUser():
    firts_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    country = input('Enter your country: ')
    age = int(input('Enter your age: '))
    return firts_name, last_name, country, age

askUser()
circle_area()