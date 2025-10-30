#day_2
#Level 1
#Day 2: 30 Days of python programming
first_name = "Bob"
last_name = "Muso"
full_name = "Bob Muso"
country = "South Africa"
city = "East London"
age = 22
year = 2025
is_married = False
is_true = True
is_light = True

month, DOB = 'October', 2003

#Level 2
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light)
type(month)
type(DOB)

len(first_name)

print("is first_name > last_name :", len(first_name) > len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30

def findCircle(radius):
    area_of_circle = 3.14 * radius ** 2
    circum_of_circle = 2 * 3.14 * radius

radius = int(input("Enter radius: "))
findCircle(radius)

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
country = input("Enter Country: ")
age = input("Enter Age: ")

