my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Convert to set to remove duplicates and back to list
my_list = list(dict.fromkeys(my_list))

print("The list with unique elements only:")
print(my_list)